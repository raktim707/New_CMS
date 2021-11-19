from django.db import models
import random

import os
# Create your models here.

from django.dispatch import receiver


def validate_file_extension(value):
    import os
    from django.core.exceptions import ValidationError
    ext = os.path.splitext(value.name)[1]  # [0] returns path+filename
    valid_extensions = ['.mp4', '.webm', '.ogg',
                        '.jpg', '.png']
    if not ext.lower() in valid_extensions:
        raise ValidationError('Unsupported file extension.')


class GalleryPost(models.Model):

    class Choice(models.TextChoices):
        _1 = 'col-md-4', 'col-md-4'
        _2 = 'col-md-6', 'col-md-6'
        _3 = 'col-md-8', 'col-md-8'
        _4 = 'col-md-10', 'col-md-10'
        _5 = 'col-md-12', 'col-md-12'
    name = models.CharField(max_length=50)
    ImageOrVideo = models.FileField(
        upload_to="gallery/", validators=[validate_file_extension])
    CssClass = models.CharField(
        max_length=10, choices=Choice.choices, default=Choice._1)

    def __str__(self):
        return self.name

    def isImage(self):
        if str(self.ImageOrVideo).endswith("jpg") or str(self.ImageOrVideo).endswith("png"):
            return True
        else:
            return False


@receiver(models.signals.post_delete, sender=GalleryPost)
def auto_delete_file_on_delete(sender, instance, **kwargs):
    """
    Deletes file from filesystem
    when corresponding `MediaFile` object is deleted.
    """
    if instance.ImageOrVideo:
        instance.ImageOrVideo.delete(save=True)


@receiver(models.signals.pre_save, sender=GalleryPost)
def auto_delete_file_on_change(sender, instance, **kwargs):
    """
    Deletes old file from filesystem
    when corresponding `MediaFile` object is updated
    with new file.
    """
    if not instance.pk:
        return False

    try:
        old_file = GalleryPost.objects.get(pk=instance.pk).ImageOrVideo
    except GalleryPost.DoesNotExist:
        return False

    new_file = instance.ImageOrVideo
    if not old_file == new_file:
        if os.path.isfile(old_file.path):
            os.remove(old_file.path)
