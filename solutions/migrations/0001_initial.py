# Generated by Django 3.0.3 on 2020-05-13 05:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='submissions',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('id1', models.IntegerField(blank=True)),
                ('Date', models.DateTimeField(blank=True, null=True)),
                ('user1', models.CharField(blank=True, max_length=264, null=True)),
                ('Result', models.IntegerField(blank=True)),
                ('Time', models.DecimalField(blank=True, decimal_places=5, max_digits=6)),
                ('mem', models.CharField(blank=True, max_length=264, null=True)),
                ('lang', models.CharField(blank=True, max_length=264, null=True)),
                ('sol', models.CharField(blank=True, max_length=264, null=True)),
            ],
        ),
    ]
