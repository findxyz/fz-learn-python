from django.shortcuts import render, render_to_response
from django.http import Http404, HttpResponse
import datetime

def hello(request):
    return HttpResponse('Hello World')

def home(request):
    now = datetime.datetime.now()
    html = '<html><body>Welcome! Now time is %s.</body></html>' % now
    return HttpResponse(html)

def hours_ahead(request, offset):
    try:
        offset = int(offset)
    except ValueError:
        raise Http404()
    dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
    dic = {
        "offset": offset,
        "dt": dt,
        "parent": "base.html"
    }
    return render_to_response("date/hours_ahead.html", dic)

def current_time(request):
    now = datetime.datetime.now()
    dic = {
        "current_time": now,
        "title": "current_time"
    }
    return render_to_response("date/current_time.html", dic)

def request_meta(request):
    values = request.META.items()
    values.sort()
    html = []
    html.append("<tr><td>%s</td><td>%s</td></tr>" % ("request.path", request.path))
    html.append("<tr><td>%s</td><td>%s</td></tr>" % ("request.get_host()", request.get_host()))
    html.append("<tr><td>%s</td><td>%s</td></tr>" % ("request.get_full_path()", request.get_full_path()))
    for k, v in values:
        html.append("<tr><td>%s</td><td>%s</td></tr>" % (k, v))
    dic = {
        "request_meta": "\n".join(html)
    }
    return render_to_response("request_meta.html", dic)