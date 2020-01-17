from rest_framework import serializers
from .models import LoggingDatabase


class LoggingSerializer(serializers.ModelSerializer):
    class Meta:
        model = LoggingDatabase
        fields = '__all__'
