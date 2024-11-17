from django.db import models
from django.utils.translation import gettext_lazy as _


class CallMeta(models.Model):
    class RegistryType(models.TextChoices):
        BEGIN = "B", _("Beginning")
        END = "E", _("End")

    rtype = models.CharField(max_length=1, choices=RegistryType)
    timestamp = models.DateTimeField()
    call_id = models.BigIntegerField()
    source = models.CharField(max_length=11, null=True)
    destination = models.CharField(max_length=11, null=True)