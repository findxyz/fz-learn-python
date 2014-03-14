from django.http import HttpResponse
import datetime

def hello(request):
    return HttpResponse('Hello World')

def home(request):
    now = datetime.datetime.now()
    html = '<html><body>Welcome! Now time is %s.</body></html>' % now
    return HttpResponse(html)