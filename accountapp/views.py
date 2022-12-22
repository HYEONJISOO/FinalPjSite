from django.shortcuts import render

# Create your views here.


app_name = 'accountapp' 

def hhh(request):
    return render(request, 'base_fromfolder.html')