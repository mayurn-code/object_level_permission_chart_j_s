# Generated by Django 3.0.7 on 2020-11-30 13:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Application',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=40)),
                ('details', models.CharField(max_length=50)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('brand', models.CharField(choices=[('Tata', 'Tata'), ('ford', 'ford'), ('mahindra', 'mahindra'), ('hundai', 'hundai')], max_length=50)),
                ('model_no', models.CharField(max_length=20)),
                ('purchase_date', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'permissions': [('can_view_brand_name_only', 'Can View Brand Name Only'), ('can_view_model_no', 'Can View Model No')],
            },
        ),
    ]