from django.contrib import admin

from .models import Book
from .models import Author
from .models import Publisher

class BookModelAdmin(admin.ModelAdmin):
    list_display=['__unicode__', 'author','status']
    list_filter=['status']
    search_fields=['author', 'status']
    class Meta:
        model=Book

class AuthorModelAdmin(admin.ModelAdmin):
    list_display=['first_name','second_name','contry']
    search_fields=['first_name', 'second_name']
    class Meta:
        model=Author


class PublisherModelAdmin(admin.ModelAdmin):
    list_display=['name', 'city']
    search_fields=['name', 'city']
    class Meta:
        model=Publisher

admin.site.register(Book,BookModelAdmin)
admin.site.register(Author,AuthorModelAdmin)
admin.site.register(Publisher,PublisherModelAdmin)
