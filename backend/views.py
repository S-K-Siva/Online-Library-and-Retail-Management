from django.shortcuts import render,redirect
from .models import Book,Category,Booker,RentBooks
# Create your views here.

def showAllBooks(request):
    books = Book.objects.all()
    return render(request,'backend/index.html',{"books":books})

def errorPage(request):
    return render(request,'errorPage.html')

def createBook(request):
    categories = [x.name.upper() for x in Category.objects.all()]
    if request.POST:
        name = request.POST['name']
        authorName = request.POST['author']
        description = request.POST['description']
        category = request.POST['category'].upper()
        categoryId = None
        if category.upper() not in categories:
            mycategory = Category.objects.create(name=category)
            mycategory.save()
            categoryId = mycategory
        else:
            categoryId = Category.objects.get(name=category)
        if name and authorName and description:
            myBook = Book.objects.create(name=name,authorName=authorName,description=description,category=categoryId)
            myBook.save()
            return redirect('homepage')
        else:
            return render(request,'errorpage')
    return render(request,'forms/bookforms.html')

def createCategory(request):
    categories = [x.name.upper() for x in Category.objects.all()]
    if request.POST:
        name = request.POST['name'].upper()
        if name in categories:
            return redirect('homepage')
        if name:
            myCategory = Category.objects.create(name=name)
            myCategory.save()
            return redirect('homepage')
        else:
            return render(request,'errorpage')
    return render(request,'forms/bookcategory.html')


def createBooker(request):
    bookers = [x.name for x in Booker.objects.all()]
    if request.POST:
        bookerName = request.POST['name']
        bookerAge = request.POST['age']
        bookerBio = request.POST['bio']
        if bookerName in bookers:
            return redirect('homepage')
        if bookerName and bookerAge and bookerBio:
            mybooker = Booker.objects.create(name=bookerName,age=bookerAge,bio=bookerBio)
            mybooker.save()
            return redirect('homepage')
        else:
            return render(request,'errorpage')
    return render(request,'forms/bookbooker.html')

def rentBook(request,name):
    bookers = [x.name.upper() for x in Booker.objects.all()]
    # books = [x.name.upper().strip() for x in Book.objects.all()]
    book = Book.objects.get(name=name)
    name = name.upper().strip()
    
    if request.POST:
        bookerName = request.POST['name'].upper()
        booker = None
        if bookerName in bookers:
            booker = Booker.objects.get(name=request.POST['name'])
        else:
            return render(request,'forms/nobooker.html')
        
        obj = RentBooks.objects.create(book=book,booker=booker)
        return redirect('homepage')
    
    return render(request, 'forms/rentbook.html',{"book":book})

def history(request):
    all_history = RentBooks.objects.all()
    return render(request,'backend/history.html',{'data':all_history})
