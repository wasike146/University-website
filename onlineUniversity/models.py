
from django.db import models
from django.contrib.auth.models import AbstractUser
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.urls import reverse
# Create your models here.


class CustomUser(AbstractUser):
    user_type_choices=((1,"Admin"),(2,"Staff"),(3,"Student"))
    user_type=models.CharField(max_length=255,choices=user_type_choices,default=1)


class AdminUser(models.Model):
    profile_pic=models.FileField(default="")
    auth_user_id=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

class StaffUser(models.Model):
    profile_pic=models.FileField(default="")
    auth_user_id=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    created_at=models.DateTimeField(auto_now_add=True)

class StudentUser(models.Model):
    auth_user_id=models.OneToOneField(CustomUser,on_delete=models.CASCADE)
    profile_pic=models.FileField(default="")
    created_at=models.DateTimeField(auto_now_add=True)

class Admin(models.Model):
    username=models.CharField(max_length=200,null=True,blank=True)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

COURSES_CHOICES = (
    ("free", "free"),
    ("paid", "paid"),
)
class Course(models.Model):
    title = models.CharField(max_length=200, null=True, blank=True)
    thumbnail = models.ImageField(max_length=200, null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    video_url= models.URLField(max_length=200, null=True, blank=True)
    course_type=models.CharField(max_length=20,choices=COURSES_CHOICES,default="free")
    def __str__(self):
        return self.title


@receiver(post_save,sender=CustomUser)
def create_user_profile(sender,instance,created,**kwargs):
    if created:
        if instance.user_type==1:
            AdminUser.objects.create(auth_user_id=instance)
        if instance.user_type==2:
            StaffUser.objects.create(auth_user_id=instance)
        if instance.user_type==4:
            StudentUser.objects.create(auth_user_id=instance)            

@receiver(post_save,sender=CustomUser)
def save_user_profile(sender,instance,**kwargs):
    if instance.user_type==1:
        instance.adminuser.save()
    if instance.user_type==2:
        instance.staffuser.save()
    if instance.user_type==3:
        instance.Studentuser.save()
    

