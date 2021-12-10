# Generated by Django 3.2.9 on 2021-12-04 04:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TrainInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('train_id', models.CharField(max_length=200)),
                ('railway', models.CharField(max_length=500)),
                ('operator', models.CharField(max_length=200)),
                ('information', models.CharField(max_length=2000)),
            ],
        ),
    ]