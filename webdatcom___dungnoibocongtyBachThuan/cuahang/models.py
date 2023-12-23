from django.db import models


class Cuahang(models.Model):
  tencuahang = models.CharField(max_length=255)
  mota = models.TextField()
