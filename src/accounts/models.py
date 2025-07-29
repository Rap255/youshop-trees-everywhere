from django.db import models
from django.utils.translation import gettext_lazy as _


class Account(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name=_("Name"),
        help_text=_("User name"),
        unique=True
    )

    created = models.DateTimeField(
        auto_now_add=True,
        verbose_name=_("Creation date"),
        help_text=_("Creation date of the account"),
    )

    active = models.BooleanField(
        default=True,
        verbose_name=_("Active Account "),
        help_text=_(""),
    )

    class Meta:
        db_table = "account"
        verbose_name = _("Account")
        verbose_name_plural = _("Accounts")
        ordering = ["id"]