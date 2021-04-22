# Generated by Django 3.0.8 on 2020-07-24 06:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Vacancy',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50, verbose_name='Bashliq')),
                ('content', models.TextField(verbose_name='Vakansiya')),
                ('dead_line', models.DateField(verbose_name='Bitmə tarixi')),
                ('date_created', models.DateField(auto_now_add=True, verbose_name='Yaradılma tarixi')),
                ('freelance', models.BooleanField(verbose_name='Freelance imkanı')),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
