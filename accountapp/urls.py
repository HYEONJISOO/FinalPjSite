from django.urls import path
from . import views

app_name = "accountapp"

urlpatterns = [
    path('hhh/', views.hhh, name = 'hhhu')
]