from django.shortcuts import render
from .models import Neighbourhood

# Create your views here.

def index(request):
    hoods = Neighbourhood.objects.all()
    return render(request, 'hood/index.html',{'hoods':hoods})
