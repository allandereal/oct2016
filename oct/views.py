from django.http import HttpResponse
from django.shortcuts import render

from oct.models import Company


def hello(request):
    return HttpResponse("Hello")


def companies(request):
    cos = Company.objects.all()
    return HttpResponse(cos)


def companies2(request):
    cos = Company.objects.all()
    context = {
        'cos': cos,
    }
    return render(request, 'oct/temp.html', context)
