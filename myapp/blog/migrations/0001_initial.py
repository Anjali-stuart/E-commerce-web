# Generated by Django 3.2.3 on 2021-11-13 23:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=34)),
                ('last_name', models.CharField(max_length=40)),
            ],
            options={
                'db_table': 'Student',
            },
        ),
    ]
