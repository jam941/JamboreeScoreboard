from rest_framework import serializers

from backend.models import Troop, Patrol, Scout, Score


class TroopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Troop
        fields = ['url', 'number', 'district', 'council', 'scoutmaster', 'emergency_contact_num', 'patrol_set']
        # zfields = '__all__'


class PatrolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patrol
        fields = '__all__'


class ScoutSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Scout
        fields = '__all__'


class ScoreSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Score
        fields = '__all__'


class ScoreScoutSerializer(serializers.Serializer):
    scout_name = serializers.CharField(source= 'name')
    troop_number = serializers.IntegerField(source='patrol__troop__number')
    patrol_name = serializers.CharField(source='patrol__name')
    score = serializers.IntegerField(source="score__score__sum")

class ScorePatrolSerializer(serializers.Serializer):
    patrol_name = serializers.CharField(source='name')
    total_score = serializers.IntegerField()
