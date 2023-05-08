from django.contrib import admin

from testProject.models import TestModel, EmailSubscribed, Permission, Role

admin.site.register(TestModel)
admin.site.register(EmailSubscribed)
admin.site.register(Permission)
admin.site.register(Role)
