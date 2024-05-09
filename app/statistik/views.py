"""
Views for the statistik APIs.
"""

from rest_framework import viewsets

from core.models import IndikatorBruttoinlandsprodukt
from statistik import serializers

class BruttoinlandsproduktViewSet(viewsets.ModelViewSet):
    """View for manage statistik APIs."""
    http_method_names=['get']
    serializer_class = serializers.BruttoinlandsproduktSerializer
    queryset = IndikatorBruttoinlandsprodukt.objects.all()
    lookup_field = 'eu_code'

class Bruttoinlandsproduktnuts1ViewSet(BruttoinlandsproduktViewSet):
    def get_queryset(self):
        return self.queryset.filter(nuts_1=1)
    
class Bruttoinlandsproduktnuts3ViewSet(BruttoinlandsproduktViewSet):
    def get_queryset(self):
        return self.queryset.filter(nuts_3=3)
    
    
# class Bruttoinlandsproduktnuts1ViewSet(viewsets.ModelViewSet):
#     """View for manage statistik APIs."""
#     http_method_names=['get']
#     serializer_class = serializers.BruttoinlandsproduktSerializer
#     queryset = IndikatorBruttoinlandsprodukt.objects.all()
#     lookup_field = 'eu_code'
#     def get_queryset(self):
#         return self.queryset.filter(nuts_1=1)
    
# class Bruttoinlandsproduktnuts3ViewSet(viewsets.ModelViewSet):
#     """View for manage statistik APIs."""
#     http_method_names=['get']
#     serializer_class = serializers.BruttoinlandsproduktSerializer
#     queryset = IndikatorBruttoinlandsprodukt.objects.all()
#     lookup_field = 'eu_code'
#     def get_queryset(self):
#         return self.queryset.filter(nuts_3=3)

   
