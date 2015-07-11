from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from statisticum.games.models import Game
from statisticum.profiles.models import UserProfile
from statisticum.profiles.forms import UserProfileForm


@login_required()
def show(request,id, template="profiles/show.html"):
    try:
        profile = UserProfile.objects.get(id=id)
    except UserProfile.DoesNotExist:
        raise Http404

    player = profile.user  
    wins = Game.objects.wins(player).count()
    losts =  Game.objects.losts(player).count()
    draws = Game.objects.draws(player).count()
    accuracy = wins / (wins + losts + draws) * 100

    return render_to_response(template, 
        {'profile': profile,'wins':wins , 'losts':losts,'draws':draws , 'accuracy':accuracy},
         context_instance=RequestContext(request))

@login_required()
def edit(request, template="profiles/edit.html"):
    try:
        profile = UserProfile.objects.get(user=request.user)
    except UserProfile.DoesNotExist:
        profile = None

    if request.method == 'POST':
        form = UserProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()
            return redirect('games_index')
    else:
        form = UserProfileForm(instance=profile)

    return render_to_response(template, {'form': form}, context_instance=RequestContext(request))

