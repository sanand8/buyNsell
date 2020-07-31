# Generated by Django 3.0.7 on 2020-07-31 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Sell',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(upload_to='pics')),
                ('price', models.IntegerField()),
                ('contact', models.CharField(max_length=10)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
