# Generated by Django 2.1.7 on 2019-02-26 14:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0003_companyreg'),
    ]

    operations = [
        migrations.CreateModel(
            name='add_company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('symbol', models.CharField(max_length=1)),
                ('password', models.CharField(max_length=10)),
                ('email', models.EmailField(max_length=30)),
                ('address', models.CharField(max_length=30)),
                ('phonenumber', models.IntegerField(max_length=30)),
                ('select', models.CharField(max_length=10)),
                ('image', models.ImageField(max_length=30, upload_to='')),
            ],
        ),
    ]
