import os
import re
from django.conf import settings
from django import template
from datetime import datetime
from statisticum.common.slughifi import slughifi
from statisticum.common import timezone
from django.core.urlresolvers import reverse
from django.utils.translation import ugettext

register = template.Library()

@register.filter("share_twitter")
def share_twitter(item):
    return "https://twitter.com/intent/tweet?text="+item.title+" - &url="


@register.filter("share_facebook")
def share_facebook(item):
    return "https://www.facebook.com/sharer/sharer.php?u=" 


@register.filter("share_linkedin")
def share_linkedin(item):
    return  "http://www.linkedin.com/shareArticle?mini=true&url="


@register.filter("slugify")
def slugify(text):
    return slughifi(text)


@register.filter("title")
def title(title):
    return re.sub("[\(\[].*?[\)\]]", "", title)


@register.filter("game_url")
def game_url(game):
    result = ""
    if game:
        for param in [game.title]:
            if param:
                result = result + " " + param
    return slughifi(result)

