from django import template

def typeaheadJsView(request, typeahead_authors, typeahead_titles):
    jsContext = {'typeahead_authors' : typeahead_authors, 'typeahead_titles' : typeahead_titles}
    return jsContext

register = template.Library()
register.inclusion_tag('jsTypeahead.js', takes_context=True)(typeaheadJsView)
