import calendar
import datetime as dt

from django.shortcuts import render
from rest_framework import serializers, viewsets
from rest_framework.decorators import api_view, action
from rest_framework.response import Response

from main import models

class CallMetaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.CallMeta
        fields = "__all__"


class CallMetaViewset(viewsets.ModelViewSet):
    queryset = models.CallMeta.objects.all()
    serializer_class = CallMetaSerializer

    @action(methods=['GET'], detail=True, url_name="invoice")
    def invoice(self, request, pk=None):
        year = request.query_params.get("year", dt.datetime.now().year)
        month = request.query_params.get("month", None)
        if type(year) == str:
            year = int(year)
        if type(month) == str:
            month = int(month)
        if month is None:
            today = dt.date.today()
            first = today.replace(day=1)
            month = (first - dt.timedelta(days=1)).month
        first_day = dt.datetime(year, month, 1)
        last_day = dt.datetime(year, month, calendar.monthrange(year, month)[1]) +  dt.timedelta(days=1)
        call_metas = models.CallMeta.objects.filter(timestamp__gte=first_day, timestamp__lte=last_day).values()
        calls = {}
        for call_meta in call_metas:
            call_id = call_meta["call_id"]
            if call_id in calls:
                calls[call_id][call_meta["rtype"]] = call_meta
            else:
                print(call_id)
                calls[call_id] = { call_meta["rtype"]: call_meta }
        data = []
        for call_id, info in calls.items():
            seconds = int((info[models.CallMeta.RegistryType.END]["timestamp"] - info[models.CallMeta.RegistryType.BEGIN]["timestamp"]).total_seconds())
            h = seconds//3600
            m = (seconds-h*3600)//60
            s = seconds - h*3600 - m*60
            data.append({
                "destination": info[models.CallMeta.RegistryType.BEGIN]["destination"],
                "start_date": info[models.CallMeta.RegistryType.BEGIN]["timestamp"].date(),
                "start_time": info[models.CallMeta.RegistryType.BEGIN]["timestamp"].time(),
                "duration": f"{h}h{m}m{s}s",
                "cost": 0.36+(seconds//60)*0.09
            })
        return Response({
            "phone_number": pk,
            "total": sum([call["cost"] for call in data]),
            "calls": data
        })  
