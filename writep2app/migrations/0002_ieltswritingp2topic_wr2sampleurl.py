# Generated by Django 2.0.3 on 2018-04-28 06:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('writep2app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ieltswritingp2topic',
            name='wr2sampleurl',
            field=models.URLField(default='', max_length=500),
            preserve_default=False,
        ),
    ]