from django.db import models
from django.utils.encoding import python_2_unicode_compatible
from django.contrib.auth.models import User

import os

def get_image_path(instance, filename):
    return os.path.join('user_images', filename)

@python_2_unicode_compatible
class UserProfile(models.Model):
    user = models.CharField(max_length=200)
    profile_image = models.ImageField(upload_to=get_image_path, blank=True, null=True)

    def __str__(self):
        return self.user

class Bunk(models.Model):
    from_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bunks_from_user')
    to_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='bunks_to_user')
    time = models.DateTimeField('time bunked', auto_now_add=True)

    def __str__(self):
        return str(self.from_user) + ' bunk\'d ' + str(self.to_user) + ' at ' + str(self.time.strftime('%H:%M'))

'''
CharField (url to image on the internet)
'''
