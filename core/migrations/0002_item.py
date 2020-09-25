# Generated by Django 3.0 on 2020-09-24 15:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('list', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.List')),
            ],
        ),
    ]
