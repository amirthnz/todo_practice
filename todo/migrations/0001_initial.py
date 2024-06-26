# Generated by Django 5.0.4 on 2024-04-04 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150)),
                ('content', models.CharField(max_length=300)),
                ('done', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
