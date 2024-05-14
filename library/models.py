from django.utils import timezone

from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


COVERS = (
    ('Твёрдый', 'Твёрдый'),
    ('Мягкий', 'Мягкий'),
    ('Пружинный', 'Пружинный'),

)

LANGUAGES = (
    ('kg', 'Кыргызский'),
    ('ru', 'Русский'),
    ('eng', 'Английский'),
)

BOOK_STATUS = (
    ('Черновик', 'Черновик'),
    ('Скрытый', 'Скрытый'),
    ('Открытый', 'Открытый'),
)


class Author(models.Model):
    id_author = models.AutoField(primary_key=True)
    surname = models.CharField(max_length=70, default=" ")
    name = models.CharField(max_length=70)
    patronym = models.CharField(max_length=70, blank=True, null=True)
    initials = models.CharField(max_length=70, blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    def __str__(self):
        if self.patronym:
            return f'{self.surname+" "+self.name+" "+self.patronym}'
        return f'{self.surname+" "+self.name}'


class Section(models.Model):  # разделы
    id_section = models.AutoField(primary_key=True)
    section = models.CharField(max_length=30)

    def __str__(self):
        return f'{self.section}'


class Inv(models.Model):  # инвентарный номер
    id_in = models.AutoField(primary_key=True)
    num = models.CharField(max_length=70)

    def __str__(self):
        return f'{self.num}'


class Book(models.Model):
    image = models.FileField(upload_to='book_images/', null=True, blank=True)
    id_book = models.AutoField(primary_key=True)
    book_status = models.CharField(max_length=20, choices=BOOK_STATUS, default='Открытый')
    udk = models.CharField(max_length=20, blank=True, null=True)
    bbk = models.CharField(max_length=20, blank=True, null=True)
    author_sign = models.CharField(max_length=20, blank=True, null=True)
    author = models.ManyToManyField(Author)
    language = models.CharField(max_length=30, choices=LANGUAGES, default='ru')
    title = models.CharField(max_length=140)
    izdanie = models.CharField(max_length=15, blank=True, null=True)
    section = models.ForeignKey(Section, on_delete=models.CASCADE, blank=True, null=True, verbose_name="Направление (секция)")  # TODO может быть список издательств
    discipline = models.CharField(max_length=30, blank=True, null=True, verbose_name="Предмет")
    public_year = models.IntegerField(
        validators=[
            MinValueValidator(1000),
            MaxValueValidator(9999)
        ]
    )  # год издания
    publisher = models.CharField(max_length=140, blank=True, null=True, verbose_name="Издатель")  # издательство
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Цена")  # цена покупки
    cover_type = models.CharField(max_length=20, choices=COVERS, verbose_name="Тип обложки")  # тип обложки
    purchase_date = models.DateField(blank=True, null=True, verbose_name="Дата поступления")
    pages_amt = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(9999)
        ], blank=True, null=True, verbose_name="Количество страниц"  # количество страниц
    )
    number_of_copies = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(999)
        ], blank=True, null=True, verbose_name="Количество копий"
    )
    inv = models.ManyToManyField(Inv, verbose_name="Инвертарный номер") #инвентарный номер
    isbn = models.CharField(max_length=20, null=True, blank=True)
    isbn2 = models.CharField(max_length=20, null=True, blank=True)
    notes = models.TextField(blank=True, null=True)
    data_full = models.BooleanField(default=False, verbose_name="Информация о книге полная")

    online_copy = models.FileField(upload_to='books/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        authors = ', '.join([str(author) for author in self.author.all()])
        return f'"{self.title}" - {authors}'

    def save(self, *args, **kwargs):
        if self.online_copy.name:
            current_file = self.online_copy.name
            latin_name = current_file
            # Обновить файл с латинской транслитерацией
            self.online_copy.name = latin_name

            # Call the original save method to save the file
        super(Book, self).save(*args, **kwargs)