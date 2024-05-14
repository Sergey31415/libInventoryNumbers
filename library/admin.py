from django.contrib import admin

from library.models import Author, Book, Section, Inv

admin.site.register(Author)
admin.site.register(Book)
admin.site.register(Section)
admin.site.register(Inv)