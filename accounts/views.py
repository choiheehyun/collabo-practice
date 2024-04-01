from django.shortcuts import render, redirect
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login as auth_login


# Create your views here.
def login(request):
    # 요청 메서드가 POST라면, 사용자 입력 데이터를 활용해 로그인을 진행
    if request.method == 'POST':
        # AuthenticationForm은 ModelForm이 아니라 Form
        # 사용자가 입력하는 데이터를 DB에 저장하지 않기 때문
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            user = form.get_user()
            # 로그인을 진행 (세션을 생성)
            auth_login(request, user)
            return redirect('accounts:complete_login')
    # 요청 메서드가 POST가 아니라면, login 페이지를 응답
    context = {
        'form': form,
    } 
    return render(request, 'articles/index.html', context)
    # return redirect('articles:index')
    
def complete_login(request):
    return render(request,'accounts/complete_login.html' )

