from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import UserModel


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


class AccountUser(models.Model):

    user = models.ForeignKey(
        UserModel,
        on_delete=models.PROTECT,
        related_name="user",
        verbose_name=_("User"),
        help_text=_("User"),
        null=True,
    )

    account = models.ForeignKey(
        Account,
        on_delete=models.PROTECT,
        related_name="account",
        verbose_name=_("Account"),
        help_text=_("Account"),
        null=True,
    )

    class Meta:
        db_table = "account_user"
        verbose_name = _("User of Account")
        verbose_name_plural = _("Users of Accounts")
        ordering = ["id"]