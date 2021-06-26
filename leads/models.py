from django.db import models
from core import models as core_models
from panel_user import models as panel_models
from logs import models as logs_models

class Contact(core_models.TimestampedModel):
    mobile = models.CharField(max_length=16, blank=True, null=True)

    def __str__(self):
        return self.mobile

class LeadSource(core_models.TimestampedModel):
    source = models.CharField(max_length=50, blank=True, null=True)
    user = models.ManyToManyField(panel_models.UserRoles, blank=True)
    def __str__(self):
        return self.source

class LeadStatus(core_models.TimestampedModel):
    status = models.CharField(max_length=100, blank=True, null=True)
    user = models.ManyToManyField(panel_models.UserRoles, blank=True)

    def __str__(self):
        return self.status

class LeadAction(core_models.TimestampedModel):
    action = models.CharField(max_length=100, blank=True, null=True)
    user = models.ManyToManyField(panel_models.UserRoles, blank=True)

    def __str__(self):
        return self.action

class Address(core_models.TimestampedModel):
    street_road = models.CharField(max_length=255, blank=True, null=True)
    locality = models.CharField(max_length=255, blank=True, null=True)
    post_office = models.CharField(max_length=255, blank=True, null=True)
    town_city = models.ForeignKey(
        core_models.Cities,
        related_name="address_town_city",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    pincode = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return "Address: {},{},{}".format(self.street_road,self.locality,self.pincode)

class ActivityType(core_models.TimestampedModel):
    type_name = models.CharField(max_length=100, blank=True, null=True)
    score =  models.IntegerField(default=0, blank=True, null=True)
    user = models.ManyToManyField(panel_models.UserRoles, blank=True)
    def __str__(self):
        return self.type_name

class Category(core_models.TimestampedModel):
    activity = models.ForeignKey(
        ActivityType,
        related_name='category_activity',
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    category = models.CharField(max_length=250, blank=True, null=True)

    def __str__(self):
        return self.category

class SubCategory(core_models.TimestampedModel):
    category = models.ForeignKey(
        Category,
        related_name='category_sub',
        on_delete=models.CASCADE,
        null=True,
        default=None
    )
    sub_category = models.CharField(max_length=100, blank=True, null=True)

    def __str__(self):
        return self.sub_category

class Activity(core_models.TimestampedModel):
    by_user = models.ForeignKey(
        "authentication.User",
        related_name="comments",
        blank=True,
        null=True,
        on_delete=models.CASCADE,
    )
    activitytype = models.ForeignKey(
        ActivityType,
        related_name="activity_type",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    message = models.CharField(max_length=255, null=True, blank=True)
    category = models.ForeignKey(
        Category,
        related_name='category_comment',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    sub_category = models.ForeignKey(
        SubCategory,
        related_name='sub_category_comment',
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    
    is_hide = models.BooleanField(default=False)

    def __str__(self):
        return "%s,%s" % (self.activitytype,self.category)

    class Meta:
        ordering = ["-created_at"]

class Lead(core_models.TimestampedModel):
    primary_name = models.CharField(max_length=255, blank=True, null=True)
    secondary_name = models.CharField(max_length=255, blank=True, null=True)
    lead_source = models.ForeignKey(
        LeadSource,
        related_name="lead_source",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )
    panel_user = models.ForeignKey(
        "panel_user.PanelUserProfile",
        related_name="paneluser",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
        default=None,
    )
    lead = models.ForeignKey(
        Contact,
        related_name="lead_content",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True
    )
    city = models.ForeignKey(
        core_models.Cities,
        related_name="patient_city",
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )
    # patient_area = models.CharField(max_length=255, blank=True, null=True)
    lead_status = models.ForeignKey(
        LeadStatus,
        related_name="lead_status",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True,
    )
    language = models.ForeignKey(
        core_models.Language,
        related_name="langauge",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )
    followup_date = models.DateField(auto_now=False, auto_now_add=False, default=None)
    followup_time = models.TimeField(auto_now=False, auto_now_add=False, default=None)
    primary_contact = models.ForeignKey(
        Contact,
        related_name="lead_primary_content",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True
    )
    secondary_contact = models.ForeignKey(
        Contact,
        related_name="lead_secondary_content",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True
    )
    content_number = models.ForeignKey(
        Contact,
        related_name="lead_content_number",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True
    )
    whatsapp_contact = models.ForeignKey(
        Contact,
        related_name="lead_whatsapp_content",
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        null=True
    )
    priority = models.CharField(max_length=50, blank=True, null=True)
    count = models.IntegerField(default=0, blank=True, null=True)
    address = models.ManyToManyField(Address, blank=True)
    log = models.ManyToManyField(Activity, blank=True)
    def __str__(self):
        return self.lead.mobile