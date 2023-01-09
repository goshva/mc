# Generated by Django 4.1.5 on 2023-01-09 09:13

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Good',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('discription', models.CharField(max_length=300)),
                ('text', models.TextField()),
                ('kind', models.CharField(max_length=300)),
                ('name', models.CharField(max_length=200)),
                ('photo_url', models.CharField(max_length=1000)),
                ('article', models.CharField(max_length=20)),
                ('color', models.CharField(max_length=250)),
                ('price_5k', models.FloatField()),
                ('price_10k', models.FloatField()),
                ('price_20k', models.FloatField()),
                ('price_many', models.FloatField()),
                ('size', models.FloatField()),
                ('weight', models.FloatField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('published_date', models.DateTimeField(blank=True, null=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
