from django.urls import path 
from . import views
urlpatterns = [
    path('',views.showAllBooks,name="homepage"),
    path('books/',views.createBook,name="addbooks"),
    path('error/',views.errorPage,name="errorpage"),
    path('category/',views.createCategory,name="addcategory"),
    path('booker/',views.createBooker,name="addbooker"),
    path('rent/<str:name>/',views.rentBook,name='rentbook'),
    path('history/',views.history,name='history'),
]