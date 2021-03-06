# Generated by Django 3.2 on 2022-03-13 18:59

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='EventType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Log',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('user_email', models.EmailField(max_length=254)),
                ('user_ip', models.GenericIPAddressField()),
                ('event_question', models.CharField(max_length=1000)),
                ('user_answer', models.CharField(max_length=2000)),
                ('user_datetime', models.DateTimeField(auto_now_add=True)),
                ('event_type_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='zayed_university_app.eventtype')),
            ],
        ),
    ]
