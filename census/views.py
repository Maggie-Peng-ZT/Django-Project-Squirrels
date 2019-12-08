from django.shortcuts import render
from django.shortcuts import redirect
from .models import Sightings
from .forms import SightingsForm
import json
from django.db.models import Avg, Max, Min, Count, Sum

def index(request):
    return HttpResponse("It works!")

def map(request):
    content = Sightings.objects.all()
    context = {'sightings': content}
    return render(request,'census/map.html',context)

def stats(request):
    number = Sightings.objects.all().count()
    ave_la = Sightings.objects.aggregate(Avg('Latitude'))
    ave_lo = Sightings.objects.aggregate(Avg('Longitude'))
    running_probability = Sightings.objects.filter(Running=True).count()/number
    chasing_probability = Sightings.objects.filter(Chasing=True).count()/number
    context = {'num':number, 'ave_la':ave_la, 'ave_lo':ave_lo, 'running_pro':running_probability, 'chasing_pro':chasing_probability}
    return render(request, "census/stats.html", context)

def display(request):
    sightings = Sightings.objects.all()
    context = {'content': sightings}
    return render(request, "census/sightings.html", context)

def edit(request, unique_squirrel_id):
    squirrel = Sightings.objects.get(Unique_Squirrel_ID=unique_squirrel_id)
    if request.method == 'POST':
        form = SightingsForm(request.POST, instance=squirrel)
        if form.is_valid():
            form.save()
            return redirect(f'/census/sightings/{unique_squirrel_id}')
    else:
        form = SightingsForm(instance=squirrel)

    context = {
        'form': form,
    }

def add(request):
    if request.method == 'POST':
        form = SightingsForm(request.POST)
        # check data with form
        if form.is_valid():
            form.save()
            return redirect(f'/adopt/list/')
    else:
        form = SightingsForm()

    context = {
        'form': form,
        'squirrel': True,
    }
