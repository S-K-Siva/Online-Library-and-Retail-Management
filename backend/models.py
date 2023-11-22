from django.db import models

# Create your models here.
from django.db import models

class Book(models.Model):
    name = models.CharField(max_length=200)
    authorName = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    category = models.ForeignKey('Category',on_delete=models.CASCADE,null=True,blank=True)
    created = models.DateTimeField(auto_now=True)
    class Meta:
        db_table="book"
    
    def __str__(self):
        return self.name
class Category(models.Model):
    name = models.CharField(max_length=200)
    created = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table="category"
    
    def __str__(self):
        return self.name

class Booker(models.Model):
    name = models.CharField(max_length=200)
    age = models.IntegerField(null=False,blank=False)
    bio = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now=True)
    class Meta:
        db_table="booker"
    
    def __str__(self):
        return self.name

class RentBooks(models.Model):
    book = models.ForeignKey(Book,on_delete=models.CASCADE,null=True,blank=True)
    booker = models.ForeignKey(Booker,on_delete=models.CASCADE,null=True,blank=True)
    created = models.DateTimeField(auto_now=True)

    class Meta:
        db_table="rentbooks"

    def __str__(self):
        return f"{self.book.name} -> {self.booker.name}"