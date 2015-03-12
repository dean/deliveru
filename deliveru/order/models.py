from django.db import models
from deliveru.user_profile.models import UserProfile


class Order(models.Model):
    '''Represents an submitted order.'''
    order_date = models.DateTimeField('date ordered')
    order_details = models.CharField(max_length=2000)
    user = models.ForeignKey(UserProfile)
