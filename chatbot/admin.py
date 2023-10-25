from django.contrib import admin
from .models import Chat,SchoolDocuments,Profile,TransactionsDetails,FlutterwaveDetails

# Register your models here.
admin.site.register(Chat)
admin.site.register(SchoolDocuments)
admin.site.register(Profile)
admin.site.register(FlutterwaveDetails)
admin.site.register(TransactionsDetails)