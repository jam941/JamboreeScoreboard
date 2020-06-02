from django.contrib.auth.models import User
from rest_framework import viewsets
from rest_framework import permissions

from backend.models import Troop, Patrol, Scout, Score
from backend.serializers import TroopSerializer, PatrolSerializer, ScoutSerializer, ScoreSerializer, \
    ScoreScoutSerializer, ScorePatrolSerializer, UserSerializer
from django.db.models import Sum


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
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ScoutViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Scout.objects.all()
    serializer_class = ScoutSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]


class ScoreViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Score.objects.all()
    serializer_class = ScoreSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    def get_serializer_context(self):
        return {'request': self.request}

class ScoutScoreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Scout.objects.all().values(
        "name",
        "patrol__name",
        "patrol__troop__number"
    ).annotate(
        Sum("score__score")
    )
    serializer_class = ScoreScoutSerializer
    permission_classes = [permissions.AllowAny]

class PatrolScoreViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Patrol.objects.all()
    serializer_class = ScorePatrolSerializer
    permission_classes = [permissions.AllowAny]

class UserViewSet(viewsets.ReadOnlyModelViewSet):
    #queryset = User.objects.all()
    def get_queryset(self):
        return User.objects.filter(id=self.request.user.id)
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]