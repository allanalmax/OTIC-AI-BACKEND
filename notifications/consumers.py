import json
from channels.generic.websocket import WebsocketConsumer, AsyncWebsocketConsumer
from django.template import Context, Template


class NotificationConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        await self.accept()
        await self.channel_layer.group_add("notifications", self.channel_name)

    async def disconnect(self, close_code):
        await self.channel_layer.group_discard("notifications", self.channel_name)

    async def send_notification(self, event):
        message = event["message"]

        template = Template(
            '<div class="notification"><p>{{message}}</p><button type="button" class="close" data-dismiss="alert" aria-label="Close"><span aria-hidden="true">&times;</span></button></div>'
        )
        context = Context({"message": message})
        rendered_notification = template.render(context)

        await self.send(
            text_data=json.dumps(
                {"type": "notification", "message": rendered_notification}
            )
        )
