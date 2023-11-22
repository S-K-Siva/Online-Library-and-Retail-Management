from django.forms import ModelForm
from .models import Book,Category,Booker

class bookForm(ModelForm):
    class Meta:
        model = Book
        fields = "__all__"


class categoryForm(ModelForm):
    class Meta:
        model = Category
        fields = "__all__"

class bookerForm(ModelForm):
    class Meta:
        model = Booker
        fields = "__all__"