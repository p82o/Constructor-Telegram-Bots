# Generated by Django 4.1.6 on 2023-04-03 01:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TelegramBotCommand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('command', models.CharField(max_length=32, null=True)),
                ('callback', models.CharField(max_length=64, null=True)),
                ('message_text', models.TextField()),
                ('keyboard', models.JSONField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='TelegramBotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.BigIntegerField()),
                ('username', models.CharField(max_length=32)),
                ('date_started', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='TelegramBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('token', models.CharField(max_length=50, unique=True)),
                ('private', models.BooleanField(default=True)),
                ('is_running', models.BooleanField(default=False)),
                ('date_added', models.DateTimeField(auto_now_add=True)),
                ('allowed_users', models.ManyToManyField(related_name='allowed_users', to='telegram_bot.telegrambotuser')),
                ('commands', models.ManyToManyField(to='telegram_bot.telegrambotcommand')),
                ('users', models.ManyToManyField(related_name='users', to='telegram_bot.telegrambotuser')),
            ],
        ),
    ]
