# Generated by Django 5.0.6 on 2024-06-07 13:19

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('librarian_app', '0003_rename_bloque_emprunteur_bloquer_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='livre',
            old_name='nom',
            new_name='name',
        ),
        migrations.AddField(
            model_name='livre',
            name='date_emprunt',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='livre',
            name='disponible',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='livre',
            name='emprunteur',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='librarian_app.emprunteur'),
        ),
        migrations.CreateModel(
            name='CD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_emprunt', models.DateField(blank=True, null=True)),
                ('disponible', models.BooleanField(default=True)),
                ('artiste', models.CharField(max_length=150)),
                ('emprunteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='librarian_app.emprunteur')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='DVD',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=150)),
                ('date_emprunt', models.DateField(blank=True, null=True)),
                ('disponible', models.BooleanField(default=True)),
                ('realisateur', models.CharField(max_length=150)),
                ('emprunteur', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='librarian_app.emprunteur')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
