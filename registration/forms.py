from django import forms
# importing built-in user model
# importing default user registration form
from django.contrib.auth.forms import User, UserCreationForm
from django.forms import ModelForm

from forum.models import EventUser


# Creating custom User registration form utilizing the default one
class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UserProfileForm(ModelForm):
    class Meta:
        model = EventUser
        fields = ['is_member']


"""Utilizing both forms to let user's update their account's information"""
# Updating the User registration form


class UserUpdateForm(ModelForm):
    class Meta:
        model = User
        fields = ['email']
        exclude = ['user']

# Updating the profile form


class ProfileUpdateForm(ModelForm):
    class Meta:
        model = EventUser
        fields = ['profile_pic']
