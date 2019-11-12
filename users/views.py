from django.shortcuts import render, HttpResponse, HttpResponseRedirect, reverse, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
User = get_user_model()
from .choices import gender,country,status
from django.views.generic.edit import UpdateView
from .forms import UserCreationForm, UserChangeForm, UserForm
from django.db import transaction

#from .forms import UserForm, ProfileForm
from django.contrib.auth.decorators import login_required

@transaction.atomic

# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(email=email, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            request.session['member_id'] = user.id
            return redirect('index')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'users/login.html')

def register(request):
    pass

def profile(request, users_id):
    user = User.objects.get(id=users_id)
    context = {
        'user': user,
        'gender':gender,
        'country':country,
        'status': status
    }
    return render(request, 'users/profile.html', context)

def members(request):
    user = User.objects.all()
    # Find User on first name
    if 'full_name' in request.GET:
        full_name = request.GET['full_name']
        if full_name:
            user = user.filter(full_name__icontains=full_name)

    # Find Users by email id
    if 'email' in request.GET:
        email = request.GET['email']
        if email:
            user = user.filter(email=email)

    # Find Users by status
    if 'is_active' in request.GET:
        is_active = request.GET['is_active']
        if is_active:
            user = user.filter(is_active=is_active)

    context = {
        'user': user
    }
    return render(request, 'users/members.html', context)

def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect('index')


def update_profile(request, user_id):
    if request.method == 'POST':
        user_form = User.objects.get(id=user_id)
        user_form = UserForm(request.POST, instance=request.user)
        if user_form.is_valid():
            user_form.save()
            return redirect('users/profile.html')
    else:
        user_form = UserForm(instance=request.user)

    return render(request, 'users/profile_update.html', { 'user_form': user_form })