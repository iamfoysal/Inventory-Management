from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.db.models.signals import post_save
from django.conf import settings
from django.dispatch import receiver
from .models import User, Users


@receiver(post_save, sender=User)
def create_user(sender, instance, created, **kwargs):
    if created and instance.email:
        Users.objects.create(user=instance)
        
        message = render_to_string('user/accountmail.html', {'name': instance.get_full_name()})
        send_mail(
            'Welcome to join inventory management System',
            message,
            settings.DEFAULT_FROM_EMAIL,
            [instance.email],
            fail_silently= False,
        )


       