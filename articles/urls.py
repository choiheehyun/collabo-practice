from django.urls import path
from . import views

# URL 분리시에 urlpatterns를 선언하지 않으면 에러 발생
app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
]