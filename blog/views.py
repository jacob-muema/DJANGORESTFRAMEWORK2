from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.decorators import login_required
from .forms import RegisterForm, CustomLoginForm
from .models import BlogPost  # Adjust the model name if different

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')  # Redirect to login after registration
    else:
        form = UserCreationForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('blog-list')  # Redirect to blog_list view after login
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

@login_required
def blog_page(request):
    return render(request, 'blog.html')

def blog_list(request):
    blogs = BlogPost.objects.all()
    return render(request, 'blog/blog_list.html', {'blogs': blogs})
