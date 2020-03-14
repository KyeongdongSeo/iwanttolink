from rest_framework import viewsets
from rest_framework import permissions
from django.db.models import Q
from .serializers import SiteSerializer
from web.models import Site


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.filter(status=200).order_by('-priority', '?')
    serializer_class = SiteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
