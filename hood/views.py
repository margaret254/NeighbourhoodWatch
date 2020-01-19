from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.decorators import login_required
from .forms import *
from django.contrib.auth.models import User

# Create your views here.
@login_required(login_url='/accounts/register/')
def index(request):
    hoods = Neighbourhood.objects.all()
    return render(request, 'hood/index.html',{'hoods':hoods})

def search_results(request):

    if 'hood' in request.GET and request.GET["hood"]:
        search_term = request.GET.get("hood")
        searched_hoods = Neighbourhood.search_by_name(search_term)
        message = f"{search_term}"

        return render(request, 'hood/search.html',{"message":message,"hoods": searched_hoods})

    else:
        message = "You haven't searched for any neighbourhood"
        return render(request, 'hood/search.html',{"message":message})

@login_required(login_url='/accounts/login/')
def hood(request,id):
    hoods = Neighbourhood.objects.get(id=id)
    return render(request,'hood/hood.html',{"hoods":hoods})

@login_required(login_url='/accounts/login/')
def new_hood(request):
    current_user = request.user
    if request.method == 'POST':
        form = NewHoodForm(request.POST, request.FILES)
        if form.is_valid():
            hood = form.save(commit=False)
            hood.admin = current_user
            hood.save()
        return redirect('index')

    else:
        form = NewHoodForm()
    return render(request, 'new_hood.html', {"form": form})


def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            post = form.save(commit=False)
            post.profile = current_user
            post.save()
        return redirect('index')

    else:
        form = ProfileForm()
    return render(request, 'hood/profile.html', {"form": form})
