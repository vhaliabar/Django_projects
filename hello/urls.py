from django.urls import path
from . import views
#from django.views.generic import TemplateView

app_name='hello'
urlpatterns = [
#    path('', TemplateView.as_view(template_name='hello/main.html')),
#    path('', views.ClassyView.as_view(), name='classy'),
    path('cookie', views.cookie),
    path('sessfun', views.sessfun),
    path('', views.hello),
    path('', views.sessfun),
#    path('', views.fun),
]