from django.db import models
import os
import sys
from django.utils import timezone
from django.utils.translation import gettext_lazy as _


def upload_to(instance, filename):
    now = timezone.now()
    base, extension = os.path.splitext(filename.lower())
    milliseconds = now.microsecond // 1000
    return f"images/{now:%Y%m%d%H%M%S}{milliseconds}{extension}"

class Pessoas(models.Model):
    nome = models.CharField(max_length=100, blank=False, default='')
    cargo = models.CharField(max_length=100, blank=False, default='')
    cpf = models.CharField(max_length=100, blank=False, default='')
    foto = models.ImageField(_("foto"),upload_to=upload_to, blank=True)