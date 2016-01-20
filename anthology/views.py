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
    all_posts_sorted = list(reversed(sorted(decades, key=lambda d: d.id)))
    data = {"decades" : decades}
    return render_to_response(template_name, data, context_instance=RequestContext(request))