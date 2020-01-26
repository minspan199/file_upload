from django.urls import path
from .views import IndexView
from . import views

app_name = 'uploader'
urlpatterns = [

    path('', views.index, name='index'),
    path('view-database', views.database, name='database'),

]
