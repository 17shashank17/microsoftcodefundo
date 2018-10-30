from django.contrib import admin
from codefundo.models import user_details,track_users,gov_fund
# Register your models here.
admin.site.register(user_details)
admin.site.register(track_users)
admin.site.register(gov_fund)