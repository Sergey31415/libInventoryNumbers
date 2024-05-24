from audioop import reverse

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.html import format_html
from django.utils.regex_helper import Choice
from simple_history.admin import SimpleHistoryAdmin

from library import models
from library.models import Author, Book, Section, Inv, Poll

from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.utils.html import format_html

from library.views import inventory_number_management

admin.site.register(Author)

admin.site.register(Section)
admin.site.register(Inv)
#admin.site.register(HistoricalBook)


#@admin.register(Book)


class BookAdmin(SimpleHistoryAdmin):
    list_display = ('title', 'data_full', 'link')
    def link(self, obj):
        url =reverse(inventory_number_management, args=[obj.pk])
        return format_html('<button style="background-color:black"><a href="{}" target="_blank">Перейти</a></button>', url)
    link.short_description = 'Управление инвентарными номерами'

    def history_button(self, obj):
        url = reverse('admin:library_book_history', args=[obj.pk])  # Создаем URL для просмотра истории изменений книги
        return format_html('<a class="button" href="{}">История</a>',
                           url)  # Создаем ссылку на страницу просмотра истории
    history_button.short_description = 'История'  # Задаем краткое описание для колонки в административной панели

admin.site.register(Book, BookAdmin)
