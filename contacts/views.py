from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, render_to_response

# Create your views here.
def index(request):
	return render_to_response('contacts/index.html')

def details(request):
	return render_to_response('contacts/details.html')