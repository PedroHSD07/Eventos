from rest_framework import viewsets
from .models import Evento, Participante
from .serializers import EventoSerializer, ParticipanteSerializer

from rest_framework.permissions import IsAuthenticated

class EventoViewSet(viewsets.ModelViewSet):
    queryset = Evento.objects.all()
    serializer_class = EventoSerializer
    permission_classes = [IsAuthenticated]  

class ParticipanteViewSet(viewsets.ModelViewSet):
    queryset = Participante.objects.all()
    serializer_class = ParticipanteSerializer
    permission_classes = [IsAuthenticated]  