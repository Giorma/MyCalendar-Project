from django.urls import path
from . import views

urlpatterns = [
    path('currentdate', views.home, name='currentdate'),
    path('yearspassed', views.user, name='years_passed_after_user_birth')

]