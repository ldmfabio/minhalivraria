# Generated by Django 4.2.5 on 2023-09-27 17:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('minhalivraria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Editora',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=100)),
                ('site', models.URLField(blank=True, null=True)),
            ],
        ),
    ]
