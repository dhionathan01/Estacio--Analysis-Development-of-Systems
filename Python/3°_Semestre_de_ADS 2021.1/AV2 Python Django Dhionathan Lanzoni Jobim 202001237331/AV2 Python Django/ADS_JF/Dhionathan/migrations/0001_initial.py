# Generated by Django 3.2.3 on 2021-06-10 13:53

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Disciplina',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=100)),
                ('periodo', models.IntegerField(unique=True)),
                ('dia_da_semana', models.CharField(max_length=20)),
                ('hora_inicio', models.CharField(max_length=5)),
                ('hora_fim', models.CharField(max_length=5)),
                ('professor', models.CharField(max_length=5)),
            ],
        ),
        migrations.CreateModel(
            name='Professor',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('nome', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Tipo_de_Avaliacao',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('tipo', models.CharField(max_length=3)),
            ],
        ),
        migrations.CreateModel(
            name='Avaliacao',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('dia_da_semana', models.CharField(max_length=20)),
                ('nota', models.DecimalField(decimal_places=1, max_digits=2)),
                ('disciplina', models.CharField(max_length=50)),
                ('tipo_de_avaliacao', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Dhionathan.tipo_de_avaliacao')),
            ],
        ),
    ]
