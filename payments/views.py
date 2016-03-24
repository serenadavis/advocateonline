from django.shortcuts import get_object_or_404, render_to_response
from django.template.context import RequestContext
from magazine.models import Subscriber, Donation, Purchase # '.' signifies the current directory
from collections import OrderedDict
import json
import stripe
from django.conf import settings
from datetime import datetime
from pytz import timezone
from magazine import views
import logging


# logger = logging.getLogger("payments")

def donate(request):
    template_name = 'donate.html'
    return render_to_response(template_name, context_instance=RequestContext(request))

def subscribe(request):
    template_name = 'subscribe.html'
    return render_to_response(template_name, context_instance=RequestContext(request))

def shopSubmit(request):
    cost_of_issue = 10
    purchases_dict = {}
    amount = 0
    for item in request.POST:
        writeToLog(item)
        if (item.find("issues_")==0):
            if str(request.POST[item]) != "0":
                purchases_dict[item[7:]]=request.POST[item]
                amount = amount + (cost_of_issue * int(request.POST[item]))
    purchases_json=(json.dumps(purchases_dict))

    token = request.POST['stripeToken']
    customer = createCustomer(token,request.POST['name'], request.POST['email'], 'shop')
    chargeCustomer(amount*100,customer.id,'shop')

    purchase = Purchase.objects.create(
        name=request.POST['name'],
        email=request.POST['email'],
        streetAddress1=request.POST['streetAddress1'],
        streetAddress2=request.POST['streetAddress2'],
        city=request.POST['city'],
        state=request.POST['state'],
        country=request.POST['country'],
        zipCode=request.POST['zipCode'],
        customerID = customer.id,
        amount= amount,
        purchases_json = purchases_json,
        time = getEasternTimeZoneString()
    )
    template_name = 'success.html'
    return render_to_response(template_name, context_instance=RequestContext(request))

def writeToLog(text):
    file = open("logFile.txt", "a")
    file.write(text+"\n")
    file.close()
    return

def stripeSubmit(request):
    # Get the credit card details submitted by the form

    if "stripeToken" not in request.POST:
      return render_to_response("subscribe.html", context_instance=RequestContext(request))
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
            amount = 45

        stripe.api_key = settings.STRIPE_BUY_SECRET_KEY

        # create a stripe customer
        customer = stripe.Customer.create(
            card = token,
            description = subscriptionType,
            email = request.POST['email'],
            metadata = {
                'Name': request.POST['name'],
                'Address': request.POST['streetAddress1'],
                'Address Line 2': request.POST['streetAddress2'],
                'City': request.POST['city'],
                'State': request.POST['state'],
                'Zip Code': request.POST['zipCode'],
                'Country': request.POST['country'],
            }
        )

        subscriber = Subscriber.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            streetAddress1=request.POST['streetAddress1'],
            streetAddress2=request.POST['streetAddress2'],
            city=request.POST['city'],
            state=request.POST['state'],
            country=request.POST['country'],
            zipCode=request.POST['zipCode'],
            renew=int(request.POST['renew']),
            customerID = customer.id,
            subscriptionType=subscriptionType,
            time = getEasternTimeZoneString()
        )

        chargeCustomer(amount*100,customer.id,'subscribe')
        template_name = 'success.html'
        return render_to_response(template_name, context_instance=RequestContext(request))
    except stripe.CardError as problem:
      # The card has been declined
      template = "Looks like there is a problem with your payment information: {0}. Arguments:\n{1!r}"
      message = template.format(type(problem).__name__, ex.problem)
      data = {
        "message": message
      }
      return render_to_response("paymenterror.html", data, context_instance=RequestContext(request))
    except Exception as problem:
      # There is a different problem
      # logger.error(problem)
      message = "There are has been an error with our servers. You card should not have been charged. If it was please get in contact with tech@theharvardadvocate.com and we will be glad to resolve this."
      data = {
        "message": message
      }
      return render_to_response("paymenterror.html", data, context_instance=RequestContext(request))

def sendDonation(request):
    # get form details
    # logger.error("")
    if "stripeToken" not in request.POST:
      return render_to_response("donate.html", context_instance=RequestContext(request))
    token = request.POST['stripeToken']


    # Create the charge on Stripe's servers - this will charge the user's card
    try:
        page = 'donate'
        name = request.POST['name']
        email = request.POST['email']
        comment=request.POST['comment']

        # Create customer on Stripe
        stripe.api_key = settings.STRIPE_DONATE_SECRET_KEY
        customer = stripe.Customer.create(
            card = token,
            description = comment,
            email = email,
            metadata = {
                'Name': name,
                'Address': request.POST['streetAddress1'],
                'Address Line 2': request.POST['streetAddress2'],
                'City': request.POST['city'],
                'State': request.POST['state'],
                'Zip Code': request.POST['zipCode'],
                'Country': request.POST['country'],
            }
        )

        amount = int(request.POST['amount'])*100

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
            amount=int(request.POST['amount']),
            comment=request.POST['comment'],
            time = getEasternTimeZoneString()
        )
        chargeCustomer(amount,customer.id,page)
        template_name = 'success.html'
        return render_to_response(template_name, context_instance=RequestContext(request))
    except stripe.CardError as problem:
      # The card has been declined
      template = "Looks like there is a problem with your payment information: {0}. Arguments:\n{1!r}"
      message = template.format(type(problem).__name__, ex.problem)
      data = {
        "message": message
      }
      return render_to_response("paymenterror.html", data, context_instance=RequestContext(request))
    except Exception as problem:
      # There is a different problem
      # logger.error(problem)
      message = "There are has been an error with our servers. Your card should not have been charged. If it was please get in contact with tech@theharvardadvocate.com and we will be glad to resolve this."
      data = {
        "message": message
      }
      return render_to_response("paymenterror.html", data, context_instance=RequestContext(request))


def galaDonation(request):
    # get form details
    # logger.error("")
    if "stripeToken" not in request.POST:
      return render_to_response("donate.html", context_instance=RequestContext(request))
    token = request.POST['stripeToken']

    amount = 0
    try:
        subscriptionType = request.POST['ticketType']
        if subscriptionType == "0 Tickets" :
            amount += 0
        elif subscriptionType == "1 Tickets":
            amount += 150
        elif subscriptionType == "2 Tickets" :
            amount += 300
        elif subscriptionType == "3 Tickets":
            amount += 450
                elif subscriptionType == "4 Tickets" :
            amount += 600
        elif subscriptionType == "5 Tickets":
            amount += 750

    try:
        subscriptionType = request.POST['ticketAnthologyType']
        if subscriptionType == "0 Tickets" :
            amount += 0
        elif subscriptionType == "1 Tickets":
            amount += 300
        elif subscriptionType == "2 Tickets" :
            amount += 600
        elif subscriptionType == "3 Tickets":
            amount += 900
                elif subscriptionType == "4 Tickets" :
            amount += 1200
        elif subscriptionType == "5 Tickets":
            amount += 1500

    try:
        subscriptionType = request.POST['ticketAnthologyUnderwriteType']
        if subscriptionType == "0 Tickets" :
            amount += 0
        elif subscriptionType == "1 Tickets":
            amount += 500
        elif subscriptionType == "2 Tickets" :
            amount += 1000
        elif subscriptionType == "3 Tickets":
            amount += 1500
                elif subscriptionType == "4 Tickets" :
            amount += 2000
        elif subscriptionType == "5 Tickets":
            amount += 2500

    try:
        subscriptionType = request.POST['subscriptionType']
        if subscriptionType == "Three years (12 issues) - U.S." :
            amount += 90
        elif subscriptionType == "Two years (8 issues) - U.S.":
            amount += 69
        elif subscriptionType == "One year (4 issues) - U.S.":
            amount += 35
        elif subscriptionType == "Three years (12 issues) - International & Institutions":
            amount += 110
        elif subscriptionType == "Two years (8 issues) - International & Institutions":
            amount += 75
        elif subscriptionType == "One year (4 issues) - International & Institutions":
            amount += 45

    try:
        amount += int(request.POST['amount'])
    amount = amount*100

    # Create the charge on Stripe's servers - this will charge the user's card
    try:
        page = 'donate'
        name = request.POST['name']
        email = request.POST['email']
        comment=request.POST['comment']

        # Create customer on Stripe
        stripe.api_key = settings.STRIPE_DONATE_SECRET_KEY
        customer = stripe.Customer.create(
            card = token,
            description = comment,
            email = email,
            metadata = {
                'Name': name,
                'Address': request.POST['streetAddress1'],
                'Address Line 2': request.POST['streetAddress2'],
                'City': request.POST['city'],
                'State': request.POST['state'],
                'Zip Code': request.POST['zipCode'],
                'Country': request.POST['country'],
            }
        )

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
            amount=int(request.POST['amount']),
            comment=request.POST['comment'],
            time = getEasternTimeZoneString()
        )
        chargeCustomer(amount,customer.id,page)
        template_name = 'success.html'
        return render_to_response(template_name, context_instance=RequestContext(request))
    except stripe.CardError as problem:
      # The card has been declined
      template = "Looks like there is a problem with your payment information: {0}. Arguments:\n{1!r}"
      message = template.format(type(problem).__name__, ex.problem)
      data = {
        "message": message
      }
      return render_to_response("paymenterror.html", data, context_instance=RequestContext(request))
    except Exception as problem:
      # There is a different problem
      # logger.error(problem)
      message = "There are has been an error with our servers. Your card should not have been charged. If it was please get in contact with tech@theharvardadvocate.com and we will be glad to resolve this."
      data = {
        "message": message
      }
      return render_to_response("paymenterror.html", data, context_instance=RequestContext(request))



def createCustomer(token,name,email,page) :
    if page == 'donate':
        stripe.api_key = settings.STRIPE_DONATE_SECRET_KEY
    else:
        stripe.api_key = settings.STRIPE_BUY_SECRET_KEY

    customer = stripe.Customer.create(
        card = token,
        description = name,
        email = email
    )
    return customer

def chargeCustomer(amt, customerID, page):
    if page == 'donate':
        stripe.api_key = settings.STRIPE_DONATE_SECRET_KEY
    else:
        stripe.api_key = settings.STRIPE_BUY_SECRET_KEY

    stripe.Charge.create(
        amount=amt, # in cents
        currency="usd",
        customer=customerID
    )

def getEasternTimeZoneString():
    etz = timezone('US/Eastern')
    return datetime.now(etz).strftime('%m/%d/%Y %H:%M:%S')
