from django.urls import path

from . import views

app_name='wiki'

urlpatterns = [
    path('', views.wikiMatrix, name='wikiMatrix'),
    path('list/<int:rpk>/<int:cpk>/', views.wikiList, name='wikiList'),
    path('create/<int:rpk>/<int:cpk>/', views.wikiCreateView, name="wikiCreate"),
]
