# Generated by Django 4.2.11 on 2024-04-19 00:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('post', '0003_comment_delete_choice_delete_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='content',
            field=models.CharField(max_length=200, null=True),
        ),
    ]
