
from rest_framework import serializers

from backend.models import Troop, Patrol


class TroopSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Troop
        fields = ['url', 'number', 'district', 'council', 'scoutmaster', 'emergency_contact_num','patrol_set']
        #zfields = '__all__'

class PatrolSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Patrol
        fields = '__all__'
