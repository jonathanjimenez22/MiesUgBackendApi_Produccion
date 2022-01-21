from rest_framework import serializers

from entrepreneur.models import Bond


class BonoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bond
        fields = '__all__'

class BoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bond
        fields = ('entrepreneur')