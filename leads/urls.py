from django.urls import path, include
from leads import views as leads_views

urlpatterns = [
    path("dashboard/", leads_views.LeadDashboard.as_view(), name="dashboard"),
    path("lead-details/", leads_views.LeadDetailsAPIView.as_view(), name="lead_details"),
    path("update/<int:id>/", leads_views.LeadUpdateView.as_view(), name="update"),
    path("address-update/<int:id>/", leads_views.LeadAddressUpdateView.as_view(), name="address_update"),
    path("alternate-number/<int:id>/", leads_views.AddAlterNumber.as_view(), name="alternate_number"),
    path("lead-source/", leads_views.LeadSourceListView.as_view(), name="lead_source"),
    path("lead-status/", leads_views.LeadStatusView.as_view(), name="lead_status"),
    path("lead-actions/", leads_views.LeadActionView.as_view(), name="lead_actions"),
    path("activity-type/", leads_views.ActivityTypeListView.as_view(), name="activity_type"),
    path("activity/", leads_views.ActivityView.as_view(), name="activity"),
    path("filter/", leads_views.LeadFilterAPIView.as_view(), name="filter"),
    path("action/<int:id>/", leads_views.LeadActionUpdateView.as_view(), name="action"),
    
    path("create-lead/", leads_views.CreateLeadAPIView.as_view(), name="create_lead"),
    #+++++++++++++++++++++++++++++++++++++#
    path("lead-filter-data/", leads_views.LeadFiltersData.as_view(), name="lead_filter"),
]
