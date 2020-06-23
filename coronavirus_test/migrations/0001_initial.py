# Generated by Django 2.2.4 on 2020-04-20 13:40

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CoronaVirusTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('phone', models.CharField(max_length=12)),
                ('cough', models.IntegerField(blank=True, null=True)),
                ('cold', models.IntegerField(blank=True, null=True)),
                ('diarrhea', models.IntegerField(blank=True, null=True)),
                ('sore_throat', models.IntegerField(blank=True, null=True)),
                ('body_aches', models.IntegerField(blank=True, null=True)),
                ('headaches', models.IntegerField(blank=True, null=True)),
                ('fever', models.IntegerField(blank=True, null=True)),
                ('difficulty_breathing', models.IntegerField(blank=True, null=True)),
                ('fatigue', models.IntegerField(blank=True, null=True)),
                ('travelled_14days_ago', models.IntegerField(blank=True, null=True)),
                ('travel_history_to_infected_area', models.IntegerField(blank=True, null=True)),
                ('contact_with_infected', models.IntegerField(blank=True, null=True)),
                ('result', models.IntegerField(blank=True, null=True)),
                ('pub_date', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
    ]
