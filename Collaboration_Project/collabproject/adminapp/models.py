from django.db import models

class Member(models.Model):
    locations = (
        ('San Jose','San Jose'),
        ('RTP','RTP'),
        ('Mexico','Mexico'),
        ('Krakow','Krakow'),
    )

    cohorts = (
        ('Spring 2018','Spring 2018'),
    )

    fName = models.CharField(max_length=25)
    lName = models.CharField(max_length=25)
    cec = models.CharField(max_length=10, primary_key=True)
    location = models.CharField(max_length=8,choices=locations)
    cohort = models.CharField(max_length=20,choices=cohorts,default=None)

    def __str__(self):
        return self.fName + ' ' + self.lName + ':' + self.cec + ' - ' +'(' + self.location + ')'

class Team(models.Model):
    tid = models.AutoField(primary_key=True)
    tname = models.CharField(max_length=50, blank=True,null=True)  # Field name made lowercase.
    cohort = models.CharField(max_length=20, blank=True, null=True)
    business_case = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.tname + ':' + self.cohort + '-' + self.business_case

class Person(models.Model):
    cec = models.CharField(unique=True, max_length=10, blank=True, primary_key=True)
    tid = models.ForeignKey(Team,on_delete=models.CASCADE)
    fname = models.CharField(max_length=25, blank=True, null=True)  # Field name made lowercase.
    lname = models.CharField(max_length=25, blank=True, null=True)  # Field name made lowercase.

    def __str__(self):
        return self.fname + ' ' + self.lname + '(' + self.cec + ')' + ':' + self.tid
