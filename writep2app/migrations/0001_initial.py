# Generated by Django 2.0.3 on 2018-04-28 06:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('uid', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Ieltswritingp2topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wr2topic', models.CharField(max_length=1000)),
                ('wr2question', models.CharField(max_length=2000)),
                ('pub_date', models.DateTimeField(verbose_name='date published')),
            ],
        ),
        migrations.AddField(
            model_name='answers',
            name='topic',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='writep2app.Ieltswritingp2topic'),
        ),
    ]
