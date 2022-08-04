from rest_framework import serializers
from linguagens_api.models import Linguagem

class LinguagemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Linguagem
        fields = '__all__'