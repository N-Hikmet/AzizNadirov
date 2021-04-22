# Generated by Django 3.0.8 on 2020-07-28 10:41

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('vacancy', '0004_auto_20200724_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment_1',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_author', models.TextField(max_length=20, verbose_name='Ad')),
                ('email', models.EmailField(max_length=254, verbose_name='Elektron poçt')),
                ('body', models.TextField(verbose_name='Şərh')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Yaradılma tarixi')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='Yenilənmə tariix')),
                ('active', models.BooleanField(default=True, verbose_name='Aktiv')),
                ('vacancy', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='vacancy.Vacancy')),
            ],
        ),
    ]
