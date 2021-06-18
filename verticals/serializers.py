from .models import Vertical, Section, Constraint, Parameter, Endpoint
from rest_framework import serializers

class ConstraintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Constraint
        fields = ['name', 'description', 'value']

class ParameterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Parameter
        fields = ['name', 'description', 'optional',
                  'accepted_values']

class EndpointSerializer(serializers.ModelSerializer):
    parameters = ParameterSerializer(read_only=True, many=True)
    constraints = ConstraintSerializer(read_only=True, many=True)

    class Meta:
        model = Endpoint
        fields = ['name', 'base_url', 'parameters', 'constraints']

class SectionSerializer(serializers.ModelSerializer):

    endpoints = EndpointSerializer(read_only=True, many=True)

    class Meta:
        model = Section
        fields = ['name', 'endpoints']

class VerticalSerializer(serializers.ModelSerializer):

    sections = SectionSerializer(read_only=True, many=True)

    class Meta:
        model = Vertical
        fields = ('name', 'sections')
