from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import RegisterForm, LoginForm
from .auth import createuser
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required

@login_required
def index(request):
    template = loader.get_template('index.html')
    context={}
    return HttpResponse(template.render(context, request))

def entry(request):
    template = loader.get_template('entry.html')
    if request.user.is_authenticated:
        template = loader.get_template('index.html')
    context={}
    return HttpResponse(template.render(context, request))

def register(request):
    errorMsg = ''
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        if (form.is_valid()):
            email = form.cleaned_data['email']
            fname = form.cleaned_data['fname']
            lname = form.cleaned_data['lname']
            password = form.cleaned_data['password']
            try:
                createuser(
                    email=email,
                    fname=fname,
                    lname=lname,
                    password=password
                )
                user = authenticate(username=email, password=password)
                auth_login(request, user)
                return HttpResponseRedirect('/index/')
            except IntegrityError:
                errorMsg = 'User already exists'
    template = loader.get_template('register.html')
    context={ 'form': RegisterForm, 'errorMsg': errorMsg }
    return HttpResponse(template.render(context, request))

def login(request):
    errorMsg = ''
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if (form.is_valid()):
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(username=email, password=password)
            if user is not None:
                auth_login(request, user)
                return HttpResponseRedirect('/index/')
            else:
                errorMsg = 'Username or password was not found'
    template = loader.get_template('login.html')
    context={ 'form': LoginForm, 'errorMsg': errorMsg }
    return HttpResponse(template.render(context, request))

def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return HttpResponseRedirect('/')

