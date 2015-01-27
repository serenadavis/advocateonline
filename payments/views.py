from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from .models import Subscriber, Donation # '.' signifies the current directory
from collections import OrderedDict
import json
import stripe
from django.conf import settings
from datetime import datetime
from pytz import timezone    
from magazine import views

def shopSubmit(request):
	#dataDictionary = request.POST
	return json.dumps(request)


def stripeSubmit(request):
	# Get the credit card details submitted by the form
	token = request.POST['stripeToken']
	# Create the charge on Stripe's servers - this will charge the user's card
	try:
		amount = 0
		subscriptionType = request.POST['subscriptionType']
		if subscriptionType == "Three years (12 issues) - U.S." :
			amount = 90
	 	elif subscriptionType == "Two years (8 issues) - U.S.":
	 		amount = 69
	 	elif subscriptionType == "One year (4 issues) - U.S.":
	 		amount = 35
		elif subscriptionType == "Three years (12 issues) - International & Institutions":
			amount = 110
		elif subscriptionType == "Two years (8 issues) - International & Institutions":
			amount = 75
		elif subscriptionType == "One year (4 issues) - International & Institutions":
			amount = 35

		customer = createCustomer(token,request.POST['name'])
		chargeCustomer(amount*100,customer.id)


		subscriber = Subscriber.objects.create(
			name=request.POST['name'], 
			email=request.POST['email'],
			streetAddress1=request.POST['streetAddress1'],
			streetAddress2=request.POST['streetAddress2'],
			city=request.POST['city'],
			state=request.POST['state'],
			country=request.POST['country'],
			zipCode=request.POST['zipCode'],
			renew=request.POST['renew'],
			customerID = customer.id,
			subscriptionType=subscriptionType,
			time = getEasternTimeZoneString()
		)

		return views.subscribe(request)
	except stripe.CardError, e:
	  # The card has been declined
	  pass
def sendDonation(request):
	# Get the credit card details submitted by the form
	token = request.POST['stripeToken']
	# Create the charge on Stripe's servers - this will charge the user's card
	try:

		customer = createCustomer(token,request.POST['name'])
		amount = int(request.POST['amount'])*100

		chargeCustomer(amount,customer.id)

		donation = Donation.objects.create(
			name=request.POST['name'], 
			email=request.POST['email'],
			streetAddress1=request.POST['streetAddress1'],
			streetAddress2=request.POST['streetAddress2'],
			city=request.POST['city'],
			state=request.POST['state'],
			country=request.POST['country'],
			zipCode=request.POST['zipCode'],
			customerID = customer.id,
			amount=int(request.POST['amount'])*100,
			time = getEasternTimeZoneString()
		)

		return views.subscribe(request)
	except stripe.CardError, e:
	  	# The card has been declined
	  	pass


def createCustomer(token,name) :
	stripe.api_key = settings.STRIPE_SECRET_KEY	
	customer = stripe.Customer.create(
    	card=token,
    	description=name
	)
	return customer

def chargeCustomer(amt, customerID):
	stripe.api_key = settings.STRIPE_SECRET_KEY	
	stripe.Charge.create(
		amount=amt, # in cents
		currency="usd",
		customer=customerID
	)



def getEasternTimeZoneString():
	etz = timezone('US/Eastern')
	return datetime.now(etz).strftime('%m/%d/%Y %H:%M:%S')
