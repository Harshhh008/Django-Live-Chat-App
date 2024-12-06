from django.db import models
from datetime import datetime
# Create your models here.
class Room(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.name
    
class Message(models.Model):
    value = models.CharField(max_length=100000000)
    date = models.DateTimeField(default=datetime.now,blank=True)
    user = models.CharField(max_length=10000000)
    room = models.CharField(max_length=10000000)
    
    def __str__(self) -> str:
        return self.value