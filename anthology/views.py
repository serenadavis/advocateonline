from django.shortcuts import get_object_or_404, render
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
    SUBS = 4
    sortedPaths = list(sorted(paths, key=lambda p: p.number, reverse=False))
    pathContent = {}
    for path in sortedPaths:
        allPathContent = Content.objects.all().filter(path=path)
        subContent = {}
        for sub in range(SUBS):
            content = allPathContent.filter(subsection=sub)
            if content:
                content = content[0]
            subContent[sub] = content
        pathContent[path] = subContent
    data = {"paths": pathContent, "subsections": range(SUBS)}
    return render(request, template_name, data)
