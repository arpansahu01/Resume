from django.urls import path
from . import views

urlpatterns = [
    path('page/',views.serv,name='servpage')
]
