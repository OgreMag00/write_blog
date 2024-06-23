from django.urls import path
from . import views

urlpatterns = [
    path('<int:post_id>', views.index, name='post_index'),
    path('change/<int:post_id>', views.change, name='change_post'),
    path('delete/<int:post_id>', views.delete, name='delete_post'),
    path('to_draft/<int:post_id>', views.add_to_draft_list, name='to_draft_post'),


    
]
