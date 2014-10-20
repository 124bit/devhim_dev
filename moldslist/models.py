from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _

#TODO Add a long descriptions, account existence test (all other things is available through BPMS admin)
class BPMSUser(models.Model):
    login = models.CharField(max_length=50,  verbose_name=_("BPMS user login"), unique=True)
    password = models.CharField(max_length=50,  verbose_name=_("BPMS user password"))
    web_user = models.OneToOneField(User, blank=True, null=True, on_delete=models.SET_NULL,
                                    verbose_name=_("Web user of BPMS account"))

    def __str__(self):
        return self.login

    class Meta:
        verbose_name = _('BPMS User')
        verbose_name_plural = _('BPMS Users')
        ordering = ['login']
