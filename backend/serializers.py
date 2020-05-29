from rest_framework import serializers
from rest_framework.exceptions import ValidationError

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
        read_only_fields = ["submit_user"]

    def validate(self, attrs):
        attrs = super().validate(attrs)

        if (attrs.get("scout") is None and attrs.get("patrol") is None):
            raise ValidationError("'scout' or 'patrol' must be provided")

        if (attrs.get("scout") is not None and attrs.get("patrol") is not None):
            raise ValidationError("'scout' and 'patrol' cannot both be provided")
        return attrs

    def create(self, validated_data):
        validated_data['submit_user'] = self.context.get('request').user.username
        return super().create(validated_data)


class ScoreScoutSerializer(serializers.Serializer):
    scout_name = serializers.CharField(source='name')
    troop_number = serializers.IntegerField(source='patrol__troop__number')
    patrol_name = serializers.CharField(source='patrol__name')
    score = serializers.IntegerField(source="score__score__sum")


class ScorePatrolSerializer(serializers.Serializer):
    patrol_name = serializers.CharField(source='name')
    total_score = serializers.IntegerField()
