from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from .forms import RegisterForm, LoginForm, ProfileForm, ForumForm, PostForm, CommentForm
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
    posts = Post.objects.filter(id=forumId)
    context={ 'id': forumId, 'posts': posts }
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
    context={ 'form': PostForm }
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
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if (form.is_valid()):
            user = form.save(commit='False')
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
