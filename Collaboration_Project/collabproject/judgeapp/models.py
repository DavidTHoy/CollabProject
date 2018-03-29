from django.utils import timezone
from django.conf import settings
from django.db import models
# Create your models here.

class Timeslot(models.Model):
    sTime = models.DateTimeField(default=timezone.now)
    eTime = models.DateTimeField(default=timezone.now)
    user = models.ManyToManyField(settings.AUTH_USER_MODEL, blank=True)

    def __str__(self):
        return self.sTime.strftime("%B %d, %Y %I:%M %p") +" - " +self.eTime.strftime("%I:%M %p")

