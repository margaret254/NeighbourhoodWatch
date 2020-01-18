from django.shortcuts import render

# Create your views here.

def hood(request):
    return render(request, 'hood/index.html')
