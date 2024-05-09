"""
Views for the statistik APIs.
"""
from django.apps import apps
from rest_framework import viewsets
from drf_spectacular.utils import extend_schema_view, extend_schema, OpenApiTypes, OpenApiParameter, OpenApiExample
from core.models import IndikatorBruttoinlandsprodukt, IndikatorErwerbstaetige, BaseIndikator
from statistik import serializers

INDICATOR_TYPE_MODEL_MAP = {
    'bruttoinlandsprodukt': 'IndikatorBruttoinlandsprodukt',
    'erwerbtaetige': 'IndikatorErwerbstaetige',
}

bruttoinlandsprodukt_response_schema = {
    'description': 'Serilaizers for Bruttoinlandsprodukt.',
    'type': 'object',
    'properties': {
        'lfd_nr': {'type': 'integer', 'maximum': 2147483647, 'minimum': -2147483648},
        'eu_code': {'type': 'string', 'maxLength': 5},
        'regional_schluessel': {'type': 'string', 'maxLength': 5},
        'land': {'type': 'string', 'maxLength': 2},
        'nuts_1': {'type': 'integer', 'maximum': 2147483647, 'minimum': -2147483648, 'nullable': True},
        'nuts_2': {'type': 'integer', 'maximum': 2147483647, 'minimum': -2147483648, 'nullable': True},
        'nuts_3': {'type': 'integer', 'maximum': 2147483647, 'minimum': -2147483648, 'nullable': True},
        'gebietseinheit': {'type': 'string', 'maxLength': 50},
        'jahr_1992': {'type': 'number', 'format': 'float', 'nullable': True},
        **{f'jahr_{year}': {'type': 'number', 'format': 'float', 'nullable': True} for year in range(1994, 2022)}
    },
}

@extend_schema_view(
    list=extend_schema(
        summary='List of all returned fields',
        parameters=[OpenApiParameter(name='indicator_type', type=str, location=OpenApiParameter.PATH, description='Indicator type (e.g., "bruttoinlandsprodukt", "erwerbtaetige")')],
        responses={200: OpenApiTypes.OBJECT, 200: bruttoinlandsprodukt_response_schema}
    ),
    retrieve=extend_schema(
        summary='List of all returned fields',
        parameters=[OpenApiParameter(name='indicator_type', type=str, location=OpenApiParameter.PATH, description='Indicator type (e.g., "bruttoinlandsprodukt", "erwerbtaetige")')],
        responses={200: OpenApiTypes.OBJECT, 200: bruttoinlandsprodukt_response_schema}
    )
)
class BaseIndikatorViewSet(viewsets.ModelViewSet):
    """Base viewset for managing base indicators."""
    http_method_names = ['get']
    queryset = None  # Placeholder queryset

    def get_queryset(self):
        # Determine the queryset based on the URL or request data
        indicator_type = self.kwargs.get('indicator_type')
        if indicator_type not in INDICATOR_TYPE_MODEL_MAP:
            raise Exception("Invalid indicator type")

         # Get the model name corresponding to the indicator type
        model_name = INDICATOR_TYPE_MODEL_MAP[indicator_type]

        # Get the model class using the model name
        model_class = apps.get_model('core', model_name)

        # Return the queryset for the corresponding model
        return model_class.objects.all()

    def get_serializer_class(self):
        indicator_type = self.kwargs.get('indicator_type')
        print("Indicator Type:", indicator_type)  # Add this line for debugging
        model_name = INDICATOR_TYPE_MODEL_MAP.get(indicator_type)
        print("Model Name:", model_name)  # Add this line for debugging
        if model_name:
            serializer_class = getattr(serializers, model_name + "Serializer")
            return serializer_class
        else:
            print("Model Name not found for indicator type:",
                  indicator_type)  # Add this line for debugging


class BruttoinlandsproduktViewSet(viewsets.ModelViewSet):
    """View for manage statistik APIs."""
    http_method_names=['get']
    serializer_class = serializers.IndikatorBruttoinlandsproduktSerializer
    queryset = IndikatorBruttoinlandsprodukt.objects.all()
    lookup_field = 'eu_code'
    def get_serializer_class(self):
        return IndikatorBruttoinlandsprodukt.get_serializer()

class Bruttoinlandsproduktnuts1ViewSet(BruttoinlandsproduktViewSet):
    def get_queryset(self):
        return self.queryset.filter(nuts_1=1)

class Bruttoinlandsproduktnuts3ViewSet(BruttoinlandsproduktViewSet):
    def get_queryset(self):
        return self.queryset.filter(nuts_3=3)


class Bruttoinlandsproduktnuts1ViewSet(viewsets.ModelViewSet):
    """View for manage statistik APIs."""
    http_method_names=['get']
    serializer_class = serializers.IndikatorBruttoinlandsproduktSerializer
    queryset = IndikatorBruttoinlandsprodukt.objects.all()
    lookup_field = 'eu_code'
    def get_queryset(self):
        return self.queryset.filter(nuts_1=1)

class Bruttoinlandsproduktnuts3ViewSet(viewsets.ModelViewSet):
    """View for manage statistik APIs."""
    http_method_names=['get']
    serializer_class = serializers.IndikatorBruttoinlandsproduktSerializer
    queryset = IndikatorBruttoinlandsprodukt.objects.all()
    lookup_field = 'eu_code'
    def get_queryset(self):
        return self.queryset.filter(nuts_3=3)
