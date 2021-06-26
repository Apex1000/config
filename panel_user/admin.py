from django.contrib import admin
from panel_user import models as panel_models
# Register your models here.

admin.site.register(panel_models.UserRoles)
admin.site.register(panel_models.PanelUserProfile)
admin.site.register(panel_models.Provider)