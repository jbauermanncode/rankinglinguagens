# Generated by Django 4.0.6 on 2022-08-04 14:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('linguagens_api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='linguagem',
            old_name='image',
            new_name='url',
        ),
        migrations.AlterField(
            model_name='linguagem',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]