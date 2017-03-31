from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import RegisterForm, LoginForm, ProfileForm, ForumForm, PostForm, CommentForm, UserForm
from .auth import createuser
from django.contrib.auth import authenticate, login as auth_login, logout as auth_logout
from django.contrib.auth.decorators import login_required
from .models import Forum, Post, Comment


@login_required
def index(request):
    template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


@login_required
def forums(request):
    forums = Forum.objects.all()
    template = loader.get_template('forums.html')
    context={ 'forums': forums }
    return HttpResponse(template.render(context, request))


@login_required
def forum(request, forumId):
    template = loader.get_template('forum.html')
    forum = Forum.objects.get(id=forumId)
    posts = Post.objects.filter(forum=forum)
    context={ 'id': forumId, 'posts': posts, 'title': forum.title }
    return HttpResponse(template.render(context, request))


@login_required
def post(request, postId):
    template = loader.get_template('post.html')
    post = Post.objects.get(id=postId)
    context = {'post': post,
               'form': CommentForm,
               'comments': Comment.objects.filter(post=post)
              }
    return HttpResponse(template.render(context, request))


# TODO: admin required
def createForum(request):
    if request.method == 'POST':
        form = ForumForm(request.POST)
        if (form.is_valid()):
            title = form.cleaned_data['title']
            forum = Forum.objects.create(title=title)
            forum.save()
            return HttpResponseRedirect('/forum/'+str(forum.id))
    template = loader.get_template('new_forum.html')
    context={ 'form': ForumForm }
    return HttpResponse(template.render(context, request))


@login_required
def createPost(request, forumId):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if (form.is_valid()):
            title = form.cleaned_data['title']
            text = form.cleaned_data['text']
            forum = Forum.objects.get(id=forumId)
            user = request.user
            post = Post.objects.create(title=title,
                                       text=text,
                                       forum=forum,
                                       user=user
            )
            post.save()
            return HttpResponseRedirect('/post/'+str(post.id))
    template = loader.get_template('new_post.html')
    context = {'form': PostForm}
    return HttpResponse(template.render(context, request))


@login_required
def createComment(request, postId):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if (form.is_valid()):
            text = form.cleaned_data['text']
            post = Post.objects.get(id=postId)
            user = request.user
            comment = Comment.objects.create(text=text,
                                             post=post,
                                             user=user
            )
            comment.save()
            return HttpResponseRedirect('/post/'+str(postId))
    return HttpResponse(status=404)


def entry(request):
    template = loader.get_template('entry.html')
    if request.user.is_authenticated:
        template = loader.get_template('index.html')
    context = {}
    return HttpResponse(template.render(context, request))


@login_required
def profile(request):
    error_msg = ""
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
        else:
            error_msg = "Please choose at least one disease."
    template = loader.get_template('profile.html')
    profile_data = {
        'is_patient': request.user.profile.is_patient,
        'disease_interests': request.user.profile.disease_interests,
    }
    user_data = {
        'first_name': request.user.first_name,
        'last_name': request.user.last_name,
    }
    profile_form = ProfileForm(profile_data)
    user_form = UserForm(user_data)
    context = {
        'user_form': user_form,
        'profile_form': profile_form,
        'email': request.user.email,
        'error_msg': error_msg
    }
    status = 200 if error_msg == "" else 400
    return HttpResponse(template.render(context, request), status=status)


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
