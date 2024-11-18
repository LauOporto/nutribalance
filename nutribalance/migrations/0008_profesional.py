# Generated by Django 5.1.1 on 2024-11-17 23:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('nutribalance', '0007_registrocomida'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profesional',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=100)),
                ('apellido', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.CharField(max_length=128)),
            ],
        ),
    ]
