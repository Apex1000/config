# from django_countries.serializer_fields import CountryField
from rest_framework import serializers
from core import models as core_models
from .models import *
from dateutil import tz
import datetime
import pytz
tz = pytz.timezone('Asia/Kolkata')

#+++++++++++++++++++++++++++++++++++++++++++++++++++#

class LeadStatusFilterSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadStatus
        fields = (
            "id",
            "status",
        )

#+++++++++++++++++++++++++++++++++++++++++++++++++++#


class LeadCreateUpdateSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lead
        fields = "__all__"

class AddressCRUDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"

class LeadSourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadSource
        fields = "__all__"

class LeadStatusSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadStatus
        fields = "__all__"

class LeadActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = LeadAction
        fields = (
            "id",
            "action",
        )

class ActivityTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = ActivityType
        fields = (
            "id",
            "type_name",
            "score",
        )

class SubCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = SubCategory
        fields = (
            "id",
            "sub_category",
        )

class CategorySerializer(serializers.ModelSerializer):
    activity = serializers.SerializerMethodField()
    activity_id = serializers.SerializerMethodField()
    sub_category = serializers.SerializerMethodField()
    
    class Meta:
        model = Category
        fields = (
            "id",
            "activity",
            "activity_id",
            "category",
            "sub_category",
        )
    
    def get_activity(self,obj):
        return obj.activity.type_name if obj.activity else None
    
    def get_activity_id(self,obj):
        return obj.activity.id

    def get_sub_category(self,obj):
        objs = SubCategory.objects.filter(category = obj)
        if len(objs)>0:
            return SubCategorySerializer(objs, many=True).data

class ActivitySerializer(serializers.ModelSerializer):
    created_at_date = serializers.SerializerMethodField()
    created_at_time = serializers.SerializerMethodField()
    by_user = serializers.SerializerMethodField()
    activitytype = serializers.SerializerMethodField()
    category = serializers.SerializerMethodField()
    sub_category = serializers.SerializerMethodField()
    score = serializers.SerializerMethodField()
    message = serializers.SerializerMethodField()
    
    class Meta:
        model = Activity
        fields = (
            "id",
            "created_at_date",
            "created_at_time",
            "message",
            # "is_hide",
            "by_user",
            "activitytype",
            "category",
            "sub_category",
            "score",
        )
    def get_created_at_date(self,obj):
        return (obj.created_at.astimezone(tz)).date()
    
    def get_created_at_time(self,obj):
        return (obj.created_at.astimezone(tz)).time().strftime("%H:%M:%S")
    
    def get_by_user(self,obj):
        return obj.by_user.username
    
    def get_activitytype(self,obj):
        return obj.activitytype.type_name if obj.activitytype else None
    
    def get_category(self,obj):
        return obj.category.category if obj.category else None
    
    def get_sub_category(self,obj):
        return obj.sub_category.sub_category if obj.sub_category else None
    
    def get_score(self,obj):
        return obj.activitytype.score 

    def get_message(self, obj):
        at = obj.activitytype.type_name if obj.activitytype else ""
        ct = obj.category.category if obj.category else ""
        sct = obj.sub_category.category if obj.sub_category else ""
        return "%s, %s, %s, %s"%(at,ct,sct,obj.message)

class AddressSerializer(serializers.ModelSerializer):
    town_city = serializers.SerializerMethodField()
    town_city_id = serializers.SerializerMethodField()
    class Meta:
        model = Address
        fields = (
            "id",
            "street_road",
            "locality",
            "post_office",
            "pincode",
            "town_city",
            "town_city_id"
        )
    def get_town_city(self,obj):
        return obj.town_city.name if obj.town_city else None
    
    def get_town_city_id(self,obj):
        return obj.town_city.id if obj.town_city else None

class LeadDashboardSerializer(serializers.ModelSerializer):
    lead_source = serializers.SerializerMethodField()
    panel_user = serializers.SerializerMethodField()
    lead = serializers.SerializerMethodField()
    primary_contact = serializers.SerializerMethodField()
    secondary_contact = serializers.SerializerMethodField()
    content_number = serializers.SerializerMethodField()
    whatsapp_contact = serializers.SerializerMethodField()
    address = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    city_id = serializers.SerializerMethodField()
    lead_status = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    
    class Meta:
        model = Lead
        fields = (
            "id",
            "primary_name",
            "secondary_name",
            "followup_date",
            "followup_time",
            "priority",
            "count",
            "lead_source",
            "panel_user",
            "lead",
            "city",
            "city_id",
            "lead_status",
            "language",
            "primary_contact",
            "secondary_contact",
            "content_number",
            "whatsapp_contact",
            "address"
        )
    
    def get_lead(self,obj):
        return "XXXXXX"+str(obj.lead.mobile[6:]) if obj.lead else None
    
    def get_primary_contact(self,obj):
        return "XXXXXX"+str(obj.primary_contact.mobile[6:]) if obj.primary_contact else None
    
    def get_secondary_contact(self,obj):
        return "XXXXXX"+str(obj.secondary_contact.mobile[6:]) if obj.secondary_contact else None
    
    def get_content_number(self,obj):
        return "XXXXXX"+str(obj.content_number.mobile[6:]) if obj.content_number else None
    
    def get_whatsapp_contact(self,obj):
        return "XXXXXX"+str(obj.whatsapp_contact.mobile[6:]) if obj.whatsapp_contact else None

    def get_lead_source(self,obj):
        return obj.lead_source.source if obj.lead_source else None
    
    def get_panel_user(self,obj):
        return obj.panel_user.user.username if obj.panel_user else None
    
    def get_city(self,obj):
        return obj.city.name if obj.city else None
    
    def get_city_id(self,obj):
        return obj.city.id if obj.city else None

    def get_lead_status(self,obj):
        return obj.lead_status.status if obj.lead_status else None
    
    def get_language(self,obj):
        return obj.language.language if obj.language else None
    
    def get_address(self, obj):
        return AddressSerializer(obj.address.all(),many=True).data

class LeadTableDetailsSerializer(serializers.ModelSerializer):
    lead_source = serializers.SerializerMethodField()
    panel_user = serializers.SerializerMethodField()
    lead = serializers.SerializerMethodField()
    city = serializers.SerializerMethodField()
    lead_status = serializers.SerializerMethodField()
    language = serializers.SerializerMethodField()
    
    class Meta:
        model = Lead
        fields = (
            "id",
            "primary_name",
            "secondary_name",
            "followup_date",
            "followup_time",
            "priority",
            "count",
            "lead_source",
            "panel_user",
            "lead",
            "city",
            "lead_status",
            "language",
        )
    
    def get_lead(self,obj):
        return obj.lead.mobile if obj.lead else None

    def get_lead_source(self,obj):
        return obj.lead_source.source if obj.lead_source else None
    
    def get_panel_user(self,obj):
        return obj.panel_user.user.username if obj.panel_user else None
    
    def get_city(self,obj):
        return obj.city.name if obj.city else None
    
    def get_lead_status(self,obj):
        return obj.lead_status.status if obj.lead_status else None
    
    def get_language(self,obj):
        return obj.language.language if obj.language else None

class LeadSaveSerializers(serializers.ModelSerializer):
    # address = AddressSerializer(many = True)

    class Meta:
        model = Lead
        fields = "__all__"

    # def update(self, instance, validated_data):
    #     # image = validated_data.pop("address")
    #     # instance.id = validated_data.get("id", instance.id)
    #     print(instance.id)
    #     instance.save()
    #     # new_address = []
    #     # for addr in address:
    #     #     if "id" in img.keys():
    #     #         if ItemImage.objects.filter(id=img["id"]).exists():
    #     #             i = ItemImage.objects.get(id=img["id"])
    #     #             i.image = img.get("image", i.image)
    #     #             i.save()
    #     #             keep_image.append(i.id)
    #     #         else:
    #     #             continue
    #     #     else:
    #     #         i = ItemImage.objects.create(**img, item=instance)
    #     #         keep_image.append(i.id)
    #     # for img in instance.image:
    #     #     if img.id not in keep_image:
    #     #         img.delete()
    #     return instance

class LeadActionUpdateSerializers(serializers.ModelSerializer):
    
    class Meta:
        model = Activity
        fields = "__all__"