from django.contrib import admin

from .models import Book

class BookAdmin(admin.ModelAdmin):
    search_fields = ('title', 'author', 'publication_year')
    search__fields = ('title', 'author')

admin.site.register(Book)
# Register your models here.
