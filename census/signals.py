from django.db.models.signals import post_delete, pre_save
from django.dispatch import receiver

from census.models import Employee


@receiver(post_delete, sender=Employee)
def submission_delete(sender, instance, **kwargs):
    instance.photo.delete(False)
    instance.qr_code.delete(False)


@receiver(pre_save, sender=Employee)
def delete_file_on_change_extension(sender, instance, **kwargs):
    if instance.pk:
        try:
            old_photo = Employee.objects.get(pk=instance.pk).photo
        except Employee.DoesNotExist:
            return
        else:
            new_photo = instance.photo
            if old_photo and old_photo.url != new_photo.url:
                old_photo.delete(save=False)
