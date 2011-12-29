from django.db import models
from django.conf import settings
# Create your models here.


class Image(models.Model):
    image = models.ImageField(upload_to=settings.IMAGE_PATH)

    def __unicode__(self):
        return self.image.url


class Label(models.Model):
    name = models.CharField(max_length=255)
    has_area = models.BooleanField(default=True)

    def __unicode__(self):
        return self.name

class LabelValue(models.Model):
    label = models.ForeignKey(Label)
    value = models.CharField(max_length=255)
    position = models.PositiveSmallIntegerField()

    def __unicode__(self):
        return self.value

    class Meta:
        ordering = ['position']

class Annotation(models.Model):
    image = models.ForeignKey(Image)
    label = models.ForeignKey(Label)
    value = models.ForeignKey(LabelValue)
    area_x1 = models.PositiveIntegerField(null=True, blank=True)
    area_x2 = models.PositiveIntegerField(null=True, blank=True)
    area_y1 = models.PositiveIntegerField(null=True, blank=True)
    area_y2 = models.PositiveIntegerField(null=True, blank=True)



