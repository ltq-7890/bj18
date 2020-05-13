from django.http import HttpResponse

def index(request):
    retutn HttpResponse('index')