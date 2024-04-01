from django.db import models

# Create your models here.
# model class 설계도 초안을 작성하는 것
# 1. 필드 이름 (클래스 변수명)
# 2. 필드의 데이터 타입 (model field)
# 3. 필드의 제약조건 (model field 키워드 인자)
class Date(models.Model):
    lunch_date = models.DateTimeField(auto_now=False)


class MainLunch(models.Model):
    title = models.CharField(max_length=10)
    content_20_korean_menu = models.TextField()
    content_20_special_menu = models.TextField()   
    
    
class SubLunch(models.Model):
    title = models.CharField(max_length=10)
    content_10_lunchbox_menu = models.TextField()
    content_10_sandwich_menu = models.TextField()
    content_10_salad_menu = models.TextField()
