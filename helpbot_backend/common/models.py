from django.db import models

# Create your models here.


class CreatedUpdatedDateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")
    updated_at = models.DateTimeField(auto_now=True, verbose_name="Updated At")

    class Meta:
        abstract = True


class CreatedDateModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True, verbose_name="Created At")

    class Meta:
        abstract = True
