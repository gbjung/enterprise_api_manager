# Generated by Django 3.2.4 on 2021-06-17 18:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Endpoint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('base_url', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Vertical',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('vertical', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='verticals.vertical')),
            ],
        ),
        migrations.CreateModel(
            name='Parameter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('accepted_values', models.TextField()),
                ('description', models.TextField()),
                ('endpoint', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='verticals.endpoint')),
            ],
        ),
        migrations.AddField(
            model_name='endpoint',
            name='section',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='verticals.section'),
        ),
        migrations.CreateModel(
            name='Constraint',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('description', models.TextField()),
                ('value', models.TextField()),
                ('endpoints', models.ManyToManyField(to='verticals.Endpoint')),
            ],
        ),
    ]
