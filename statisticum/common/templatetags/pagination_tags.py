from django import template

register = template.Library()

def paginator(context, adjacent_pages=2):
    """
    To be used in conjunction with the object_list generic view.

    Adds pagination context variables for use in displaying first, adjacent and
    last page links in addition to those created by the object_list generic
    view.
    """
    page_numbers = [n for n in \
                    range(context["page"] - adjacent_pages, context["page"] + adjacent_pages + 1) \
                    if n > 0 and n <= context["pages"]]
    return {
        "results_per_page": context["results_per_page"],
        "page": context["page"],
        "pages": context["pages"],
        "page_numbers": page_numbers,
        "next": context["page"] + 1,
        "previous": context["page"] - 1,
        "has_next": context["page"] < context["pages"],
        "has_previous": context["pages"] > 1,
        "show_first": 1 not in page_numbers,
        "show_last": context["pages"] not in page_numbers,
        "page_url":context["page_url"]
    }

register.inclusion_tag("paginator.html", takes_context=True)(paginator)
