from django.urls import path
from profileapp.views import ProfileCreateView, ProfileUpdateView

app_name = 'profileapp'

urlpatterns = [
    path('create/', ProfileCreateView.as_view(), name ='create'),
    path('update/<int:pk>', ProfileUpdateView.as_view(), name = 'update') # 어떤 사람의 프로파일에 접근하는지 알아야하니까 pk 넣어줌
]