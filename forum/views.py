# importing messages
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Count, Q
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import get_object_or_404, redirect, render

from .forms import AnswerForm, UserPostForm, EventForm
from .models import *
from django.contrib.auth.models import Group


# Create your views here.
def index(request):
    events = Event.objects.all()

    context = {
        'events': events,
    }

    return render(request, 'index.html', context)


def home(request):
    user_posts = UserPost.objects.all()

    # Display latest posts.
    latest_blogs = BlogPost.objects.order_by('-timestamp')[0:3]

    latest_topics = UserPost.objects.order_by('-date_created')[0:3]

    context = {
        'user_posts': user_posts,
        'latest_blogs': latest_blogs,
        'latest_topics': latest_topics
    }
    return render(request, 'forum-main.html', context)


@login_required(login_url='login')
def userPost(request):
    # User Post form.
    form = UserPostForm(request.POST or None)

    if request.method == 'POST':
        if form.is_valid():
            title = request.POST.get('title')
            description = request.POST.get('description')
            topic = UserPost.objects.create(
                title=title,
                author=request.user.author,
                description=description)
            topic.save()
            return redirect('home')
    else:
        form = UserPostForm()

    context = {'form': form}
    return render(request, 'user-post.html', context)


@login_required(login_url='login')
def postTopic(request, pk):
    # Get specific user post by id.
    post_topic = get_object_or_404(UserPost, pk=pk)

    # Count Post View only for authenticated users
    if request.user.is_authenticated:
        TopicView.objects.get_or_create(
            user=request.user, user_post=post_topic)

    # Get all answers of a specific post.
    answers = Answer.objects.filter(user_post=post_topic)

    # Answer form.
    answer_form = AnswerForm(request.POST or None)
    if request.method == "POST":
        if answer_form.is_valid():
            content = request.POST.get('content')
            # passing User Id & User Post Id to DB
            ans = Answer.objects.create(
                user_post=post_topic,
                user=request.user,
                content=content)
            ans.save()
            return HttpResponseRedirect(post_topic.get_absolute_url())
    else:
        answer_form = AnswerForm()

    context = {
        'topic': post_topic,
        'answers': answers,
        'answer_form': answer_form,

    }
    return render(request, 'topic-detail.html', context)


@login_required(login_url='login')
def userDashboard(request):
    topic_posted = request.user.author.userpost_set.all()
    ans_posted = request.user.answer_set.all()
    topic_count = topic_posted.count()
    ans_count = ans_posted.count()

    context = {
        'topic_posted': topic_posted,
        'ans_posted': ans_posted,
        'topic_count': topic_count,
        'ans_count': ans_count
    }
    return render(request, 'user-dashboard.html', context)

"""
def searchView(request):
    queryset = UserPost.objects.all()
    search_query = request.GET.get('q')

    if search_query:
        queryset = queryset.filter(Q(title__icontains=search_query) | Q(
            description__icontains=search_query)).distinct()

        q_count = queryset.count()
    else:
        messages.error(
            request,
            f"Oops! Looks like you didn't put any keyword. Please try again.")
        return redirect('home')

    context = {
        'queryset': queryset,
        'search_query': search_query,
        'q_count': q_count
    }

    return render(request, 'search-result.html', context)
"""


def blogListView(request):

    # Display all blog posts.
    all_posts = BlogPost.objects.all()

    context = {
        'all_posts': all_posts
    }
    return render(request, 'blog-listing.html', context)


# Blog single post detail view.
def blogDetailView(request, slug):
    # Get specific post by slug.
    post_detail = get_object_or_404(BlogPost, slug=slug)

    context = {
        'post_detail': post_detail,
    }

    return render(request, 'blog-detail.html', context)

def event_detail(request, id):
    event = get_object_or_404(Event, id=id)
    return render(request, 'event_detail.html', {'event': event})

@login_required(login_url='login')
def add_event(request):
    if request.method == 'POST':
        form = EventForm(request.POST, request.FILES)
        if form.is_valid():
            event = form.save(commit=False)
            event.organizer = request.user
            event.save()
            return redirect('forum:event-detail', id=event.id)  # Redirect to the event detail page
        else:
            # Debugging: Print form errors to console
            print(form.errors)
            messages.error(request, "There was an error with your submission. Please check the form and try again.")
    else:
        form = EventForm()
    return render(request, 'forum/add_event.html', {'form': form})


def groups(request):
    all_groups = Group.objects.all()
    context = {
        'all_groups': all_groups
    }
    return render(request, 'forum/forum-groups.html', context)


def group_profile(request, group_id):
    group = get_object_or_404(EventGroup, id=group_id)
    group_events = group.events.all()
    group_description = group.description
    group_name = group.name
    
    # Assuming there is a User model with a ManyToMany relationship to Group
    group_members = User.objects.filter(groups=group)
    
    context = {
        'group': group,
        'group_members': group_members,
        'group_events': group_events,
        'group_description': group_description,
        'group_name': group_name
    }

    return render(request, 'forum/group-profile.html', context)