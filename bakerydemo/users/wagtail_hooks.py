from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register

from bakerydemo.users.models import User


class UserAdmin(ModelAdmin):
    model = User


modeladmin_register(UserAdmin)
