from django.urls import path
from . import views

app_name = "logins_front"
urlpatterns = [
    path('', views.index, name='index'),
]