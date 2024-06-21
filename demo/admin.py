from demo.models import *
from django.contrib import admin


@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "isbn", "qty", "price", "sotuvda_bormi")

@admin.register(Sale)
class SaleAdmin(admin.ModelAdmin):
    list_display = ("book", "qty", "price", "total_price", "created_at",)
   


# admin.register(Book, BookAdmin)
admin.site.register(Todo)