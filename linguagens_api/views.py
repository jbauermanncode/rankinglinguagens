from rest_framework import viewsets
from linguagens_api.models import Linguagem
from linguagens_api.serializer import LinguagemSerializer

class LinguagensViewSet(viewsets.ModelViewSet):
    """Exibindo todas as linguagens"""
    queryset = Linguagem.objects.all()
    serializer_class = LinguagemSerializer

