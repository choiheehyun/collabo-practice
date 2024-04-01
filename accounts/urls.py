from django.urls import path
from . import views

# URL 분리시에 urlpatterns를 선언하지 않으면 에러 발생
app_name = 'accounts'
urlpatterns = [
    path('login/', views.login, name='login'),
    path('complete_login/', views.complete_login, name='complete_login'),
]