from django.shortcuts import render

# Create your views here.


app_name = 'accountapp' 

def hhh(request):
    return render(request, 'accountapp/hhh.html')