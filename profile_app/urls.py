from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='profile_index'),    
    path('new_post/', views.new_post, name='new_post_page'),
    path('draft_list/', views.draft_list, name='draft_list_page'),
]