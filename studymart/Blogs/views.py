from django.shortcuts import render
from django.http import HttpResponse
def blog1(request):
    return HttpResponse('<p>This is our first blog</p>')