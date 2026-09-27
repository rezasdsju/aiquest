from django.shortcuts import render
from django.http import HttpResponse
def machine_learning(request):
    return render(request, 'machine_learning.html')
    
