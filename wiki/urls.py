from django.urls import path

from . import views

urlpatterns = [
    path('', views.wikiMatrix, name='wikiMatrix'),
    path('list/<int:rpk>/<int:cpk>/', views.wikiList, name='wikiList'),
]
