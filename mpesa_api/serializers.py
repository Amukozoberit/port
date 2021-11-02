from mpesa_api.models import LNmpesaOnline
from rest_framework import serializers

class LNMOnlineSerializer(serializers.ModelSerializer):
    class Meta:
        model = LNmpesaOnline
        fields = '__all__'