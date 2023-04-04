from django.db import models

# Create your models here.

class Games(models.Model):
    name_of_game=models.CharField(max_length=100,primary_key=True)
    state_of_game=models.CharField(max_length=100,default="india")
    
    def __str__(self):
        return self.name_of_game
class Player(models.Model):
    name_of_game=models.ForeignKey(Games,on_delete=models.CASCADE)
    player_name=models.CharField(max_length=100)
    age=models.IntegerField()
    
    def __str__(self):
        return self.player_name
    
    
class Location(models.Model):
    player_name=models.ForeignKey(Player,on_delete=models.CASCADE)
    city=models.CharField(max_length=100)
    state=models.CharField(max_length=100)
    
    def __str__(self):
        return self.city
