from django.urls import path

from . import views

app_name = 'forum'  # This sets the namespace

urlpatterns = [
    path('', views.index, name='home'),
    path('user-post/', views.userPost, name='user-post'),
    path('topic/<int:pk>/', views.postTopic, name='topic-detail'),
    #path('search-result/', views.searchView, name='search-result'),
    path('user-dashboard/', views.userDashboard, name='user-dashboard'),
    path('blog/', views.blogListView, name='blog'),
    path('article/<slug:slug>/', views.blogDetailView, name='article-detail'),
    path('event/<int:id>/', views.event_detail, name='event-detail'),
    path('add-event/', views.add_event, name='add-event'),
    path('groups/', views.groups, name='groups'),
    path('group/<int:group_id>/', views.group_profile, name='group-profile'),
]
