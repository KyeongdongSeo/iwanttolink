from rest_framework import status
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.views import APIView
from rest_framework.response import Response
from ipware.ip import get_ip
from .serializers import SiteSerializer, LogSerializer
from web.models import Site, Log


class SiteViewSet(viewsets.ModelViewSet):
    queryset = Site.objects.filter(status=200).order_by('-priority', '?')
    serializer_class = SiteSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)


class LogView(APIView):
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def get(self, request, format=None):
        logs = Log.objects.all()
        serializer = LogSerializer(logs, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        site_pk = request.data.get('site_pk')
        row_pk = request.data.get('row_pk')
        ip = get_ip(request)
        data = {'site': site_pk, 'row': row_pk, 'ip': ip}
        serializer = LogSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
