from django.urls import path
from .views import signup, detail, edit
from django.contrib.auth import views as auth_views

app_name = 'user_app'
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='user_app/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('user/<int:user_id>/', detail, name='detail'),
    path('user/edit/<int:user_id>/', edit, name='edit'),
]
