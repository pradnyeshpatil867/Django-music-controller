from django.shortcuts import render, HttpResponse

# Create your views here.
def main(request):
    return HttpResponse('<h1>hello Django and react</h1>')
