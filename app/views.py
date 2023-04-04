from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.

from app.models import *


def insert_games(request):
    gn=input("enter the game name :")
    sg=input("enter the state of game :")
    GO=Games.objects.get_or_create(name_of_game=gn,state_of_game=sg)[0]
    GO.save()
    
    return HttpResponse("game name insert successfully")
    
def insert_player(request):
    gn=input("enter the game name :")
    GO=Games.objects.get_or_create(name_of_game=gn)[0]
    GO.save()
    
    pn=input("enter the player name :")
    age=input("enter the age :")
    
    PO=Player.objects.get_or_create(name_of_game=GO,player_name=pn,age=age)[0]
    PO.save()
    
    return HttpResponse("insert player successfully")
    
def insert_location(request):
     gn=input("enter the game name :")
     pn=input("enter the player name :")
     age=input("enter the age :")
     ci=input("enter the city ;")
     st=input("enter the state ;")
     GO=Games.objects.get_or_create(name_of_game=gn)[0]
     GO.save()
     PO=Player.objects.get_or_create(name_of_game=GO,player_name=pn,age=age)[0]
     PO.save()
     LO=Location.objects.get_or_create(player_name=PO,city=ci,state=st)[0]
     LO.save()
     
     return HttpResponse("location insert succesfully")
     
     
     
    
    
    


