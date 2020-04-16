# Generated by Django 3.0.3 on 2020-03-28 17:56

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Reproduccion', '0003_auto_20200327_1518'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='album',
            options={'verbose_name': 'Album', 'verbose_name_plural': 'Albumes'},
        ),
        migrations.AlterModelOptions(
            name='cancion',
            options={'verbose_name': 'Cancion', 'verbose_name_plural': 'Canciones'},
        ),
        migrations.AlterModelOptions(
            name='disquera',
            options={'verbose_name': 'Disquera', 'verbose_name_plural': 'Disqueras'},
        ),
        migrations.AlterModelOptions(
            name='genero',
            options={'verbose_name': 'Genero', 'verbose_name_plural': 'Generos'},
        ),
        migrations.AlterModelOptions(
            name='playlist',
            options={'verbose_name': 'Playlist', 'verbose_name_plural': 'Playlists'},
        ),
        migrations.AlterModelOptions(
            name='playlistcanciones',
            options={'verbose_name': 'PlaylistCancion', 'verbose_name_plural': 'PlaylistCanciones'},
        ),
        migrations.AlterModelOptions(
            name='usuariocanciones',
            options={'verbose_name': 'UsuarioCancion', 'verbose_name_plural': 'UsuarioCanciones'},
        ),
        migrations.AddField(
            model_name='album',
            name='disquera',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Reproduccion.Disquera'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='album',
            name='genero',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='Reproduccion.Genero'),
            preserve_default=False,
        ),
    ]
