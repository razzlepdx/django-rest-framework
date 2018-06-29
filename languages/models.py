from django.db import models

class Language(models.Model):
    ''' Defines objects of the Language class. '''
    
    name = models.CharField(max_length=50)
    paradigm = models.CharField(max_length=50)

