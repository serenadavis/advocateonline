from django.shortcuts import get_object_or_404, render_to_response
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.template.context import RequestContext
from collections import OrderedDict
from itertools import chain
import json
import stripe
from django.conf import settings
import random

from .models import *

# Create your views here.

def main(request):
    template_name = 'anthology_home.html'
    decades = Decade.objects.all()
    # sort the decades by their first four chars (the lower date in their range)
    all_decades_sorted = list((sorted(decades, key=lambda d: int(d.name[:4]) )))
    decade_content = {}
    for decade in all_decades_sorted:
    	content = Content.objects.all().filter(decade = decade)
    	decade_content[decade] = content
    data = {"decades" : decade_content}
    return render_to_response(template_name, data, context_instance=RequestContext(request))
	


