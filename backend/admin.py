from django.contrib import admin
from .models import Book,Category,Booker,RentBooks
# Register your models here.

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(Booker)
admin.site.register(RentBooks)