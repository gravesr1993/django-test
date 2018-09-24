from django.shortcuts import render
from django.views.generic import TemplateView
from django.contrib.auth import get_user_model
from plaid import Client
from plaid.errors import APIError, ItemError
from django.views.decorators.csrf import csrf_exempt
from django.utils.encoding import smart_text
from django.http import HttpResponse,JsonResponse
import os
import datetime
import plaid
from flask import Flask
from flask import render_template
from flask import request
from flask import jsonify

app = Flask(__name__)

# Fill in your Plaid API keys - https://dashboard.plaid.com/account/keys
PLAID_CLIENT_ID = '5b9fccf1448de50011a24cd4'
PLAID_SECRET = '6a9f258d5053fd287026612838344f'
PLAID_PUBLIC_KEY = '113612795da4a87e4850681ffb3866'
PLAID_ENV='sandbox'

# Use 'sandbox' to test with Plaid's Sandbox environment (username: user_good,
# password: pass_good)
# Use `development` to test with live users and credentials and `production`
# to go live
# Create your views here.



client = plaid.Client(client_id = PLAID_CLIENT_ID, secret=PLAID_SECRET,
                  public_key=PLAID_PUBLIC_KEY, environment=PLAID_ENV)

def index(request):
   return render(request,'./plaidtest/plaid_test.html', {'plaid_public_key':PLAID_PUBLIC_KEY, 'plaid_environment':PLAID_ENV})


access_token = None
public_token = None

# @app.route("/get_access_token", methods=['POST'])
# CSRF exempt prevents callbacks going inward from triggering invalid CSRF on valid transactions specifically for sandbox environment
@csrf_exempt
def get_access_token(request):
  print(request)
  global access_token
  print("before cleaning UTF-8 conversion")
  print(request.POST.get('public_token'))
  public_token = smart_text(request.POST.get('public_token'),encoding='utf-8', strings_only=False, errors='strict')
  print("after cleaning UTF-8 conversion")
  print(public_token)
  exchange_response = client.Item.public_token.exchange(public_token)
  print ('access token: ' + exchange_response['access_token'])
  access_token=exchange_response['access_token']
  return HttpResponse(request,{'access_token':exchange_response})

def set_access_token(request):
  global access_token
  access_token = request.POST.get('access_token')
  print ('access token: ' + access_token)
  return JsonResponse({'error': False})


def accounts(request):
  global access_token
  accounts = client.Auth.get(access_token)
  print(accounts)
  return JsonResponse(accounts)

@csrf_exempt
def item(request):
  global access_token
  item_response = client.Item.get(access_token)
  institution_response = client.Institutions.get_by_id(item_response['item']['institution_id'])
  return JsonResponse({'item': item_response['item'], 'institution': institution_response['institution']})

@csrf_exempt
def transactions(request):
  global access_token
  # Pull transactions for the last 30 days
  start_date = "{:%Y-%m-%d}".format(datetime.datetime.now() + datetime.timedelta(-30))
  end_date = "{:%Y-%m-%d}".format(datetime.datetime.now())

  response = client.Transactions.get(access_token, start_date, end_date)
  return JsonResponse(response)

# @app.route("/create_public_token", methods=['GET'])
# def create_public_token():
#   global access_token
#   # Create a one-time use public_token for the Item. This public_token can be used to
#   # initialize Link in update mode for the user.
#   response = client.Item.public_token.create(access_token)
#   return jsonify(response)
