# UserCreationForm 상속받아서 커스터마이징
from django.contrib.auth.forms import UserCreationForm

class AccountUpdateForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['username'].disabled = True
        # user name 의 칸을 건드릴수 없게 비활성화 커스터마이징 : disabled = True 인 이상 서버에 반영 안됨