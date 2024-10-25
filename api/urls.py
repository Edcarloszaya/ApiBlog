# urls.py

from django.urls import path
from .views import list_or_create_post,retrieve_update_destroy_post

# urls da api pra fazer o crud
urlpatterns = [
    path('posts/', list_or_create_post, name='list_or_create_post'),
    path('posts/<int:id>',retrieve_update_destroy_post, name='retrieve_update_destroy_post'), 
    
]
