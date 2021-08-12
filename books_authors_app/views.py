from django.shortcuts import render, HttpResponse, redirect

def index(request):
    context = {
        "title": "Books & Authors",
    }
    return render(request, "index.html", context)

# def some_method(request):

# 	return redirect("/") 