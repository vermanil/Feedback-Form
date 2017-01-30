from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def showBase(request):
    return render(request, 'feedback/form.html', {'Name':'Django'})

def formProcess(request):
    HttpResponse("hello world")
