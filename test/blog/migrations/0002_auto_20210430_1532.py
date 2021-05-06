# Generated by Django 3.2 on 2021-04-30 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blog',
            name='email',
            field=models.EmailField(default='0', max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='file',
            field=models.FileField(default='0', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='image',
            field=models.ImageField(default='0', null=True, upload_to=''),
        ),
        migrations.AddField(
            model_name='blog',
            name='updated_at',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='url',
            field=models.URLField(default='0', null=True),
        ),
        migrations.AddField(
            model_name='blog',
            name='when',
            field=models.IntegerField(default='0', null=True),
        ),
    ]
