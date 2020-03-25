from django.urls import path

from . import views

app_name='wiki'

urlpatterns = [
    path('', views.wikiMatrix, name='wikiMatrix'),
    path('register-<int:regPk>', views.wikiMatrix, name='wikiMatrix'),
    path('list-<int:rowPk>-<int:colPk>/', views.wikiList, name='wikiList'),
    path('create-<int:rowPk>-<int:colPk>/', views.wikiCreateView, name="wikiCreate"),
]
