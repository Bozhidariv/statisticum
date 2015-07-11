from django.template import RequestContext
from django.shortcuts import render_to_response, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, Http404
from django.db.models import Q
from django.contrib.auth.decorators import login_required
from statisticum.profiles.models import UserProfile
from statisticum.profiles.forms import UserProfileForm


@login_required()
def show(request,id, template="profiles/show.html"):
    try:
        profile = UserProfile.objects.get(id=id)
    except UserProfile.DoesNotExist:
        raise Http404

    return render_to_response(template, {'profile': profile}, context_instance=RequestContext(request))

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

