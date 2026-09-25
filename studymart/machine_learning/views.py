from django.shortcuts import render
from django.http import HttpResponse
def machine_learning(request):
    return HttpResponse('<h1>Study Mart Offering a lot of courses</h1>')
    
def deep_learning(request):
    return HttpResponse('<h1>Study Mart Offering Deep Learning course</h1>')
    
def about_us(request):
    return HttpResponse('<p>We have available a lot of experience teachers</p>')
    