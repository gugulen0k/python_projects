# Generated by Django 3.1.1 on 2020-11-15 09:35

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lesson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Название предмета')),
                ('slug', models.SlugField(unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Homework',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255, verbose_name='Название Д/З')),
                ('slug', models.SlugField(unique=True)),
                ('file', models.FileField(upload_to='files/')),
                ('description', models.TextField(null=True, verbose_name='Описание')),
                ('publication_date', models.DateField(default=datetime.date.today, verbose_name='Дата публикации Д/З')),
                ('expiration_date', models.DateField(verbose_name='Срок сдачи Д/З')),
                ('homework', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home_page.lesson', verbose_name='Предмет')),
            ],
        ),
    ]