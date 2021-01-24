from django.db import models
from django.contrib.auth.models import User

class Notification(models.Model):

    #2 constants to differanciante the type of notification
    MESSAGE = 'message'
    APPLICATION = 'application'

    #For Django admin interface
    CHOICES = (
        (MESSAGE,'Message'), 
        (APPLICATION, 'Application')
    )
    #Reference to User
    to_user = models.ForeignKey(User, related_name='notifications', on_delete=models.CASCADE)
    notification_type = models.CharField(max_length=20, choices=CHOICES)
    is_read = models.BooleanField(default=False)
    extra_id = models.IntegerField(null=True,blank=True) #To keep track if it's an ID for a application or message

    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(User, related_name='creatednotifications', on_delete=models.CASCADE)

    class Meta:
        ordering = ['-created_at']


