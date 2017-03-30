"""django_site URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from forum import views

urlpatterns = [
    url(r'^$', views.entry, name='entry'),
    url(r'^register/', views.register, name='register'),
    url(r'^login/', views.login, name='login'),
    url(r'^logout/', views.logout, name='logout'),
    url(r'^profile/', views.profile, name='profile'),
    url(r'^index/', views.index, name='index'),
    url(r'^admin/', admin.site.urls),
    url(r'^forums/', views.forums),
    url(r'^forums/', views.forums, name='forums'),
    url(r'^forum/(?P<forumId>\d+)/$', views.forum, name='forum'),
    url(r'^post/(?P<postId>\d+)/$', views.post, name='post'),
    url(r'^createForum/', views.createForum, name='createForum'),
    url(r'^createPost/(?P<forumId>\d+)/$', views.createPost, name='createPost'),
    url(r'^createComment/(?P<postId>\d+)/$', views.createComment, name='createComment'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
