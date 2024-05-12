"""
Views for the statistik APIs.
"""

from rest_framework import viewsets
from core.models import IndikatorBruttoinlandsprodukt,IndikatorErwerbstaetige, MetaDaten
from statistik import serializers



#Bruttoinlandsprodukt indicator Views
class BruttoinlandsproduktViewSet(viewsets.ModelViewSet):
    """Bruftoinlandsprodukt in jeweiligen Preisen  APIs."""
    http_method_names=['get']
    serializer_class = serializers.IndikatorBruttoinlandsproduktSerializer
    queryset = IndikatorBruttoinlandsprodukt.objects.all()
    

class BruttoinlandsproduktNuts1ViewSet(BruttoinlandsproduktViewSet):
    """Bruftoinlandsprodukt in jeweiligen Preisen Auf Bundeslandebene (NUTS 1)"""
    def get_queryset(self):
        return self.queryset.filter(nuts_1=1).order_by("lfd_nr")

class BruttoinlandsproduktNuts3ViewSet(BruttoinlandsproduktViewSet):
    """Bruftoinlandsprodukt in jeweiligen Preisen Auf Kreisebene (NUTS 3)"""
    def get_queryset(self):
        return self.queryset.filter(nuts_3=3).order_by("lfd_nr")

#Erwerbstaetige indicator Views    
class IndikatorErwerbstaetigeViewSet(viewsets.ModelViewSet):
    """Erwerbstäfige (Inlandskonzept) APIs."""
    http_method_names=['get']
    serializer_class = serializers.IndikatorErwerbstaetigeSerializer
    queryset = IndikatorErwerbstaetige.objects.all()
    

class IndikatorErwerbstaetigeNuts1ViewSet(IndikatorErwerbstaetigeViewSet):
    """Erwerbstäfige (Inlandskonzept) Auf Bundeslandebene (NUTS 1)"""
    def get_queryset(self):
        return self.queryset.filter(nuts_1=1).order_by("lfd_nr")

class IndikatorErwerbstaetigeNuts3ViewSet(IndikatorErwerbstaetigeViewSet):
    """Erwerbstäfige (Inlandskonzept) Auf Kreisebene (NUTS 3)"""
    def get_queryset(self):
        return self.queryset.filter(nuts_3=3).order_by("lfd_nr")
    
### Metadaten view

class MetaDatenViewSet(viewsets.ModelViewSet):
    """Metadaten zur Quelle"""
    http_method_names=['get']
    serializer_class = serializers.MetaDatenSerializer
    queryset = MetaDaten.objects.all()



