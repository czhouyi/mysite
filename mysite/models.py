from django.db import models
from django.contrib import admin
from django.contrib.auth.models import User

from mptt.models import MPTTModel
from mptt.admin import MPTTModelAdmin

# Create your models here.
class OpenId(models.Model):
    user = models.ForeignKey(User)
    openid = models.CharField(max_length=100)

    def __unicode__(self):
        return self.user.username

class Topic(MPTTModel):
    name = models.CharField(max_length=50)
    parent = models.ForeignKey('self', blank=True, null=True, related_name="children")

    class MPTTMeta:
        parent_attr = 'parent'

    def __unicode__(self):
        return self.name

class OpenIdAdmin(admin.ModelAdmin):
    list_display = ("user", "openid", )

admin.site.register(OpenId, OpenIdAdmin)
admin.site.register(Topic)
