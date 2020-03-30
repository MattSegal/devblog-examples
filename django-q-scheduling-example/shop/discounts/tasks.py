from django.utils import timezone

from .models import Discount

def delete_expired_discounts():
    """
    Deletes all Discounts that are more than a minute old
    """
    one_minute_ago = timezone.now() - timezone.timedelta(minutes=1)
    expired_discounts = Discount.objects.filter(created_at__lte=one_minute_ago)
    expired_discounts.delete()
