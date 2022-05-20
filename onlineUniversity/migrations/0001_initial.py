# Generated by Django 4.0.2 on 2022-04-21 09:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='admin',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(blank=True, max_length=200, null=True)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('thumbnail', models.ImageField(blank=True, max_length=200, null=True, upload_to='')),
                ('description', models.TextField(blank=True, null=True)),
                ('video_url', models.ImageField(blank=True, max_length=200, null=True, upload_to='')),
                ('course_type', models.CharField(choices=[('free', 'free'), ('paid', 'paid')], default='free', max_length=20)),
            ],
        ),
    ]