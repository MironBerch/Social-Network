from django.shortcuts import get_object_or_404

from notifications.models import Notification
from accounts.models import User


def get_notification(pk, to_user):
    return get_object_or_404(
        Notification, 
        pk=pk, 
        to_user=to_user,
    )


def get_user_notification(to_user: User):
    return Notification.objects.filter(
        to_user=to_user,
    )


def count_user_notification(
        request_user: User
    ):
    return Notification.objects.filter(
        to_user=request_user,
        created_at__gt=request_user.last_notification_read_time,
    ).count()
