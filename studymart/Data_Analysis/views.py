from django.shortcuts import render
from django.http import HttpResponse
def data_analysis(request):
    return render(request, 'analysis.html')