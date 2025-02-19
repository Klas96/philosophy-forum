# importing messages
from django.contrib import messages
# import authentication related stuffs
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import User
from django.shortcuts import redirect, render

from forum.models import EventUser

from .forms import (ProfileUpdateForm, UserProfileForm, UserRegisterForm,
                    UserUpdateForm)

# Create your views here.

# Registration view


def register_view(request):
    if request.user.is_authenticated:
        return redirect('forum:home')

    if request.method == 'POST':
        reg_form = UserRegisterForm(request.POST)
        pro_form = UserProfileForm(request.POST)

        if reg_form.is_valid() and pro_form.is_valid():
            user = reg_form.save()
            pro_form = pro_form.save(commit=False)
            pro_form.user = user
            pro_form.save()

            messages.success(
                request,
                "Congrats! Your account was created successfully. Please login to continue.")
            return redirect('registration:login')
    else:
        reg_form = UserRegisterForm()
        pro_form = UserProfileForm()

    context = {
        'reg_form': reg_form,
        'pro_form': pro_form
    }

    return render(request, 'registration/register.html', context)

# Login view


def login_view(request):
    if request.user.is_authenticated:
        return redirect('forum:home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                redirect_url = request.GET.get('next', 'forum:home')
                return redirect(redirect_url)
            else:
                messages.error(request, "Oops! Username or Password is invalid. Please try again.")
        return render(request, 'registration/login.html')

# Logout view


@login_required(login_url='registration:login')
def logout_view(request):
    logout(request)
    return redirect('forum:home')

# Profile view


@login_required(login_url='registration:login')
def profileView(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, f"Your profile has been updated successfully!")
            return redirect('registration:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'registration/profile.html', context)


#def login_view(request):
#    if request.method == 'POST':
#        username = request.POST['username']
#        password = request.POST['password']
#        user = authenticate(request, username=username, password=password)
#        if user is not None:
#            login(request, user)
#            return redirect('forum:home')  # Redirect to a success page.
#        else:
#            messages.error(request, 'Invalid username or password.')
#    return render(request, 'registration/login.html')

#def logout_view(request):
#    logout(request)
#    return redirect('forum:home')
#
#def register_view(request):
#    if request.method == 'POST':
#        username = request.POST['username']
#        password = request.POST['password']
#        email = request.POST['email']
#        user = User.objects.create_user(username=username, password=password, email=email)
#        user.save()
#        login(request, user)
#        return redirect('forum:home')
#    return render(request, 'registration/register.html')

def profile_view(request):
    return render(request, 'registration/profile.html')

def connect_social_media(request):
    return render(request, 'registration/connect_social_media.html')
