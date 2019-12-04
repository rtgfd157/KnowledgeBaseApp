from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from core.utils import generate_random_string
from knowledge_app.models import Subject

@receiver(pre_save, sender=Subject)
def add_slug_to_subject(sender, instance, *args, **kwargs):
    if instance and not instance.slug:
        print("instance.title : ",instance.title)
        slug = slugify(instance.title)
        print("slug : ",slug)
        random_string = generate_random_string()
        instance.slug = slug + "-" + random_string