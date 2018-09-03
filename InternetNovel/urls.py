from django.urls import path
from . import views


app_name = 'InternetNovel'
urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('login/', views.Login, name='login'),
]
