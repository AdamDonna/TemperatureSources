# Generated by Django 2.2.6 on 2019-10-08 11:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Thermometer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(max_length=255)),
                ('base_url', models.TextField(max_length=255)),
                ('is_enabled', models.BooleanField(default=False)),
                ('is_celcius', models.BooleanField(default=True)),
                ('api_key', models.TextField(default='', max_length=255)),
                ('polymorphic_ctype', models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='polymorphic_api.thermometer_set+', to='contenttypes.ContentType')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
        ),
        migrations.CreateModel(
            name='OpenWeatherMap',
            fields=[
                ('thermometer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Thermometer')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('api.thermometer',),
        ),
        migrations.CreateModel(
            name='WeatherBit',
            fields=[
                ('thermometer_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='api.Thermometer')),
            ],
            options={
                'abstract': False,
                'base_manager_name': 'objects',
            },
            bases=('api.thermometer',),
        ),
    ]
