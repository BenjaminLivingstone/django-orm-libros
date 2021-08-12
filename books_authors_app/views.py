from django.shortcuts import render, HttpResponse, redirect
from . models import *

def index(request):
    context = {
        "title": "Add a Book",
        "books": Book.objects.all(),
    }
    return render(request, "index.html", context)

def addbook(request):
    # print(request.POST) Verificar !!!
    book=Book.objects.create(title=request.POST['book_title'], desc=request.POST['book_desc'])
    return redirect("/")

def author(request):
    context = {
        "title": "Add an Author",
        "authors": Author.objects.all(),
    }
    return render(request, "authors.html", context)

def addauthor(request):
    author= Author.objects.create(first_name=request.POST['author_first_name'], last_name=request.POST['author_last_name'], notes=request.POST['author_notes'])
    return redirect("/authors/")

# def some_method(request):

# 	return redirect("/") 

# def books(request):
#     context = {
#         "title": "Add a Book",
#     }
#     return render(request, "books.html", context)
