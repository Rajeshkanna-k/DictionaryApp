from django.db import models
import os
class Word(models.Model):
    name = models.CharField(max_length=25)
    is_found = models.BooleanField()
    # created_date = models.DateField(default=None)

    def __str__(self):
        return self.name

    class Meta:
       verbose_name = 'word'

class Visitor(models.Model):
    visitors_count = models.IntegerField()
    created_date = models.DateField(null=True)

    # def __str__(self):
    #      value = self.visitors_count.__str__() + " " + self.created_date.__str__()
    #      value.split(' ', 1)
    #      return value
    
    def _getVisitorDetails(self):
         data = Visitor().objects.filter(created_date == date.today()).first()
         
         return data
    
    # def getCreatedDate(self):
    #      dtvalue = self.created_date.__str__()
    #     #  __class__
    #     #  super.getCreatedDate()
    #      return dtvalue

    class Meta:
       verbose_name = 'visitors_count'
    