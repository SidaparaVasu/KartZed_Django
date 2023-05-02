# Generated by Django 4.1 on 2023-05-02 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GameCategory',
            fields=[
                ('game_category_id', models.AutoField(primary_key=True, serialize=False)),
                ('game_category_name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GameFeatures',
            fields=[
                ('game_feature_id', models.AutoField(primary_key=True, serialize=False)),
                ('game_feature_name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='GameModes',
            fields=[
                ('game_mode_id', models.AutoField(primary_key=True, serialize=False)),
                ('game_mode_name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Offer',
            fields=[
                ('offer_id', models.AutoField(primary_key=True, serialize=False)),
                ('offer_name', models.CharField(max_length=225)),
                ('offer_description', models.CharField(max_length=220)),
                ('offer_tc', models.CharField(max_length=220)),
            ],
        ),
        migrations.CreateModel(
            name='OperatingSystems',
            fields=[
                ('os_id', models.AutoField(primary_key=True, serialize=False)),
                ('os_name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Plan',
            fields=[
                ('plan_id', models.AutoField(primary_key=True, serialize=False)),
                ('points', models.IntegerField()),
                ('amount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Platform',
            fields=[
                ('platform_id', models.AutoField(primary_key=True, serialize=False)),
                ('platform_name', models.CharField(max_length=25, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='VideoCards',
            fields=[
                ('vc_id', models.AutoField(primary_key=True, serialize=False)),
                ('vc_name', models.CharField(max_length=50, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='VCVersions',
            fields=[
                ('vc_version_id', models.AutoField(primary_key=True, serialize=False)),
                ('vc_version_name', models.CharField(max_length=50, unique=True)),
                ('vc_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.videocards')),
            ],
        ),
        migrations.CreateModel(
            name='Processors',
            fields=[
                ('processor_id', models.AutoField(primary_key=True, serialize=False)),
                ('processor_name', models.CharField(max_length=50, unique=True)),
                ('os_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.operatingsystems')),
            ],
        ),
        migrations.CreateModel(
            name='OSVersions',
            fields=[
                ('version_id', models.AutoField(primary_key=True, serialize=False)),
                ('version', models.CharField(max_length=50, unique=True)),
                ('os_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Administrator.operatingsystems')),
            ],
        ),
    ]
