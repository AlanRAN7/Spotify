# Generated by Django 3.0.3 on 2020-03-28 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Reproduccion', '0004_auto_20200328_1156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genero',
            name='descripcion',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='genero',
            name='nombre',
            field=models.CharField(max_length=30, null=True),
        ),
    ]