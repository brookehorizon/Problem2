# Generated by Django 4.0 on 2022-06-25 17:43

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='t1',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('height', models.CharField(max_length=100)),
                ('weight', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='t2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('game_no', models.CharField(max_length=100)),
                ('activity_1', models.CharField(max_length=100)),
                ('activity_2', models.CharField(max_length=100)),
                ('activity_3', models.CharField(max_length=100)),
                ('year', models.CharField(max_length=100)),
                ('narrative', models.CharField(max_length=100)),
            ],
        ),
    ]