from django.contrib import admin
from books.models import Publisher, Author, Book

class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', )
    search_fields = ('first_name', 'last_name', 'email', )

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publication_date', )
    list_filter = ('publication_date', 'publisher', )
    date_hierarchy = 'publication_date'
    # BookAdmin's ordering will override Book's ordering see the detail in Book
    ordering = ('publication_date', )
    fields = ('title', 'authors', 'publisher', 'publication_date', )
    filter_horizontal = ('authors', )
    # filter_vertical = ('authors', )
    raw_id_fields = ('publisher', )

# Register your models here.
admin.site.register(Publisher)
admin.site.register(Author, AuthorAdmin)
admin.site.register(Book, BookAdmin)