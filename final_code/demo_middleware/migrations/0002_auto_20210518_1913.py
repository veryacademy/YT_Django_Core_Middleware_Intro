# Generated by Django 3.2.3 on 2021-05-18 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('demo_middleware', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='newstats',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('win', models.IntegerField()),
                ('mac', models.IntegerField()),
                ('iph', models.IntegerField()),
                ('android', models.IntegerField()),
                ('oth', models.IntegerField()),
            ],
        ),
        migrations.DeleteModel(
            name='stats',
        ),
    ]
