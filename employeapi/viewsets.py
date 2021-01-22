from django.db import models
from rest_framework import viewsets
from . import models
from . import serializers

class EmployerViewset(viewsets.ModelViewSet):
    queryset=models.Employer.objects.all()
    serializer_class=serializers.EmployerSerializer