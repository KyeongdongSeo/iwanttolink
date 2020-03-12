from rest_framework import serializers
from web.models import Site


class SiteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Site
        fields = ('pk', 'name', 'url', 'status',)
