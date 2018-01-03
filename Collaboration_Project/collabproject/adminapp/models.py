from django.db import models


# Create your models here.

class Member(models.Model):
    locations = (
        ('RTP','RTP'),
        ('Mexico','Mexico'),
        ('Krakow','Krakow'),
    )
    fName = models.CharField(max_length=25)
    lName = models.CharField(max_length=25)
    cec = models.CharField(max_length=10, primary_key=True)
    location = models.CharField(max_length=6,choices=locations)

    def __str__(self):
        return self.fName + ' ' + self.lName + ' - ' + self.cec + '(' +self.location + ')'
