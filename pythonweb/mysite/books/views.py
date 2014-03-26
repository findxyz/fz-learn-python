from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse
from books.models import Book
# Create your views here.

def search_form(request):
    return render_to_response("search_form.html")

def search(request):
    if 'q' in request.GET and request.GET['q']:
        q = request.GET['q']
        books = Book.objects.filter(title__contains=q)
        dic = {
            "books": books,
            "q": q
        }
        return render_to_response("search_results.html", dic)
    else:
        return HttpResponse('Please submit a search term.<br/><a href=%s>Back to search_form!</a>' % ('/books/search_form'))
