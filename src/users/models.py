from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.contrib.auth.models import User


class AccessType(models.Model):

    name = models.CharField(
        max_length=50,
        verbose_name=_("Name"),
        help_text=_("Access type name"),
    )

    class Meta:
        db_table = "access_type"
        verbose_name = _("Access type")
        verbose_name_plural = _("Access types")
        ordering = ["id"]

    def __str__(self):
        return self.name

class UserModel(AbstractUser,PermissionsMixin):

    type_of_access = models.ForeignKey(AccessType,
        on_delete=models.PROTECT,
        related_name="users",
        verbose_name=_("Type of access"),
        help_text=_("Type of access"),
        null=True,
    )
    email = models.EmailField(
        max_length=50,
        unique=True,
        verbose_name=_("E-mail"),
        help_text=_("User's e-mail"),
    )
    
    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []


    class Meta:
        db_table = "users"
        verbose_name = _("Users")
        verbose_name_plural = _("Users")
        ordering = ["id"]

    def __str__(self):
        return self.name