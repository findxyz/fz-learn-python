from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from books.models import Book
from books.forms import ContactForm
# Create your views here.

# def search_form(request):
#     return render_to_response("search_form.html")

def search(request):
    errors = []
    if 'q' in request.GET:
        q = request.GET['q']
        if not q:
            errors.append("Please enter a term.")
        elif len(q) > 20:
            errors.append("Please enter at most 20 characters.")
        else:
            books = Book.objects.filter(title__contains=q)
            dic = {
                "books": books,
                "q": q
            }
            return render_to_response("search_results.html", dic)
    return render_to_response('search_form.html', {"errors": errors})

def contact(request):
    dic = {}
    dic.update(csrf(request))
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print cd
            return HttpResponseRedirect('/books/contact/thanks/')
    else:
        form = ContactForm()
    dic['form'] = form
    return render_to_response('contact.html', dic)

def contact_thanks(request):
    return render_to_response('contact_thanks.html')



