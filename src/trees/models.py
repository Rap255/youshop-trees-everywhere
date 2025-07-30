from django.db import models
from django.utils.translation import gettext_lazy as _
from users.models import UserModel
from accounts.models import Account


class Tree(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name=_("Name"),
        help_text=_("User name"),
        unique=True
    )
    scientific_name = models.CharField(
        max_length=50,
        verbose_name=_("Name"),
        help_text=_("User name"),
        unique=True
    )

    class Meta:
        db_table = "tree"
        verbose_name = _("Tree")
        verbose_name_plural = _("Trees")
        ordering = ["id"]


class PlantedTree(models.Model):

    user = models.ForeignKey(
        UserModel,
        on_delete=models.PROTECT,
        related_name="planted_tree",
        verbose_name=_("User"),
        help_text=_("User"),
        null=True,
    )

    tree = models.ForeignKey(
        Tree,
        on_delete=models.PROTECT,
        related_name="tree",
        verbose_name=_("Tree"),
        help_text=_("Tree"),
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

    age = models.CharField(
        verbose_name=_("Age"),
        help_text=_("Age of Tree"),
        unique=True
    )

    planted_at = models.DateTimeField(
        verbose_name=_("Planted At"),
        help_text=_("When it was planted"),
    )

    longitude = models.DecimalField(
        verbose_name=_("Longitude"),
        help_text=_("Longitude that was planted")
    )

    class Meta:
        db_table = "planted_tree"
        verbose_name = _("Planted Tree")
        verbose_name_plural = _("Planted Trees")
        ordering = ["id"]