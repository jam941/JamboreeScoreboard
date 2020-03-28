from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions

from backend.models import Troop, Patrol
from backend.serializers import TroopSerializer, PatrolSerializer


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
