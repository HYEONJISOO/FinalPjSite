from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

# request - > response
# request handler
# action

# def calculate():
#     x=1
#     y=2
#     return x
def project_play(request):
    return render(request, 'project_play.html')

def say_hello(request):

    # Pull data from db
    # Transform
    # Send email

    # x = calculate()

    return render(request, 'hello.html', {'name': ' Jisoo'})
    # render() 치면 나오는 네모 박스에 function signature 나옴. -> 뒤가 이 함수의 결과(리턴) 형식임. 
    # 이 렌더 함수는 HttpResponse로 리턴됨.