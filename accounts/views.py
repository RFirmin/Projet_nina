from django.shortcuts import render, redirect

# from django.contrib.auth.forms import UserCreationForm
from .forms import UserForm

# Create your views here.

def home(request):
    return render(request, 'home.html')

def register(request):

    if request.user.is_authenticated:
        return redirect('home')
    
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')    
    else:
        form = UserForm()
        
    context = {
        'form': form,
    }
        
    return render(request, 'register.html', context)