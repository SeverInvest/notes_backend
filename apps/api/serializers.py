from rest_framework.serializers import ModelSerializer

from apps.memory_card.models import Result


class ResultSerializer(ModelSerializer):
    class Meta:

        model = Result
        fields = ['id', 'score', 'user', 'created_at', 'seconds']

