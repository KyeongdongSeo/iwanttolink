from django.shortcuts import get_object_or_404
from rest_framework import serializers
from web.models import Site, Log


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ('pk', 'name', 'url', 'status', 'priority',)


class LogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Log
        fields = ('pk', 'site', 'row', 'ip', 'click_date')
