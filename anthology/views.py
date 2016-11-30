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
    template_name = 'anthology_base.html'
    paths = Path.objects.all()
    # sort the decades by their first four chars (the lower date in their range)
    sortedPaths = list(sorted(paths, key=lambda p: p.number))
    pathContent = {}
    for path in sortedPaths:
    	content = Content.objects.all().filter(path = path)
    	pathContent[path] = content
    data = {"paths" : pathContent, "subsections": range(4)}
    return render_to_response(template_name, data, context_instance=RequestContext(request))
	


