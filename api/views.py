from rest_framework import viewsets
from .serializers import SiteSerializer
from web.models import Site


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.filter(status=200).order_by('-created_date')
    serializer_class = SiteSerializer
