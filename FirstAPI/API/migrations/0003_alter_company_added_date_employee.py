# Generated by Django 5.0.1 on 2024-04-22 18:12

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('API', '0002_rename_id_company_company_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='added_date',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.EmailField(max_length=50)),
                ('address', models.CharField(max_length=100)),
                ('phone', models.CharField(max_length=11)),
                ('about', models.TextField()),
                ('position', models.CharField(choices=[('Manager', 'Manager'), ('Software Developer', 'Software Developer'), ('Testing', 'Testing'), ('Project Leader', 'Project Leader'), ('Intern', 'Intern')], max_length=50)),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='API.company')),
            ],
        ),
    ]
