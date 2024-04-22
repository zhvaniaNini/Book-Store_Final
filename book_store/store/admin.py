from django.contrib import admin
from store.models import Book, Author, Category

# Register your models here.
@admin.register(Author)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name']
    search_fields = ['name']

@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ['name', 'page_count', 'price']
    search_fields = ['name']

admin.site.register(Category)
