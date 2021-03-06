from django.template import RequestContext
from django.shortcuts import render_to_response


def index(request, template="index.html"):
    return render_to_response(template, {},
                              context_instance=RequestContext(request))
