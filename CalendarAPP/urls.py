from django.urls import path
from . import views

urlpatterns = [
    path('currentdate', views.home, name='home'),
    path('yearspassed', views.user, name='user')

]