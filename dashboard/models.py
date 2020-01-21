import os
from django import forms
from django.db import models
from django.contrib.auth.models import User
from django.core.files.images import get_image_dimensions
from django.db.models.signals import post_save
from django.dispatch import receiver
from api.models import MyModelForm

def avatar_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/avatar/user_<username>.<file_extension>
    filename, file_extension = os.path.splitext(filename)
    return 'avatar/user_{0}{1}'.format(instance.user.username, file_extension)

# from: https://simpleisbetterthancomplex.com/tutorial/2016/07/22/how-to-extend-django-user-model.html#onetoone
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, blank=True)
    photo = models.ImageField(upload_to=avatar_path, blank=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

class AccountFormU(MyModelForm):
    class Meta:
        model = User
        fields = ('first_name','last_name',)

class AccountFormP(MyModelForm):
    class Meta:
        model = Profile
        exclude = ('user','photo')  # fotoğraf yükleme işini çözemedim. yarına inş...
        labels = {
            'title': 'Ünvan',
            'photo': 'Fotoğraf',
        }
