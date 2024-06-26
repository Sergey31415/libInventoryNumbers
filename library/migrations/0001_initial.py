# Generated by Django 5.0.6 on 2024-05-14 09:14

import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id_author', models.AutoField(primary_key=True, serialize=False)),
                ('surname', models.CharField(default=' ', max_length=70)),
                ('name', models.CharField(max_length=70)),
                ('patronym', models.CharField(blank=True, max_length=70, null=True)),
                ('initials', models.CharField(blank=True, max_length=70, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Inv',
            fields=[
                ('id_in', models.AutoField(primary_key=True, serialize=False)),
                ('num', models.CharField(max_length=70)),
            ],
        ),
        migrations.CreateModel(
            name='Section',
            fields=[
                ('id_section', models.AutoField(primary_key=True, serialize=False)),
                ('section', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('image', models.FileField(blank=True, null=True, upload_to='book_images/')),
                ('id_book', models.AutoField(primary_key=True, serialize=False)),
                ('book_status', models.CharField(choices=[('Черновик', 'Черновик'), ('Скрытый', 'Скрытый'), ('Открытый', 'Открытый')], default='Открытый', max_length=20)),
                ('udk', models.CharField(blank=True, max_length=20, null=True)),
                ('bbk', models.CharField(blank=True, max_length=20, null=True)),
                ('author_sign', models.CharField(blank=True, max_length=20, null=True)),
                ('language', models.CharField(choices=[('kg', 'Кыргызский'), ('ru', 'Русский'), ('eng', 'Английский')], default='ru', max_length=30)),
                ('title', models.CharField(max_length=140)),
                ('izdanie', models.CharField(blank=True, max_length=15, null=True)),
                ('discipline', models.CharField(blank=True, max_length=30, null=True, verbose_name='Предмет')),
                ('public_year', models.IntegerField(validators=[django.core.validators.MinValueValidator(1000), django.core.validators.MaxValueValidator(9999)])),
                ('publisher', models.CharField(blank=True, max_length=140, null=True, verbose_name='Издатель')),
                ('price', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Цена')),
                ('cover_type', models.CharField(choices=[('Твёрдый', 'Твёрдый'), ('Мягкий', 'Мягкий'), ('Пружинный', 'Пружинный')], max_length=20, verbose_name='Тип обложки')),
                ('purchase_date', models.DateField(blank=True, null=True, verbose_name='Дата поступления')),
                ('pages_amt', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(9999)], verbose_name='Количество страниц')),
                ('number_of_copies', models.IntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(999)], verbose_name='Количество копий')),
                ('isbn', models.CharField(blank=True, max_length=20, null=True)),
                ('isbn2', models.CharField(blank=True, max_length=20, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('data_full', models.BooleanField(default=False, verbose_name='Информация о книге полная')),
                ('online_copy', models.FileField(blank=True, null=True, upload_to='books/')),
                ('created_at', models.DateTimeField(auto_now_add=True, null=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('author', models.ManyToManyField(to='library.author')),
                ('inv', models.ManyToManyField(to='library.inv', verbose_name='Инвертарный номер')),
                ('section', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='library.section', verbose_name='Направление (секция)')),
            ],
        ),
    ]
