# Generated by Django 2.1.7 on 2019-04-08 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coordinatorinfo',
            name='CSATScoreImage',
            field=models.ImageField(upload_to='uploads/', verbose_name='CAST score image'),
        ),
        migrations.AlterField(
            model_name='coordinatorinfo',
            name='profileImage',
            field=models.ImageField(upload_to='uploads/', verbose_name='profile picture'),
        ),
        migrations.AlterField(
            model_name='coordinatorinfo',
            name='schoolScoreImage',
            field=models.ImageField(upload_to='uploads/', verbose_name='school score image'),
        ),
    ]