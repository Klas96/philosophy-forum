# importing messages
from django.contrib import messages
# import authentication related stuffs
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import User
from django.shortcuts import redirect, render

from forum.models import Author

from .forms import (ProfileUpdateForm, UserProfileForm, UserRegisterForm,
                    UserUpdateForm)

# Create your views here.

# Registration view


def registerView(request):
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


def loginView(request):
    # restrict login page for logged in user
    if request.user.is_authenticated:
        return redirect('forum:home')
    else:
        if request.method == 'POST':
            # get username
            username = request.POST.get('username')
            # get password
            password = request.POST.get('password')
            # check authentication
            user = authenticate(request, username=username, password=password)
            # if user exists log them in
            if user is not None:
                login(request, user)
                redirect_url = request.GET.get('next', 'forum:home')
                return redirect(redirect_url)
            else:
                # show error message
                messages.error(
                    request, f"Oops! Username or Password is invalid. Please try again.")

        return render(request, 'registration/login.html')

# Logout view


@login_required(login_url='registration:login')
def logoutView(request):
    # call logout method
    logout(request)
    return redirect('registration:login')

# Profile view


@login_required(login_url='registration:login')
def profileView(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(
            request.POST, request.FILES, instance=request.user.author)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(
                request, f"Your profile has been updated successfully!")
            return redirect('registration:profile')
    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.author)

    context = {
        'user_form': user_form,
        'profile_form': profile_form
    }
    return render(request, 'registration/profile.html', context)


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('forum:home')  # Redirect to a success page.
        else:
            messages.error(request, 'Invalid username or password.')
    return render(request, 'registration/login.html')

def logout_view(request):
    logout(request)
    return redirect('forum:home')

def register_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        user.save()
        login(request, user)
        return redirect('forum:home')
    return render(request, 'registration/register.html')