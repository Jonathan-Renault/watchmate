from django.contrib import admin

from watchmate_app import models

admin.site.register(models.StreamPlatform)
admin.site.register(models.WatchList)
admin.site.register(models.Review)

