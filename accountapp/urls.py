from django.urls import path
from . import views
from accountapp.views import hhh, AccountCreateView, AccountDetailView

from django.contrib.auth.views import LoginView, LogoutView
app_name = "accountapp"

urlpatterns = [
    path('hhh/', hhh, name = 'hhhu'), # 함수형 뷰는 그냥 이름 써서 넣으면 됨

    path('create/', AccountCreateView.as_view(), name ='create'), # 클래스 뷰는 뒤에 as_view() 붙여줘야해
    
    # 로그인 로그아웃 간단하니까 그냥 여기서 바로 as_view 씀
    path('login/', LoginView.as_view(template_name = 'accountapp/login.html'), name='login'), 
    path('logout/', LogoutView.as_view(), name = 'logout'), # 로그아웃은 왜 템플릿 따로 지정안해줘?
    path('detail/<int:pk>', AccountDetailView.as_view(), name = 'detail'), # 몇번 유저의 디테일에 접근할건지 적어줘야해 
]