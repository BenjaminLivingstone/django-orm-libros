from django.shortcuts import render, HttpResponse, redirect
from . models import *

def index(request):
    context = {
        "title": "Add a Book",
        "books": Book.objects.all(),
    }
    return render(request, "index.html", context)

def addbook(request):
    # print(request.POST) Se usa para veriicar Verificar !!!
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

def bookdetail (request, num):
    context = {
        "book": Book.objects.get(id=num),
        "allauthors": Author.objects.all(),
        # "bookdetail": Book.objects.get(id=num).authors.all()
    }
    return render(request, "bookdetails.html", context)

def authordetail (request, num):
    context = {
        "author": Author.objects.get(id=num),
        "allbooks": Book.objects.all(),
        # "authordetail": Book.objects.get(id=num).authors.all()
    }
    return render(request, "authordetails.html", context)

def addbooktoauthor (request):
    context = {
        "author": Author.objects.get(id=num),
        "allbooks": Book.objects.all(),
        # "authordetail": Book.objects.get(id=num).authors.all()
    }

def addauthortobook (request):
    context = {
        "author": Author.objects.get(id=num),
        "allbooks": Book.objects.all(),
        # "authordetail": Book.objects.get(id=num).authors.all()
    }