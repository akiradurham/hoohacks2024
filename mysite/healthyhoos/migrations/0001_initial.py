# Generated by Django 4.2.10 on 2024-03-24 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('is_public', models.BooleanField(default=False)),
                ('likes', models.IntegerField(default=0)),
                ('calendarID', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
                ('groups', models.ManyToManyField(related_name='users', to='healthyhoos.group')),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('category_code', models.CharField(max_length=3)),
                ('time', models.TimeField()),
                ('description', models.TextField()),
                ('users', models.ManyToManyField(related_name='tasks', to='healthyhoos.user')),
            ],
        ),
        migrations.AddField(
            model_name='group',
            name='admin_users',
            field=models.ManyToManyField(related_name='admin_groups', to='healthyhoos.user'),
        ),
        migrations.AddField(
            model_name='group',
            name='tasks',
            field=models.ManyToManyField(related_name='groups', to='healthyhoos.task'),
        ),
    ]
