from django.db import models
from django.conf import settings

User = settings.AUTH_USER_MODEL

# Create your models here.

class PaidChoices(models.TextChoices):
    PAID = 'Paid'
    UNPAID = 'Unpaid'


class Tada(models.Model):
    date = models.DateField()
    employee = models.ForeignKey(User, on_delete=models.CASCADE)
    travel_cost = models.IntegerField(default=0)
    lunch_cost = models.IntegerField(default=0)
    instruments_cost = models.IntegerField(default=0)
    paid = models.CharField(max_length=150, choices=PaidChoices.choices,default=PaidChoices.UNPAID)


    def __str__(self):
        return str(self.employee.get_full_name())

    def get_total(self):
        return (self.instruments_cost + self.lunch_cost + self.travel_cost) 