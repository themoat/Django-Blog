'''This is a new model in users app. We have to create this, cause this info related needs to be stored in db'''
from django.db import models
from django.contrib.auth.models import User
from PIL import Image

class Profile(models.Model):
    user = models.OneToOneField(User,on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpeg', upload_to='profile_pics') #upload_to>> gives directory we upload to

    def __str__(self):
        return (self.user.username)

    def save(self, *args, **kwargs):
        super(Profile,self).save(*args, **kwargs)
        img = Image.open(self.image.path)

        if img.height>300 or img.width>300:
            output_size = (300,300)
            img.thumbnail(output_size)
            img.save(self.image.path)
