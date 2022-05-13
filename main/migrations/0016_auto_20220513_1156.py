# Generated by Django 3.2.9 on 2022-05-13 09:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_auto_20220513_1104'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='fri',
            field=models.CharField(default=-9, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='mon',
            field=models.CharField(default=-1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='sat',
            field=models.CharField(default=-1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='sun',
            field=models.CharField(default=-1, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='thu',
            field=models.CharField(default=-2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='tue',
            field=models.CharField(default=-2, max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='doctor',
            name='wed',
            field=models.CharField(default=-4, max_length=255),
            preserve_default=False,
        ),
        migrations.DeleteModel(
            name='Schedule',
        ),
    ]