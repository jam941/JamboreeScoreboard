from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from backend.models import Troop, Patrol, Scout, Score
from backend.serializers import TroopSerializer, PatrolSerializer, ScoutSerializer, ScoreSerializer


class TroopViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Troop.objects.all().order_by('number')
    serializer_class = TroopSerializer
    permission_classes = [permissions.AllowAny]


class PatrolViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Patrol.objects.all()
    serializer_class = PatrolSerializer
    permission_classes = [permissions.AllowAny]


class ScoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Scout.objects.all()
    serializer_class = ScoutSerializer
    permission_classes = [permissions.AllowAny]

class ScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [permissions.AllowAny]
