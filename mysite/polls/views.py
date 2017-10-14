from django.http import HttpResponse

def index(request):
    return HttpResponse("polls index :)")
# Create your views here.
