import io
import json
import random
import re
# from django_countries import countries
from django.db.models import Q
# from django_countries.fields import Country
# from phonenumbers.phonenumberutil import region_code_for_number
# from phonenumbers.phonenumberutil import region_code_for_country_code
# import phonenumbers
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
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny, IsAuthenticated
# from core.permissions import IsOwner
from .functions import LogActivity
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from datetime import date, datetime, timedelta
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse, JsonResponse
from leads import models as lead_models
from leads import serializers as lead_serializers
from panel_user import models as panel_models
from panel_user import serializers as panel_serializers
from core import models as core_models

now = date.today()
# current_time = datetime.datetime.utcnow().strftime("%H:%M:%S")
# today = datetime.date.today()



class LeadDashboard(ListAPIView):
    serializer_class = lead_serializers.LeadDashboardSerializer
    queryset = lead_models.Lead.objects.all()

    def get_queryset(self):
        return self.queryset.filter()[:1]

class LeadDetailsAPIView(RetrieveAPIView):
    serializer_class = lead_serializers.LeadDashboardSerializer

    def get_object(self):
        id = self.request.GET.get("id")
        queryset = lead_models.Lead.objects.get(id = id)
        return queryset

class LeadUpdateView(APIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = lead_serializers.LeadSaveSerializers
    
    def patch(self,request,id):
        data = request.data
        try:
            lead = lead_models.Lead.objects.get(id = id)
        except:
            return Response({"error":"Not Found."},status=status.HTTP_400_BAD_REQUEST)

        serializer = self.serializer_class(lead, data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({"error":"Invaild Data."},status=status.HTTP_400_BAD_REQUEST)
        # for addr in address:
        #     addr_obj = lead_models.Address.objects.create(
        #         street_road = addr.get("street_road",""),
        #         locality = addr.get("locality",""),
        #         post_office = addr.get("post_office",""),
        #         pincode = addr.get("pincode",0),
        #         town_city = core_models.Cities.objects.get(id = addr.get("town_city", None)))
        #     lead.address.add(addr_obj)

        # act_obj = LogActivity(lead,request, request.user, "Lead Details Update", "", "Details Update", 0)
        # lead.log.add(act_obj)
        return Response({"message":"Lead Update Success."},status=status.HTTP_200_OK)

class LeadAddressUpdateView(APIView):
    permission_classes = (IsAuthenticated,)
    serializer_class = lead_serializers.AddressCRUDSerializer
    def post(self,request,id):
        addr = request.data
        try:
            lead = lead_models.Lead.objects.get(id = id)
        except:
            return Response({"error":"Not Found."},status=status.HTTP_400_BAD_REQUEST)
        
        addr_obj = lead_models.Address.objects.create(
            street_road = addr.get("street_road",""),
            locality = addr.get("locality",""),
            post_office = addr.get("post_office",""),
            pincode = addr.get("pincode",0),
            town_city = core_models.Cities.objects.get(id = addr.get("town_city_id", None)))

        lead.address.add(addr_obj)

        act_obj = LogActivity(lead,request, request.user, "Lead Details Update", "", "Details Update", 0)
        lead.log.add(act_obj)
        return Response({"message":"Lead Address Update Success."},status=status.HTTP_200_OK)


    def patch(self,request,id):
        addr = request.data
        try:
            addr_obj = lead_models.Address.objects.get(id = id)
        except:
            return Response({"error":"Not Found."},status=status.HTTP_400_BAD_REQUEST)
        data = {
            "street_road" : addr.get("street_road",""),
            "locality" : addr.get("locality",""),
            "post_office" : addr.get("post_office",""),
            "pincode" : addr.get("pincode",0),
            "town_city" : addr.get("town_city_id")
        }
        serializer = self.serializer_class(addr_obj, data=data)
        if serializer.is_valid():
            serializer.save()
        else:
            return Response({"error":"Invaild Data."},status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"Lead Update Success."},status=status.HTTP_200_OK)
    
    def delete(self,request,id):
        try:
            lead_models.Address.objects.filter(id = id).delete()
        except:
            return Response({"error":"Not Found."},status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"Address Deleted Success."},status=status.HTTP_200_OK)
        

class AddAlterNumber(APIView):
    def post(self,request,id):
        data = request.data
        mobile = data.get("mobile")
        try:
            lead_obj = lead_models.Lead.objects.get(id = id)
            obj = lead_models.Contact.objects.filter(mobile = mobile)
            if not obj:
                c_obj = lead_models.Contact.objects.create(mobile = mobile)
            else:
                return Response({"error":"Number Already Exists!"},status=status.HTTP_400_BAD_REQUEST)
            if not lead_obj.primary_contact:
                lead_obj.primary_contact = c_obj
            elif not lead_obj.secondary_contact:
                lead_obj.secondary_contact = c_obj
            elif not lead_obj.content_number:
                lead_obj.content_number = c_obj
            elif not lead_obj.whatsapp_contact:
                lead_obj.whatsapp_contact = c_obj
            lead_obj.save()
            act_obj = LogActivity(lead_obj,request, request.user, "Lead Details Update", "", "Update Alternate Number", 0)
            lead_obj.log.add(act_obj)
        except Exception as e:
            print(e)
            return Response({"error":"Somethings went wrong!"},status=status.HTTP_400_BAD_REQUEST)
        return Response({"message":"Alternate Number Added Success."},status=status.HTTP_200_OK)



class LeadSourceListView(ListAPIView):
    # permission_classes = (IsAuthenticated,)
    serializer_class = lead_serializers.LeadSourceSerializer
    queryset = lead_models.LeadSource.objects.all()

class LeadStatusView(ListAPIView):
    serializer_class = lead_serializers.LeadStatusSerializer

    def get_queryset(self):
        user_obj = panel_models.Profile.objects.get(user = self.request.user)
        queryset = lead_models.LeadStatus.objects.filter(user = user_obj.user_type.id)
        return queryset

class LeadActionView(ListAPIView):
    serializer_class = lead_serializers.LeadActionSerializer
    
    def get_queryset(self):
        user_obj = panel_models.Profile.objects.get(user = self.request.user)
        queryset = lead_models.LeadAction.objects.filter(user = user_obj.user_type.id)
        return queryset

class ActivityTypeListView(ListAPIView):
    serializer_class = lead_serializers.CategorySerializer

    def get_queryset(self):
        q_type = self.request.GET.get("type")
        if not q_type:
            raise Http404("Not Found.")

        query = lead_models.ActivityType.objects.filter(type_name = q_type)[0]
        queryset = lead_models.Category.objects.filter(activity_id = query.id)
        return queryset

class ActivityView(ListAPIView):
    serializer_class = lead_serializers.ActivitySerializer

    def get_queryset(self):
        id = self.request.GET.get("id")
        activity_type = self.request.GET.get("activitytype")
        try:
            lead_obj = lead_models.Lead.objects.get(id = id)
        except ObjectDoesNotExist:
            raise Http404("Not Found.")
        queryset = lead_obj.log.all()

        if activity_type:
            queryset = queryset.filter(activitytype = activity_type)

        return queryset


class LeadFilterAPIView(ListAPIView):
    serializer_class = lead_serializers.LeadTableDetailsSerializer
    def get_queryset(self):
        queryset = lead_models.Lead.objects.all()
        day = self.request.query_params.get("day")
        city = self.request.query_params.get("city")
        language = self.request.query_params.get("language")
        priority = self.request.query_params.get("priority")
        source = self.request.query_params.get("source")

        if day == "today":
            queryset = queryset.filter(followup_date = date.today())
        elif day == "tomarrow":
            queryset = queryset.filter(followup_date = date.today() + timedelta(1))

        if city:
            queryset = queryset.filter(city__id = city)

        if language:
            queryset = queryset.filter(language__id = language)

        if priority:
            queryset = queryset.filter(priority = priority)

        if source:
            queryset = queryset.filter(lead_source__id = source)

        return queryset.order_by("-created_at")

class LeadActionUpdateView(APIView):
    serializer_class = lead_serializers.LeadActionUpdateSerializers
    def post(self, request, id):
        data = request.data
        lead_obj = lead_models.Lead.objects.get(id = id)
        activitytype = data.get("activitytype")
        message = data.get("message","")
        category = data.get("category")
        sub_category = data.get("sub_category")
        print(data)
        data = {
            "by_user" : request.user.id,
            "activitytype" : activitytype,
            "message" : message,
            "category" : category,
            "sub_category" : sub_category
        }

        serializer = self.serializer_class(data=data)
        if serializer.is_valid(raise_exception=True):
            obj = serializer.save()
            lead_obj.log.add(obj)

        result = {
            "message":"Success"
        }
        return Response(result, status=status.HTTP_200_OK)

class CreateLeadAPIView(ListAPIView):
    def post(self, request):
        data = request.data
        primary_name = data.get("primary_name")
        city = data.get("city")
        lead = data.get("phone")
        contact_objs = lead_models.Contact.objects.filter(mobile = lead)
        if contact_objs:
            return Response({"error":"Phone Number Already Exists!"}, status=status.HTTP_400_BAD_REQUEST)
        else:
            contact_obj = lead_models.Contact.objects.create(mobile = lead)
        data = {
            "primary_name":primary_name,
            "city":city,
            "lead":contact_obj.id,
            "followup_date": date.today(),
            "followup_time": "11:00:00"
        }

        lead_serializer_obj = lead_serializers.LeadCreateUpdateSerializers(data=data)
        if lead_serializer_obj.is_valid(raise_exception=True):
            lead_obj = lead_serializer_obj.save()
            print(lead_obj)
            return Response(lead_serializers.LeadCreateUpdateSerializers(lead_obj).data, status=status.HTTP_200_OK)
        else:
            return Response({}, status=status.HTTP_400_BAD_REQUEST)

class LeadFiltersData(APIView):
    # permission_classes = (IsAuthenticated,)
    
    def get(self, request):
        call_status = lead_models.LeadStatus.objects.all()
        panel_user = panel_models.Profile.objects.filter(
            user_type__name="AGENT", 
        )
        pccs = panel_serializers.ProfileFilterSerializer(panel_user, many=True)
        callSerializer = lead_serializers.LeadStatusFilterSerializer(
            call_status, many=True)

        priority = [
            {
            "priority":"Urgent"  
            },
            {
            "priority":"Super"  
            },
            {
            "priority":"Low"  
            },
            {
            "priority":"High"  
            }
        ]
        results = {
            "priority": priority,
            "lead_status": json.loads(
                (JsonResponse(callSerializer.data, safe=False).content)
            ),
            "agents": json.loads((JsonResponse(pccs.data, safe=False).content)),
        }
        return Response(results, status=status.HTTP_200_OK)
