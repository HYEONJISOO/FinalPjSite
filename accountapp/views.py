from django.shortcuts import render

# Create your views here.


app_name = 'accountapp' 

def hhh(request):

    # post get 구분!
    if request.method == "POST":
        return render(request, 'accountapp/hhh.html', context={'text' : "POST METHOD!!"})
    else:
        return render(request, 'accountapp/hhh.html', context={'text' : "GET METHOD!!"})