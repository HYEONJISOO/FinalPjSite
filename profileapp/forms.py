from django.forms import ModelForm

from profileapp.models import Profile

class ProfileCreationForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['image', 'nickname', 'message'] # user 필드가 하나 더 있긴한데 이건 서버에서 처리해줄거임