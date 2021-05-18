from leads import models as lead_models

def LogActivity(lead,request,user,activitytype,msg,category,subCategory):
    if not activitytype == 0:
        at_obj = lead_models.ActivityType.objects.get_or_create(type_name = activitytype)[0]
    else:
        at_obj = None

    if not category == 0:
        ct_obj = lead_models.Category.objects.filter(category = category)
        if not ct_obj:
            ct_obj = lead_models.Category.objects.create(
                activity = at_obj,
                category = category.first())
    else:
        ct_obj = None
    
    if not subCategory == 0:
        sct_obj = lead_models.SubCategory.objects.filter(sub_category = subCategory)
        if not sct_obj:
            sct_obj = lead_models.SubCategory.objects.create(
                category = ct_obj.first(),
                sub_category = subCategory.first())
    else:
        sct_obj = None
    obj = lead_models.Activity.objects.create(
        by_user = request.user,
        activitytype = at_obj,
        message = msg,
        category = ct_obj.first(),
        sub_category = sct_obj.first() if sct_obj else None 
    )
    lead.log.add(obj)
    return obj