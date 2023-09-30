import os
from django.db.models.signals import pre_delete
from django.dispatch import receiver

from .models import ImageUploadModel

@receiver(pre_delete, sender=ImageUploadModel)
def delete_old_file(sender, instance, **kwargs):
    if instance.image:
        if os.path.isfile(instance.image.path):
            os.remove(instance.image.path)