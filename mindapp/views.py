from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from mindapp.models import *
import datetime
from time import timezone
import csv
from django.http import HttpResponse
from decouple import config

# Create your views here.

def saveLeaderboard(request):
    if request.GET.get("password") == config('LEADERBOARD_PASSWORD',cast=str):
        response = HttpResponse(content_type="text/csv")
        response["Content-Disposition"] = 'attachment; filename="leaderboards.csv"'
        writer = csv.writer(response)
        for player in Player.objects.order_by("-score", "timestamp"):
            writer.writerow([player.user.username, player.score])
        return response
    else:
        return HttpResponse("Not Authorised. Bad user :(")

def index(request):
    #Config for activating contest active and inactive time
    #config = Config.objects.all().first()
    if request.user:
        if request.user.is_authenticated:
            return render(request, 'index.html',{'user':request.user})
    return render(request, 'index.html')

@login_required
def answer(request):
    if request.method == 'POST':
        op_no = request.POST.get('op_no')
        player=Player.objects.get(user=request.user)
        option=option.objects.get(id=op_no)
        if option.end:
            #player is dead redirect to start node
            return render(request, 'dead.html',{'player':player})
        else:
            #option is non terminating one player progresses to next level
            player.current_sitn=option.next_sit
            player.score+=1
            player.timestamp = datetime.datetime.now()
            player.save()
            sitn=Situation.objects.get(situation_no=option.next_sit)
            return render(request , 'level.html' ,{'player':player,'sitn':sitn})
    else:
        player = Player.objects.get(user=request.user)
        sitn = Situation.objects.get(situation_no=player.current_sitn)
        return render(request,"level.html", {'player':player,'sitn':sitn})

def leaderboard(request):
    players = Player.objects.all()
    context = {'players':players}
    return render(request,"leaderboard.html",context)


