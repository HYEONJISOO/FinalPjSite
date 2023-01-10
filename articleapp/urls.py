from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('list/', TemplateView.as_view(template_name='articleapp/list.html'), name='list'), # template 만 제공하면 나머지 다 먼들어주는 templateview! 
]