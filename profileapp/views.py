from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, UpdateView
from profileapp.decorators import profile_ownership_required
from profileapp.forms import ProfileCreationForm
from profileapp.models import Profile
from django.utils.decorators import method_decorator



# Create your views here.
class ProfileCreateView(CreateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:detail') # pk 추가ㅏ적으로 보내줘야해! -> 여기서 설정 못해줌.. -> get_success_url 이라는 내부 메서드 만들자!
    template_name = 'profileapp/create.html'


    # forms.py 의 class ProfileCreationForm 에서 받아온 form 에 들어있는 데이터가 
    # 이 form_valid(form) 의 폼으로 들어감.  
    # 이걸 임시로 저장 
    # ['image', 'nickname', 'message'] 데이터는 있는데 유저 데이터는 없음 
    # 셀프에서 리퀘스트 보내서 그 접속한 당사자 유저정해줌
    # 이걸 최종적으로 저장
    def form_valid(self, form):
        temp_profile = form.save(commit= False)
        temp_profile.user = self.request.user
        temp_profile.save()
        return super().form_valid(form) # 나머지는 조상이 ProfileCreateView 임. 여기에 원래있던 것의 결과를 리턴함

    def get_success_url(self) :
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk}) # self 에서 object 가 가지고 있는건 프로파일! 그 프로파일의 유저(model.py)의 pk를 찾아서 넘겨줌

# UPDATE VIEW

@method_decorator(profile_ownership_required, 'get')
@method_decorator(profile_ownership_required, 'post')

class ProfileUpdateView(UpdateView):
    model = Profile
    context_object_name = 'target_profile'
    form_class = ProfileCreationForm
    # success_url = reverse_lazy('accountapp:hhhu')
    template_name = 'profileapp/update.html'

    def get_success_url(self) :
        return reverse('accountapp:detail', kwargs={'pk':self.object.user.pk}) # self 에서 object 가 가지고 있는건 프로파일! 그 프로파일의 유저(model.py)의 pk를 찾아서 넘겨줌
