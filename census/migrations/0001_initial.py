# Generated by Django 2.2.7 on 2019-12-07 21:36

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sightings',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Latitude', models.FloatField()),
                ('Longitude', models.FloatField()),
                ('Unique_Squirrel_ID', models.CharField(max_length=100)),
                ('Shift', models.CharField(choices=[('AM', 'AM'), ('PM', 'PM')], max_length=4)),
                ('Date', models.DateField()),
                ('Age', models.CharField(blank=True, choices=[('Adult', 'Adult'), ('Juvenile', 'Juvenile'), ('?', '?')], default='', max_length=50)),
                ('Primary_Fur_Color', models.CharField(blank=True, choices=[('Gray', 'Gray'), ('Cinnamon', 'CInnamon'), ('Black', 'Black')], default='', max_length=100)),
                ('Location', models.CharField(blank=True, choices=[('Ground Plane', 'Ground Plane'), ('Above Ground', 'Above Ground')], default='', max_length=100)),
                ('Specific_Location', models.CharField(blank=True, default='', max_length=100)),
                ('Running', models.BooleanField()),
                ('Chasing', models.BooleanField()),
                ('Climbing', models.BooleanField()),
                ('Eating', models.BooleanField()),
                ('Foraging', models.BooleanField()),
                ('Other_Activities', models.CharField(blank=True, default='', max_length=500)),
                ('Kuks', models.BooleanField()),
                ('Quaas', models.BooleanField()),
                ('Moans', models.BooleanField()),
                ('Tail_flags', models.BooleanField()),
                ('Tail_twitches', models.BooleanField()),
                ('Approaches', models.BooleanField()),
                ('Indifferent', models.BooleanField()),
                ('Runs_from', models.BooleanField()),
            ],
        ),
    ]
