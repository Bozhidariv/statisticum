from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.db.models import Q


from statisticum.games.models import Game, GameScore
from statisticum.games.forms import GameForm, GameScoreForm , AddGameScoreFormset

def index(request,template="games/index.html"):
    
    try:
        player_id = 1 #bozhidar
        games = Game.objects.filter(Q(first_player=player_id) | Q(second_player=player_id))
    except Game.DoesNotExist:
        raise Http404

    return render_to_response(template,{'games':games},context_instance = RequestContext(request))


def add(request,template="games/add.html"):

    if request.method == 'POST':
        form = GameForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('games_index')
    else:
        form =  GameForm() 

    return render_to_response(template,{'form':form},context_instance = RequestContext(request))


def show(request,id,template="games/show.html"):
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        raise Http404

    scores = GameScore.objects.filter(game=game)
    return render_to_response(template,{'game':game, 'scores':scores},context_instance = RequestContext(request))


def edit(request,id,template="games/add.html"):
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = GameForm(request.POST,instance=game)

        if form.is_valid():
            form.save()
            return redirect('games_index')
    else:
        form =  GameForm(instance=game) 

    return render_to_response(template,{'form':form},context_instance = RequestContext(request))


def add_score(request,id,template="games/add_score.html"):
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        raise Http404

    # if this form has been submitted...
    new_score = AddGameScoreFormset (prefix='score',instance=game)
    if request.method=='POST':
        post = request.POST.copy()
        if 'add_score' in request.POST:
            post['score-TOTAL_FORMS'] = int(post.get('score-TOTAL_FORMS',0))+ 1
            new_score = AddGameScoreFormset(post,prefix='score',instance=game)
        elif 'submit' in request.POST:
            formset = AddGameScoreFormset(post,prefix='score',instance=game)
            if formset.is_valid():
                game.save()
                formset.save()

    return render_to_response(template,{'game':game,'score':new_score},context_instance = RequestContext(request))