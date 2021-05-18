from django.db import models
from core import models as core_models

class LogsScore(core_models.TimestampedModel):
    user = models.ForeignKey('authentication.User', related_name='user_logs_score', on_delete=models.CASCADE,blank=True, null=True)
    score = models.IntegerField(default=0)
    day = models.DateField(auto_now=False, auto_now_add=False,default=None,blank=True, null=True)
    time = models.TimeField(auto_now=False, auto_now_add=False,default=None,blank=True, null=True)
    def __str__(self):
        return "%s,%s"%(self.user,self.score)

class UserLogs(core_models.TimestampedModel):
    user = models.ForeignKey('authentication.User', related_name='user_logs', on_delete=models.CASCADE)
    log_msg = models.CharField(max_length=255, blank=True, null=True)

    def __str__(self):
        return self.user.username