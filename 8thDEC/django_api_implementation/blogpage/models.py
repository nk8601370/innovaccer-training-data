from django.db import models
 # Create your models here. #you have to run the two migration command to make sure the database gets created 
 
class players(models.Model): 
     fname = models.CharField(max_length=50) 
     lname = models.CharField(max_length=50) 
     playerType = models.CharField(max_length=50) 
     jerseyNumber = models.IntegerField() 
     
     def __str__(self): 
         return self.fname 