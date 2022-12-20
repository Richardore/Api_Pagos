from django.db import models

from django.utils.translation import gettext_lazy as _
# Create your models here.

from users.models import User

class Services(models.Model):
    class Servicios(models.TextChoices):
        NETFLIX = 'NF', _('Netflix')
        AMAZON = 'AP', _('Amazon Video')
        START = 'ST', _('Start+')
        PARAMOUNT = 'PM', _('Paramount+')

    servicio = models.CharField(
        max_length=2,
        choices=Servicios.choices,
        default=Servicios.NETFLIX,
    )
    Description = models.CharField(max_length=250)

    Logo = models.CharField(max_length=250)


class Payment_user(models.Model):
    usuario = models.ForeignKey(User, on_delete =models.CASCADE, related_name='userss')
    servicio = models.ForeignKey(Services,on_delete =models.CASCADE, related_name='services')
    Amount = models.FloatField(default=0.0)
    PaymentDate = models.DateField(auto_now_add=True)
    ExpirationDate = models.DateField(auto_now_add=True)



class Expired_payments(models.Model):
    Payment_user_id = models.ForeignKey(Payment_user,on_delete =models.CASCADE, related_name='services')
    Penalty_fee_amount = models.FloatField(default=0.0)
    