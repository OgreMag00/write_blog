from django.urls import path
from . import views

urlpatterns = [
    path('signin', views.sign_in, name='sign_in'),
    path('login', views.log_in, name='log_in'),
    path('logout', views.log_out, name='logout'),
]