"""Blog URL configuration

"""
from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', view=views.post_list, name='post_list'),

]