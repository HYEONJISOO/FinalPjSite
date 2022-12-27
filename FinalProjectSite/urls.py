"""FinalProjectSite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')

# 다른 url 구성을 포함하려면 다음스텝따라해라!
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include   # 인클루드 임포트 해주고
import debug_toolbar
urlpatterns = [
    path('', include('single_pages.urls')),
    path('admin/', admin.site.urls),
    path('playground/', include('playground.urls')),   # playground/ 로 끝나는 모든 url 들은 playground.urls 에서 관리함!
    path('__debug__/', include('debug_toolbar.urls')),
    path('accounts/', include('accountapp.urls')),

]
