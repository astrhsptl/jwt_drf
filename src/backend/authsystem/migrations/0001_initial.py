# Generated by Django 5.0.1 on 2024-01-03 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('username', models.CharField(max_length=50, unique=True, verbose_name='Username')),
                ('avatar', models.ImageField(blank=True, upload_to='user/avatar', verbose_name='Avatar')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='Email')),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=False)),
                ('is_seller', models.BooleanField(default=False)),
            ],
            options={
                'indexes': [models.Index(fields=['id'], name='id_index')],
            },
        ),
    ]
