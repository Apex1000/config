import io
import json
import random
import re
import pandas as pd
from django_countries import countries
from django.db.models import Q
from django_countries.fields import Country
from phonenumbers.phonenumberutil import region_code_for_number
from phonenumbers.phonenumberutil import region_code_for_country_code
import phonenumbers
from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from rest_framework.generics import (
    ListAPIView,
    RetrieveAPIView,
    CreateAPIView,
    UpdateAPIView,
    DestroyAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView,
    ListCreateAPIView,
)
from itertools import islice
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
# from core.permissions import IsOwner
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date, datetime, timedelta
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from leads import models as lead_models
from leads import serializers as lead_serializers
from panel_user import models as panel_models
from core import models as core_models
from store import models as store_models

from haversine import haversine, Unit
from geopy.geocoders import Nominatim

now = date.today()
# current_time = datetime.datetime.utcnow().strftime("%H:%M:%S")
# today = datetime.date.today()

# class CityUploader(APIView):
#     # permission_classes = (IsAuthenticated,)

#     def post(self, request):
#         csv_file = request.FILES["file"]
#         csv = pd.read_csv(csv_file)
#         city = csv["city"]
#         state = csv["state"]
#         country_obj = core_models.Country.objects.get_or_create(name="India",mobile_code = "+91")[0]
#         objs = (
#             core_models.Cities(
#                 state=core_models.State.objects.get_or_create(country = country_obj,name=state[row])[0],
#                 name=city[row],
#                 display_name=city[row] + ", " + state[row],
#             )
#             for row in range(700)
#         )

#         batch_size = 100
#         while True:
#             batch = list(islice(objs, batch_size))
#             if not batch:
#                 break
#             try:
#                 core_models.Cities.objects.bulk_create(batch, batch_size)
#             except Exception as e:
#                 print(e)

#         s = {"status": True}
#         return Response(s, status=status.HTTP_200_OK)

# class CustomUploader(APIView):
#     # permission_classes = (IsAuthenticated,)
#     def post(self, request):
#         try:
#             csv_file = request.FILES["file"]
#         except:
#             return Response(
#                 {"error": "Attach File to your request"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         reader = pd.read_csv(csv_file, encoding="latin-1")
#         reader = reader.dropna()
#         phone_numbers = reader["Telephone"]
#         full_name = reader["Name"]
#         city = reader["Location"]

        

#         source = lead_models.LeadSource.objects.get_or_create(source="Demo")[0]
#         prospect_callstatus = lead_models.LeadStatus.objects.get_or_create(status="Prospact")[0]
        
#         for row in range(len(phone_numbers)):
#             contactobj = lead_models.Contact.objects.filter(mobile = str(phone_numbers[row]))
            
#             if contactobj:
#                 continue
#             else:
#                 contactnewobj = lead_models.Contact.objects.create(mobile = str(phone_numbers[row]))

#             city_obj = core_models.Cities.objects.filter(name__icontains= city[row])
#             lead_models.Lead.objects.create(
#                 lead = contactnewobj,
#                 primary_name = full_name[row],
#                 lead_source = source,
#                 panel_user = panel_models.Profile.objects.get(id = 1),
#                 city =  city_obj.first() if city_obj else None,
#                 followup_date = date.today(),
#                 followup_time = "11:00:00",
#                 priority = "Super"
#             )
#             print(row)
#         return Response({}, status=status.HTTP_200_OK)

# class StoreUploader(APIView):
#     # permission_classes = (IsAuthenticated,)
#     def post(self, request):
#         try:
#             csv_file = request.FILES["file"]
#         except:
#             return Response(
#                 {"error": "Attach File to your request"},
#                 status=status.HTTP_400_BAD_REQUEST,
#             )
#         reader = pd.read_csv(csv_file, encoding="latin-1")
#         # reader = reader.dropna()
        
#         phone_numbers = reader["contact"]
#         name = reader["storage_name"]
#         # query = reader["query"]
#         # latitude = reader["latitude"]
#         # logitude = reader["longitude"]
#         fulladdr = reader["address"]
#         # categories = reader["categories"]
#         # url = reader["url"]
#         # addr1 = reader["addr1"]
#         # addr2 = reader["addr2"]
#         # addr3 = reader["addr3"]
#         # addr4 = reader["addr4"]
#         district = reader["city"]
#         manager_name = reader["manager_name"]
#         # print((latitude))
        
#         for row in range(len(phone_numbers)):
#             # geolocator = Nominatim(user_agent="mobile_app")
#             # location = geolocator.reverse(str(latitude[row])+","+str(logitude[row]))
#             # address = location.raw['address']

#             city_obj = core_models.Cities.objects.get_or_create(name=district[row])[0]
            
#             store_models.Store.objects.create(
#                 name = name[row],
#                 # query = query[row],
#                 # latitude = latitude[row],
#                 # logitude = logitude[row],
#                 phone_number = phone_numbers[row],
#                 city = city_obj,
#                 fulladdr = fulladdr[row],
#                 # categories = categories[row],
#                 # url = url[row],
#                 # addr1 = addr1[row],
#                 # addr2 = addr2[row],
#                 # addr3 = addr3[row],
#                 # addr4 = addr4[row],
#                 district = district[row],
#                 manager = manager_name[row]
#             )
#             print(city_obj)
#         return Response({}, status=status.HTTP_200_OK)