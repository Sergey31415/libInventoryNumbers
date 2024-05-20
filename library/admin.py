from audioop import reverse

from django.contrib import admin
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.utils.html import format_html

from library import models
from library.models import Author, Book, Section, Inv


from django.contrib import admin
from django.db import models
from django.urls import reverse
from django.utils.html import format_html

from library.views import inventory_number_management

admin.site.register(Author)

admin.site.register(Section)
admin.site.register(Inv)
#admin.site.register(Book)


#@admin.register(Book)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'data_full', 'link')

    def link(self, obj):
        url =reverse(inventory_number_management, args=[obj.pk])
        return format_html('<button style="background-color:black"><a href="{}" target="_blank">Перейти</a></button>', url)
    link.short_description = 'Управление инвентарными номерами'

admin.site.register(Book, BookAdmin)




























"""

def bulk_add_invs(modeladmin, request, queryset):
    if request.method == 'POST':
        book_id = request.POST.get('book')
        start_number = int(request.POST.get('start_number'))
        end_number = int(request.POST.get('end_number'))

        book = Book.objects.get(id=book_id)
        for number in range(start_number, end_number + 1):
            inv = Inv.objects.create(number=number)
            inv.books.add(book)

        modeladmin.message_user(request, "Inventory numbers successfully added.")
        return HttpResponseRedirect(request.get_full_path())

    return render(request, 'inventory_number_management.html', {'books': queryset})

bulk_add_invs.short_description = "Bulk Add Inventory Numbers"

class BookAdmin(admin.ModelAdmin):
    actions = [bulk_add_invs]


admin.site.register(Book, BookAdmin)

"""