from django.conf import settings
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save


class UserSetting(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, null=True, on_delete=models.CASCADE())
    postemail = models.BooleanField(default=True)
    commentemail = models.BooleanField(default=True)

    def __str__(self):
        return str(self.user)


def post_save_settings_model_receiver(sender, instance, created, *args, **kwargs):
    if created:
        try:
            UserSetting.objects.create(user=instance)
        except:
            pass


post_save.connect(post_save_settings_model_receiver, sender=settings.AUTH_USER_MODEL)
