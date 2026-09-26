from django.shortcuts import render
from django.http import HttpResponse

def about_us(request):
    return HttpResponse('This is About Us Page')