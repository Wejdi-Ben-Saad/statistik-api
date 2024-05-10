"""
Serializers for statistik APIs
"""

from rest_framework import serializers

from core.models import IndikatorBruttoinlandsprodukt, IndikatorErwerbstaetige, MetaDaten


class IndikatorBruttoinlandsproduktSerializer(serializers.ModelSerializer):
    """Serilaizer for Bruttoinlandsprodukt Indicator."""
    class Meta:
        model = IndikatorBruttoinlandsprodukt
        fields = '__all__'

class IndikatorErwerbstaetigeSerializer(serializers.ModelSerializer):
    """Serilaizer for Erwerbstaetige Indicator."""
    class Meta:
        model = IndikatorErwerbstaetige
        fields = '__all__'

class MetaDatenSerializer(serializers.ModelSerializer):
    """Serilaizer for Erwerbstaetige Indicator."""
    class Meta:
        model = MetaDaten
        fields = '__all__'
        
        



