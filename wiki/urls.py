from django.urls import path

from . import views

urlpatterns = [
    path('', views.wikiMatrix, name='wikiMatrix'),
]
