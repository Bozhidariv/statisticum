from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from statisticum.profiles.models import Profile
from statisticum.games.models import Game
from statisticum.profiles.forms import ProfileForm

def index(request, template="games/index.html"):
    if not request.user.is_authenticated():
        template = 'landing.html'
        return render_to_response(template, context_instance=RequestContext(request))

    try:
        player_id = request.user  
        first_win = 1
        first_lose = 2

        games = Game.objects.filter(Q(first_player=player_id) | Q(second_player=player_id))
    except Game.DoesNotExist:
        raise Http404
    return render_to_response(template, {'games': games}, context_instance=RequestContext(request))

@login_required()
def add(request, template="profile/profile.html"):

    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('games_index')
    else:
        form = ProfileForm()

    return render_to_response(template, {'form': form}, context_instance=RequestContext(request))

#@login_required()
#def show(request, id, template="games/show.html"):
#    try:
 #       game = Game.objects.get(id=id)
  #  except Game.DoesNotExist:
   #     raise Http404
#
 #   scores = GameScore.objects.filter(game=game)
  #  return render_to_response(template, {'game': game, 'scores': scores}, context_instance=RequestContext(request))

@login_required()
def edit(request, id, template="profile/profile.html"):
    try:
        form = Profile.objects.get(id=id)
    except Profile.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=game)

        if form.is_valid():
            form.save()
            return redirect('games_index')
    else:
        form = ProfileForm(instance=game)

    return render_to_response(template, {'form': form}, context_instance=RequestContext(request))

