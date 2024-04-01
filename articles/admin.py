from django.contrib import admin
from .models import Date, MainLunch, SubLunch

# Register your models here.
# admin site에 등록한다.
# register 메서드에는 서로 다른(연관이 없는) 클래스를 함께 넣을 수 없음.
admin.site.register(Date)
admin.site.register(MainLunch)
admin.site.register(SubLunch)