from django.db import models
from django.db import models
from django.db.models import Q
from django.utils.text import slugify
from django.utils.encoding import smart_unicode, smart_str
from tinymce import models as tinymce_models
from bs4 import BeautifulSoup
import re

import os
import datetime

# Create your models here.

class Decade(models.Model):
	name = models.CharField(max_length=255)