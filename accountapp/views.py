from django.shortcuts import render
from accountapp.models import HelloWorld
# Create your views here.


app_name = 'accountapp' 

def hhh(request):

    # post get 구분!
    if request.method == "POST":
        temp = request.POST.get("hhh_input")
        # 리퀘스트에서 포스트에서 hhh.input 이라는 이름을 가진 데이터를 가져와라
        # 데이터 저장
        new_hhh = HelloWorld()       # hhh라는 모델(빵틀ㅋㅋㅋ)에서 나온 새로운 객체가 저장
        new_hhh.text = temp          # 템프에 받았던 데이터를 이 새로운 객체의 text 에 넣음
        new_hhh.save()               # DB에 저장


        return render(request, 'accountapp/hhh.html', context={'hhh_output' : new_hhh }) # 객체를 내보냄
    else:
        return render(request, 'accountapp/hhh.html', context={'hhh_output' : "GET METHOD!!"})