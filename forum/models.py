from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import Group

class Event(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(max_length=500)
    datetime = models.DateTimeField(null=True, blank=True)
    image = models.ImageField(upload_to='event_images/', null=True, blank=True)
    organizer_user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, related_name='organized_events')
    organizer_group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True, related_name='organized_events')

class EventUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    profile_pic = models.ImageField(
        default="pro_pic.png", null=True, blank=True)
    is_member = models.BooleanField(default=False)
    phone_number = models.TextField(max_length=500, null=True, blank=True)
    email = models.EmailField(max_length=254, null=True, blank=True)
    urls = models.TextField(max_length=500, null=True, blank=True)
    def __str__(self):
        return self.user.username


class UserPost(models.Model):
    author = models.ForeignKey(EventUser, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=200, null=True)
    description = models.TextField(max_length=500, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('topic-detail', kwargs={
            'pk': self.pk
        })

    # Use this method as a property
    @property
    def answer_count(self):
        return Answer.objects.filter(user_post=self).count()

    # Use this method as a property
    @property
    def topic_view_count(self):
        return TopicView.objects.filter(user_post=self).count()


class Answer(models.Model):
    user_post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField(max_length=500)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
    upvotes = models.ManyToManyField(User, blank=True, related_name='upvotes')
    downvotes = models.ManyToManyField(
        User, blank=True, related_name='downvotes')

    def __str__(self):
        return self.user_post.title

    @property
    def upvotes_count(self):
        return Answer.objects.filter(user=self).count()


class BlogPost(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=200, unique=True, null=True, blank=True)
    content = models.TextField(blank=True, null=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    thumbnail = models.ImageField(default="header.jpg", null=True, blank=True)

    def __str__(self):
        return self.title


class TopicView(models.Model):
    user_post = models.ForeignKey(UserPost, on_delete=models.CASCADE)
    user = models.ForeignKey(EventUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.user_post.title


class EventGroup(Group):
    events = models.ManyToManyField(Event, blank=True)
    description = models.TextField(max_length=500)
    members = models.ManyToManyField(User, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
