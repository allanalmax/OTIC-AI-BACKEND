# Generated by Django 4.2.4 on 2023-08-23 11:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chatbot', '0003_remove_document_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolDocuments',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('content', models.TextField()),
            ],
        ),
    ]