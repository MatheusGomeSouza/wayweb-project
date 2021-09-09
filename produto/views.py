from django.http import request
from django.shortcuts import render
import json
from rest_framework.decorators import api_view
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework import status
from produto.api.serialize import *
from django.views.decorators.csrf import csrf_exempt


# Create your views here.
from rest_framework.decorators import action
      
