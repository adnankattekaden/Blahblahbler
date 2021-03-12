from django.db import models
from django.contrib.auth.models import User,auth
from owner.models import Category
# Create your models here.

class CreatorDeatails(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    about_me = models.CharField(max_length=255,null=True,blank=True)
    mobile_number = models.BigIntegerField(null=True,blank=True)
    role = models.CharField(default='Podcaster',max_length=255)
    image = models.FileField(upload_to='creatorprofile/')

    @property
    def ImageURL(self):
        try:
            url = self.image.url
        except:
            url = ''
        return url
    
    def delete(self, *args, **kwargs):
        self.image.delete()
        super().delete(*args, **kwargs)

class Show(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE,null=True,blank=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    show_name = models.CharField(max_length=200,null=True,blank=True)
    description = models.CharField(max_length=200,null=True,blank=True)
    total_episodes = models.IntegerField(default=0,null=True,blank=True)
    thumbnail = models.FileField(upload_to='showthumbnail/')

    @property
    def ImageURL(self):
        try:
            url = self.thumbnail.url
        except:
            url = ''
        return url
    
    def delete(self, *args, **kwargs):
        self.thumbnail.delete()
        super().delete(*args, **kwargs)

class Contents(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    artist = models.CharField(max_length=255,null=True,blank=True)
    show = models.ForeignKey(Show, on_delete=models.CASCADE,null=True)
    episode_name = models.CharField(max_length=255,null=True,blank=True)
    description = models.CharField(max_length=2000,null=True,blank=True)
    date_of_published = models.DateField(auto_now_add=True)
    podcast = models.FileField(upload_to='podcasts/')
    thumbnail = models.FileField(upload_to='thumbnail/')


    @property
    def ImageURL(self):
        try:
            url = self.thumbnail.url
        except:
            url = ''
        return url
        

    @property
    def PodcastURL(self):
        try:
            url = self.podcast.url
        except:
            url = ''
        return url

    def delete(self, *args, **kwargs):
        self.podcast.delete()
        self.thumbnail.delete()
        super().delete(*args, **kwargs)

class Follows(models.Model):
    follower = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name='follow_follower')
    followed = models.ForeignKey(User, on_delete=models.CASCADE,null=True,blank=True,related_name='follow_followed')
    date = models.DateField(auto_now_add=True,null=True,blank=True)
    time = models.TimeField(auto_now_add=True,null=True,blank=True)
    follow_type = models.CharField(max_length=20,null=True,blank=True)
    follows = models.IntegerField(default=0,null=True)
    unfollows = models.IntegerField(default=0,null=True)
    total_followers = models.IntegerField(default=0,null=True,blank=True)