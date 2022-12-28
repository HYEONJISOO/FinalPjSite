from django.contrib.auth.models import User
from django.http import HttpResponseForbidden
from django.shortcuts import HttpResponseRedirect, render
from django.urls import reverse, reverse_lazy
# reverse : 함수형 뷰에서 사용하는 url
# reverse_lazy : 클래스 형 뷰에서 사용하는 url
from django.views.generic import CreateView, DetailView, UpdateView, DeleteView
from django.contrib.auth.forms import UserCreationForm
# 커스터마이징 한 폼!
from accountapp.forms import AccountUpdateForm

from accountapp.models import HelloWorld

# Create your views here.


app_name = 'accountapp' 

def hhh(request):
 
    if request.user.is_authenticated:      # 유저가 로그인했는지 확인


        # post get 구분!
        if request.method == "POST":
            temp = request.POST.get("hhh_input")
            # 리퀘스트에서 포스트에서 hhh.input 이라는 이름을 가진 데이터를 가져와라
            new_hhh = HelloWorld()       # hhh라는 모델(빵틀ㅋㅋㅋ)에서 나온 새로운 객체가 저장
            new_hhh.text = temp          # 템프에 받았던 데이터를 이 새로운 객체의 text 에 넣음
            new_hhh.save()               # DB에 저장
            # 데이터 저장
            

            # return render(request, 'accountapp/hhh.html', context={'hhh_list' : hhh_list }) # 객체를 내보냄
            # 렌더로 하면 새로고침할때 계속 포스트하는 문제 발생
            return HttpResponseRedirect(reverse('accountapp:hhhu'))
        else:
            hhh_list = HelloWorld.objects.all()
            return render(request, 'accountapp/hhh.html', context={'hhh_list' : hhh_list })

    else:
        return HttpResponseRedirect(reverse('accountapp:login'))



class AccountCreateView(CreateView):

    # 함수가 정의된 곳으로 이동  : fn+f12
    # 유저 만들때 사용할 폼이 필요함 : 장고가 기본 폼 제공함

    model = User
    form_class = UserCreationForm
    # 계정 만들기 성공했을때 어느 유알엘로 연결할것인가
    success_url = reverse_lazy('accountapp:hhhu')
    # 어느 html 파일로 볼지 
    template_name = 'accountapp/create.html'

class AccountDetailView(DetailView):
    model = User
    context_object_name = "target_user"
    template_name = "accountapp/detail.html"


class AccountUpdateView(UpdateView):
    model = User
    context_object_name = "target_user"
    form_class = AccountUpdateForm
    success_url = reverse_lazy('accountapp:hhhu')
    template_name = 'accountapp/update.html'

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:    # 로그인 되어 있고, self는 해당 accountupdateview뷰를 가리킴 이 안에서 사용되고 있는 오브젝트 들 중에서도 여기서는 pk 를 가져옴. 그게 지금 리퀘스트를 보내는 유저와같은지 확인
            return super().get(*args, **kwargs)                         # 하던거 계속 해라
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):       # POST 방식일때도 똑같이!
        if self.request.user.is_authenticated and self.get_object() == self.request.user:    
            return super().get(*args, **kwargs)                         
        else:
            return HttpResponseForbidden()

class AccountDeleteView(DeleteView):
    model = User
    context_object_name = "target_user"

    success_url = "accountapp:login"
    template_name = "accountapp/delete.html"


    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated and self.get_object() == self.request.user:    # 로그인 되어 있고, self는 해당 accountupdateview뷰를 가리킴 이 안에서 사용되고 있는 오브젝트 들 중에서도 여기서는 pk 를 가져옴. 그게 지금 리퀘스트를 보내는 유저와같은지 확인
            return super().get(*args, **kwargs)                         # 하던거 계속 해라
        else:
            return HttpResponseForbidden()

    def post(self, *args, **kwargs):       # POST 방식일때도 똑같이!
        if self.request.user.is_authenticated and self.get_object() == self.request.user:    
            return super().get(*args, **kwargs)                         
        else:
            return HttpResponseForbidden()