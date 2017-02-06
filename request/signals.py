from django.db.models.signals import post_save, pre_delete
from django.dispatch import receiver
from .models import Request


@receiver(post_save, sender=Request)
def set_request_name(sender, instance, created, **kwargs):
    if created:
        instance.name = '%i_%s' % (instance.id, instance.user.last_name)
        if instance.user.pi:
            instance.name += '_' + instance.user.pi.name
        instance.save()


@receiver(pre_delete, sender=Request)
def delete_libraries_and_samples(sender, instance, **kwargs):
    instance.libraries.all().delete()
    instance.samples.all().delete()
