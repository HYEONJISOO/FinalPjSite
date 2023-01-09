from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile') # 이 프로파일과 이 유저 객체를 하나씩 연결해준다
    # 이 프로파일의 주인이 누구인지

    image = models.ImageField(upload_to='profile/', null = True)
    # upload_to : 이미지를 받아서 서버 내에 이미지 파일 저장 : 그 이미지가 어디에 저장될것인지 경로 지정 : 29강에서 media/profile 경로가 추가되어서 거기에 이미지가 들어감
    # null = True : 이미지 꼭 없어도 된다.
    nickname = models.CharField(max_length=20, unique=True, null=True)
    # 닉네임은 유니크하게 설정하도록

    message = models.CharField(max_length=100, null=True)

    # on_delete = 이 연결되어 있는 유저 객체가 삭제될때 그와 연결되어 있는 프로파일 객제가 어떻게 되는지 지정
    # CASCADE = 이 연결된 프로파일 객체 또한 삭제됨
    # 다른 기능은 장고 문서 참고!

    # related_name : view 에서 여러가지 유저 객체를 썼었음 request.user.profile 로 해당 유저의 프로파일에 바로 연결될 수 있게 이름 지정해주는것
    # ex) request.user.profile.nickname 으로 바로 별명으로 연결해서 해당 정보 받아 올 수 있음 