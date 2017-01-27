from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /forum/
    url(r'^$', forum.index, name='index'),
]