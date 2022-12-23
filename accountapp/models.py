from django.db import models

# Create your models here.


# models 의 Models 가져옴
# 거기서 추가적인 정보입력 해서 그걸 클래스로 만듦
class HelloWorld(models.Model):
    text = models.CharField(max_length=255, null = False)