from rest_framework.response import Response

from countries.models import Country
from rest_framework import viewsets, permissions, generics
from .serializers import *
from django_filters.rest_framework import DjangoFilterBackend


class CountryViewSet(viewsets.ModelViewSet):
    queryset = Country.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = CountrySerializer
    filter_backends = [DjangoFilterBackend]
    filter_fields = ('continent', 'name', 'local_name',)
