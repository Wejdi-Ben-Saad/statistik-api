"""
Serializers for statistik APIs
"""

from rest_framework import serializers

from core.models import IndikatorBruttoinlandsprodukt, IndikatorErwerbstaetige


class IndikatorBruttoinlandsproduktSerializer(serializers.ModelSerializer):
    """Serilaizers for Bruttoinlandsprodukt."""
    class Meta:
        model = IndikatorBruttoinlandsprodukt
        fields = '__all__'

class IndikatorErwerbstaetigeSerializer(serializers.ModelSerializer):
    """Serilaizers for Erwerbstaetige."""
    class Meta:
        model = IndikatorErwerbstaetige
        fields = '__all__'
        



