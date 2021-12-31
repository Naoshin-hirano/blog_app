from .views import index, detail, add, edit, delete
from django.urls import path, include

app_name = 'blog_app'
urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:post_id>/', detail, name='detail'),
    path('add/', add, name='add'),
    path('edit/<int:post_id>/', edit, name='edit'),
    path('delete/<int:post_id>/', delete, name='delete'),
]
