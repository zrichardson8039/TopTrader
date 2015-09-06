from django.db import models
from django.contrib.auth.models import User


class EditMixin(models.Model):
    creator = models.ForeignKey(
        User, null=True, blank=True,
        related_name="%(app_label)s_%(class)s_creator")
    created_at = models.DateTimeField(null=True, auto_now_add=True)
    modified_at = models.DateTimeField(null=True, auto_now=True)

    class Meta:
        abstract = True