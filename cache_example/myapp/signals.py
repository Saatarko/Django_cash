from django.db.models.signals import post_save, post_delete
from django.dispatch import receiver
from django.core.cache import cache
from .models import Posts


@receiver(post_save, sender=Posts)
@receiver(post_delete, sender=Posts)
def clear_post_cache(sender, instance, **kwargs):
    cache_key = f'posts_by_category_{instance.category_id}'
    cache.delete(cache_key)
