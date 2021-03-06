from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from statisticum.games.models import Game, GameScore
from statisticum.games.forms import GameForm
from statisticum.games.forms import AddGameScoreFormset
from statisticum.games.forms import GameScoreForm
from statisticum.games.forms import GameApproveForm


def index(request, template="games/index.html"):
    if not request.user.is_authenticated():
        template = 'landing.html'
        return render_to_response(template,
                                  context_instance=RequestContext(request))

    try:
        player_id = request.user

        games = Game.objects.filter(
            (Q(first_player=player_id) | Q(second_player=player_id)) &
            Q(approver_status=Game.APPROVED))
    except Game.DoesNotExist:
        raise Http404
    return render_to_response(template, {'games': games},
                              context_instance=RequestContext(request))


@login_required()
def add(request, template="games/add.html"):

    if request.method == 'POST':
        form = GameForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('games_index')
    else:
        form = GameForm()

    return render_to_response(template, {'form': form},
                              context_instance=RequestContext(request))


@login_required()
def for_approval(request, template="games/for_approval.html"):

    try:
        player = request.user
        games = Game.objects.games_to_approve(player)
    except Game.DoesNotExist:
        raise Http404
    return render_to_response(template, {'games': games},
                              context_instance=RequestContext(request))


@login_required()
def for_approval(request, template="games/for_approval.html"):

    try:
        player = request.user
        games = Game.objects.games_to_approve(player)
    except Game.DoesNotExist:
        raise Http404
    return render_to_response(template, {'games': games},
                              context_instance=RequestContext(request))


@login_required()
def rejected(request, template="games/rejected.html"):

    try:
        player = request.user
        games = Game.objects.rejected(player)
    except Game.DoesNotExist:
        raise Http404
    return render_to_response(template, {'games': games},
                              context_instance=RequestContext(request))


@login_required()
def show(request, id, template="games/show.html"):
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        raise Http404

    scores = GameScore.objects.filter(game=game)
    return render_to_response(template, {'game': game, 'scores': scores},
                              context_instance=RequestContext(request))


@login_required()
def edit(request, id, template="games/add.html"):
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        raise Http404

    if request.method == 'POST':
        form = GameForm(request.POST, instance=game)

        if form.is_valid():
            form.save()
            return redirect('games_index')
    else:
        form = GameForm(instance=game)

    return render_to_response(template, {'form': form},
                              context_instance=RequestContext(request))


@login_required()
def edit_approval(request, id, template="games/edit_approval.html"):
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        raise Http404

    form = GameApproveForm(request.POST, instance=game)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('games_index')
    scores = GameScore.objects.filter(game=game)
    return render_to_response(template, {'game': game, 'scores': scores,
                                         'form': form},
                              context_instance=RequestContext(request))


@login_required()
def show_rejected(request, id, template="games/show_rejected.html"):
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        raise Http404

    scores = GameScore.objects.filter(game=game)
    return render_to_response(template, {'game': game, 'scores': scores},
                              context_instance=RequestContext(request))


@login_required()
def wins(request, template="games/wins.html"):
    try:
        player = request.user

        games = Game.objects.wins(player)
    except Game.DoesNotExist:
        raise Http404

    return render_to_response(template, {'games': games},
                              context_instance=RequestContext(request))


@login_required()
def losts(request, template="games/losts.html"):
    try:
        player = request.user
        games = Game.objects.losts(player)
    except Game.DoesNotExist:
        raise Http404
    return render_to_response(template, {'games': games},
                              context_instance=RequestContext(request))


@login_required()
def draws(request, template="games/draws.html"):
    try:
        player = request.user
        games = Game.objects.draws(player)
    except Game.DoesNotExist:
        raise Http404

    return render_to_response(template, {'games': games},
                              context_instance=RequestContext(request))


@login_required()
def add_score(request, id, template="games/add_score.html"):
    try:
        game = Game.objects.get(id=id)
    except Game.DoesNotExist:
        raise Http404

    # if this form has been submitted...
    new_score = AddGameScoreFormset(prefix='score', instance=game)
    if request.method == 'POST':
        post = request.POST.copy()
        if 'add_score' in request.POST:
            post[
                'score-TOTAL_FORMS'] = int(post.get(
                    'score-TOTAL_FORMS', 0)) + 1
            new_score = AddGameScoreFormset(
                post, prefix='score', instance=game)
        elif 'submit' in request.POST:
            formset = AddGameScoreFormset(post, prefix='score', instance=game)
            if formset.is_valid():
                game.save()
                formset.save()

    return render_to_response(template, {'game': game, 'score': new_score},
                              context_instance=RequestContext(request))
