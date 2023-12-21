# Generated by Django 4.2.1 on 2023-12-18 23:05

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Manager', '0005_delete_personal'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='duration',
            field=models.PositiveSmallIntegerField(default=24, validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AddField(
            model_name='project',
            name='event',
            field=models.CharField(choices=[('personal', 'personal on event'), ('visiting', 'organizing a visiting'), ('cleaning', 'cleaning'), ('auto', 'auto events'), ('development', 'development events'), ('security', 'event security'), ('exhibition', 'exhibition services'), ('moving', 'moving events'), ('trucking', 'trucking on events'), ('parcking', 'parking organization'), ('photography', 'event photography'), ('analisis', 'data analysis events'), ('web design', 'web design events'), ('svg Animations', 'svg animations events'), ('ui development', 'ui development events'), ('testing', 'testing events')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='project',
            name='start_date',
            field=models.DateField(null=True),
        ),
        migrations.CreateModel(
            name='PersonalList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(250), django.core.validators.MaxValueValidator(100000)])),
                ('category', models.CharField(choices=[('Not changed', 'Not changed'), ('animators', 'animators'), ('auxiliary workers', 'auxiliary workers'), ('barmens', 'barmens'), ('carpenters', 'carpenters'), ('cleaners', 'cleaners'), ('coordinators', 'coordinators'), ('copying and duplicating machine operators', 'copying and duplicating machine operators'), ('delivers', 'delivers'), ('doormens', 'doormens'), ('drivers', 'drivers'), ('helpers', 'helpers'), ('laborers', 'laborers'), ('loaders', 'loaders'), ('models for presentation', 'models for presentation'), ('nurses', 'nurses'), ('orderlies', 'orderlies'), ('paramedics', 'paramedics'), ('parking attendants', 'parking attendants'), ('promo-models', 'promo-models'), ('promo-personal', 'promo-personal'), ('promoters', 'promoters'), ('security', 'security'), ('security guards', 'security guards'), ('supervisors', 'supervisors'), ('temporary staff', 'temporary staff'), ('waiters', 'waiters')], default=('Not changed', 'Not changed'), max_length=100)),
                ('count', models.PositiveSmallIntegerField(validators=[django.core.validators.MinValueValidator(1)])),
                ('project', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='personal_list', to='Manager.project')),
            ],
        ),
    ]