# Generated by Django 4.0.3 on 2022-04-11 23:06

from django.db import migrations, models
from nextServer import settings

class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GISource',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('university_fk', models.IntegerField()),
                ('required_degree_fk', models.IntegerField()),
                ('contact1', models.CharField(max_length=20)),
                ('email1', models.CharField(max_length=20)),
                ('contact2', models.CharField(max_length=20)),
                ('email2', models.CharField(max_length=20)),
                ('url', models.CharField(max_length=255)),
                ('post_date', models.DateField()),
                ('close_date', models.DateField()),
                ('start_date', models.DateField()),
                ('job_fk', models.IntegerField()),
                ('has_close_date', models.SmallIntegerField(max_length=1)),
                ('number_of_vacancy', models.IntegerField()),
                ('vacancy_name', models.CharField(max_length=20)),
                ('vacancy_rank', models.CharField(max_length=20)),
                ('label', models.TextField()),
                ('still_open', models.SmallIntegerField()),
                ('verified', models.SmallIntegerField()),
                ('provider', models.CharField(max_length=20)),
                ('provider_email', models.CharField(max_length=255)),
                ('country_fk', models.IntegerField()),
                ('country', models.IntegerField()),
                ('job', models.IntegerField()),
            ],
            options={
                'db_table': 'GISource',
                'managed': False,
            },
        ),
    ]
