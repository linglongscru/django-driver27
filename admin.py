from django.contrib import admin

from .models import Driver, Team, Competition, Circuit, Season

admin.site.register(Driver)
admin.site.register(Team)
admin.site.register(Competition)
admin.site.register(Circuit)
admin.site.register(Season)