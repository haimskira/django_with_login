# Generated by Django 4.0.6 on 2023-03-05 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('age', models.DecimalField(decimal_places=0, max_digits=3)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('image', models.ImageField(blank=True, default='/placeholder.png', null=True, upload_to='')),
            ],
        ),
    ]
