# importing password reset related urls
from django.contrib.auth import views as auth_views
from django.urls import path

from . import views
from django.contrib.auth import views as auth_views
from .views import register_view, login_view, logout_view, profile_view

app_name = 'registration'

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('user-profile/', profile_view, name='profile'),

    # send users to a page to reset their password
    path(
        'password-reset/',
        auth_views.PasswordResetView.as_view(),
        name='password_reset'),
    # the page shown after a user has been emailed a link to reset their
    # password
    path(
        'password-reset-request/',
        auth_views.PasswordResetDoneView.as_view(),
        name='password_reset_done'),
    # presents a form for entering a new password
    path(
        'reset-confirm/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(),
        name='password_reset_confirm'),
    # show users password successfully changed message
    path(
        'reset-done/',
        auth_views.PasswordResetCompleteView.as_view(),
        name='password_reset_complete'),

]
