from django.http import HttpResponse

def hello(request):
    return HttpResponse("hello world! This is my first trial.")
