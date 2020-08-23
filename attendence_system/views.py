from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template import loader
from django.contrib import messages
from .forms import LoginForm

# Create your views here.
def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request,
                                username=cd['username'],
                                password=cd['password'])
            if user is not None:
                if user.is_active:
                    # login(request, user)
                    # return HttpResponse('Authenticated '\
                    #                     'successfully')
                    context = {}
                    return render(request, 'attendence_system/home2.html', context)
                else:
                    return HttpResponse('Disabled account')
            else:
                return HttpResponse('Invalid login')
    else:
        form = LoginForm()
    return render(request, 'attendence_system/registration/login.html', {'form': form})


@login_required
def dashboard(request):
    return render(request,
                  'attendence_system/dashboard.html',
                  {'section': 'dashboard'})
@login_required
def home(request):
    return render(request, 'attendence_system/home2.html', {'section': 'home'})



@login_required
def record_attn(request):
    return render(request, 'attendence_system/record_attendence.html', {'section': 'record_attn'})


@login_required
def attn_records(request):
    return render(request, 'attendence_system/attn_records.html', {'section': 'attn_records'})

@login_required
def register_user(request):
    return render(request, 'attendence_system/register.html',  {'section': 'register_user'})
