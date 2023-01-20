from rest_framework import serializers, viewsets
from Website.models import Temperature

class DhtSerialize(serializers.ModelSerializer):
    class Meta :
        model = Temperature
        fields = ['id', 'temp', 'dt']
