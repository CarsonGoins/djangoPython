from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from store.models import Product


# Create your models here. - to pull out data from database to present to user
# store and pull data

class TaggedItemManager(models.Manager):
    def get_tags_for(self, obj_type, obj_id):
        content_type = ContentType.objects.get_for_model(obj_type)

        return tagged_item.objects.select_related('tag').filter(
                content_type=content_type,
                object_id=obj_id
            )

class Tag(models.Model):
    label = models.CharField(max_length=255)

class tagged_item(models.Model):
    objects = TaggedItemManager()
    # dependency on tag
    tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    # to define a generic relationsip we need the below three fields
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    content_object = GenericForeignKey