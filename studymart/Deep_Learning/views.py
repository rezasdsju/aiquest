from django.shortcuts import render
from django.http import HttpResponse
def deep_learning(request):
    return render(request, 'deep_learning.html')
    