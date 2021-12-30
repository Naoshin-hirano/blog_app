from .views import index
from django.urls import path, include

app_name = 'blog_app'
urlpatterns = [
    path('', index, name='index'),
]
