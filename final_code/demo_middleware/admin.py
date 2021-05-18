import json 

from django.contrib import admin

from django.core.serializers.json import DjangoJSONEncoder
from django.core import serializers

from .models import newstats

@admin.register(newstats)
class NewStatsAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):

        stat_data = (
            newstats.objects.annotate().values("win","mac","iph","android","oth")
        )

        # data = newstats.objects.all()
        # newdata = serializers.serialize('json', list(data), fields=("win","mac","iph","android","oth"))
        # print(newdata)

        as_json = json.dumps(list(stat_data), cls=DjangoJSONEncoder)
        extra_context = extra_context or {"stat_data": as_json}

        return super().changelist_view(request, extra_context=extra_context)


