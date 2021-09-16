from django.db import models
from django.contrib.auth.models import User
# Create your models here.
class profile(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    Birthday=models . DateField(blank=True)
    Website=models.TextField(blank=True)
    City=models.CharField(max_length=20,default=' ')
    Phone=models.IntegerField()
    Age=models.IntegerField()
    Degree=models.TextField(max_length=20)
    Freelance=models.TextField(max_length=20)

    def __str__(self):
        return self.user.username

class skills(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    skill=models.TextField(max_length=20)
    level=models.IntegerField()
    def __str__(self):
        return self.user.username
class Education(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    degree=models.TextField(max_length=10)
    year=models.IntegerField()
    college=models.TextField(max_length=10)
    def __str__(self):
        return self.user.username