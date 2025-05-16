from django.urls import path
from . import views
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('register')),  # Redirect root to register
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('blog/', views.blog_list, name='blog-list'),  # This should match the redirect
    path('<int:pk>/', views.article_detail, name='article_detail'),
]
