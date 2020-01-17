from rest_framework.response import Response
from .serializers import LoggingSerializer
from .models import LoggingDatabase
from rest_framework import viewsets, permissions, generics
from django_filters.rest_framework import DjangoFilterBackend


class LoggingViewSet(viewsets.ModelViewSet):
    queryset = LoggingDatabase.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = LoggingSerializer
    pagination_class = None
