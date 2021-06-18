from rest_framework import viewsets
from rest_framework import permissions
from .serializers import EndpointSerializer, VerticalSerializer, SectionSerializer
from .models import Vertical, Section, Constraint, Parameter, Endpoint


class VerticalsViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Vertical.objects.all()
    serializer_class = VerticalSerializer
