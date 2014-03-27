from django.core.context_processors import csrf
from django.core.mail import send_mail
from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse, HttpResponseRedirect
from books.models import Book
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
    errors = []
    if request.method == 'POST':
        if not request.POST.get('subject', ''):
            errors.append('Enter a subject.')
        if not request.POST.get('message', ''):
            errors.append('Enter a message.')
        if request.POST.get('email') and '@' not in request.POST.get('email'):
            errors.append('Enter a valid e-mail address.')
        if not errors and request.POST.get('email'):
            send_mail(
                request.POST['subject'],
                request.POST['message'],
                'djangomail@126.com',
                [request.POST.get('email')]
            )
            return HttpResponseRedirect('/books/contact/thanks/')
    dic["errors"] = errors
    return render_to_response('contact.html', dic)

def contact_thanks(request):
    return render_to_response('contact_thanks.html')



