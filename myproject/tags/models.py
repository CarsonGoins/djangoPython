from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


# Create your models here. - to pull out data from database to present to user
# store and pull data

class Tag(models.Model):
    label = models.CharField(max_length=255)

class tagged_item(models.Model):
    # dependency on tag
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # to define a generic relationsip we need the below three fields
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey