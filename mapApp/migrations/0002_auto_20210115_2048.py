# Generated by Django 2.2 on 2021-01-15 20:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('mapApp', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='theftnotification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='incidentnotification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='hazardnotification',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='alertarea',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
        migrations.AddField(
            model_name='administrativearea',
            name='users',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL, verbose_name='users'),
        ),
        migrations.CreateModel(
            name='Weather',
            fields=[
                ('incident', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='mapApp.Incident')),
                ('summary', models.CharField(max_length=250, verbose_name='Summary')),
                ('sunrise_time', models.DateTimeField(verbose_name='Sunrise time')),
                ('sunset_time', models.DateTimeField(verbose_name='Sunset time')),
                ('dawn', models.BooleanField(verbose_name='The accident occurred at dawn')),
                ('dusk', models.BooleanField(verbose_name='The accident occurred at dusk')),
                ('precip_intensity', models.FloatField(verbose_name='Precipitation intensity (mm/h)')),
                ('precip_probability', models.FloatField(verbose_name='Precipitation probability')),
                ('precip_type', models.CharField(max_length=50, verbose_name='Type of precipitation')),
                ('temperature', models.FloatField(verbose_name='Temperature (C)')),
                ('black_ice_risk', models.BooleanField(verbose_name='Black ice risk present')),
                ('wind_speed', models.FloatField(verbose_name='Wind speed (km/h)')),
                ('wind_bearing', models.FloatField(verbose_name='Wind bearing (deg)')),
                ('wind_bearing_str', models.CharField(max_length=5, verbose_name='Wind bearing')),
                ('visibility_km', models.FloatField(verbose_name='Visibility (km)')),
            ],
            options={
                'verbose_name': 'Weather',
                'verbose_name_plural': 'Weather',
            },
        ),
        migrations.AddField(
            model_name='theftnotification',
            name='point',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='theftNotification', to='mapApp.Theft'),
        ),
        migrations.AddField(
            model_name='incidentnotification',
            name='point',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='incidentNotification', to='mapApp.Incident'),
        ),
        migrations.AddField(
            model_name='hazardnotification',
            name='point',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='hazardNotification', to='mapApp.Hazard'),
        ),
        migrations.AlterUniqueTogether(
            name='theftnotification',
            unique_together={('user', 'point')},
        ),
        migrations.AlterUniqueTogether(
            name='incidentnotification',
            unique_together={('user', 'point')},
        ),
        migrations.AlterUniqueTogether(
            name='hazardnotification',
            unique_together={('user', 'point')},
        ),
    ]
