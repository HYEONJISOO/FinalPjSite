from django.urls import path # ,URLPattern
from . import views           # from current folder

#URLconf iguration : url구성 : 모든 앱은 각자의 url configuration을 가지고있음. 그걸  프로젝트의 메인 urls.py에 임포트 해줘야해
urlpatterns = [
    path('hello/', views.say_hello),    # 원래는 playground/hello 인데 playground.urls 로 가라고 메인 urls.py 에서 지정해줬으니까 더이상 playground/ 는 쓸필요 없음! 제거, 
    path('project_play/', views.project_play)
]

# 항상 / 으로 끝나야해
