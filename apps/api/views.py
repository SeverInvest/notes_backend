from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet

from apps.memory_card.models import Result
from apps.api.serializers import ResultSerializer


class ResultViewSet(ModelViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer
