from django.shortcuts import render
from .models import Date, MainLunch, SubLunch


# Create your views here.
def index(request):
    # DB에서 전체 게시글을 조회 후
    dates = Date.objects.all()
    mainlunchs = MainLunch.objects.all()
    sublunchs = SubLunch.objects.all()

    # 메인 페이지를 응답 (render)
    # context는 다름 이름이여도 상관 없음(단, 반드시 딕셔너리여야 함)
    context = {
        'dates': dates,
        'mainlunchs': mainlunchs,
        'sublunchs': sublunchs,
    }
    
    return render(request, 'articles/index.html', context)



# context = {
#     'dates': dates
    
# }

# dates = [
#     {
#     'id': 1
#     'lunch_date': '2024'
#     },
    
#     {
#     'id': 2
#     'lunch_date': '2024'
#     },
# ]