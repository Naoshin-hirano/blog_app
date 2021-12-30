from .views import index, detail, add
from django.urls import path, include

app_name = 'blog_app'
urlpatterns = [
    path('', index, name='index'),
    path('detail/<int:post_id>/', detail, name='detail'),
    path('add/', add, name='add'),
]
