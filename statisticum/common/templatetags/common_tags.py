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

@register.filter("first_letters")
def first_letters(text,limit=2):
    letters = [word[0].upper() for word in text.split()][:limit]
    return "".join(letters)

@register.filter("pretty_date")
def pretty_date(time,short=True):
    
    if type(time) is not int and type(time)!= datetime:
        return ""
    """
    Get a datetime object or a int() Epoch timestamp and return a
    pretty string like 'an hour ago', 'Yesterday', '3 months ago',
    'just now', etc
    """
    #print timezone.now().strftime('%X %x %Z')
    time = time.replace(tzinfo=timezone.utc)
    #print time.strftime('%X %x %Z')
    now = timezone.now()

    diff = now - time
  
    second_diff = diff.seconds
    day_diff = diff.days
    if day_diff < 0:
        return ''

    if day_diff == 0:
        if second_diff < 10:
            return  "now" if short else "just now"
        if second_diff < 60:
            return str(second_diff) + "s" if short else " seconds ago"
        if second_diff < 120:
            return  "1 m" if short else "a minute ago" 
        if second_diff < 3600:
            return str( second_diff // 60 ) + " m" if short else " minutes ago"
        if second_diff < 7200:
            return "1 h" if short else " an hour ago"
        if second_diff < 86400:
            return str( second_diff // 3600 ) + " h" if short else " hours ago"
    if day_diff == 1:
        return "1 d" if short else ugettext("Yesterday")
    if day_diff < 7:
        return str(day_diff) + " " + "d" if short else ugettext("days ago")
    if day_diff < 31:
        return str(int(day_diff//7)) + " w" if short else " weeks ago"
    if day_diff < 365:
        return str(int(day_diff//30)) + " months ago"
    return str(int(day_diff//365)) + " y" if short else " years ago"