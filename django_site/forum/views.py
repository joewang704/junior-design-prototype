from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import RegisterForm, LoginForm, ProfileForm
from .auth import createuser
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required


@login_required
def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


def entry(request):
    template = loader.get_template('entry.html')
    if request.user.is_authenticated:
        template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


@login_required
def profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        print "a"
        if (form.is_valid()):
            print "b"
            #fname = form.cleaned_data['fname']
            #lname = form.cleaned_data['fname']
            user = form.save(commit='False')
            print user.first_name
            user.save()
    template = loader.get_template('profile.html')
    data = {'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            }
    profile_form = ProfileForm(data)
    context = {'form': profile_form,
               'email': request.user.email,
               }
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
                return HttpResponseRedirect('/')
            except IntegrityError:
                errorMsg = 'User already exists'
    template = loader.get_template('register.html')
    context = {'form': RegisterForm, 'errorMsg': errorMsg}
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
                return HttpResponseRedirect('/')
            else:
                errorMsg = 'Username or password was not found'
    template = loader.get_template('login.html')
    context = {'form': LoginForm, 'errorMsg': errorMsg}
    return HttpResponse(template.render(context, request))


def logout(request):
    if request.user.is_authenticated:
        auth_logout(request)
    return HttpResponseRedirect('/')
