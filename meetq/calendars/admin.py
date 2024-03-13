from django.contrib import admin

from .models import *

admin.site.register(Calendar)
admin.site.register(Contact)
admin.site.register(Invited)
admin.site.register(Response)
admin.site.register(Schedule)
admin.site.register(Meeting)
admin.site.register(SchedulePlan)
