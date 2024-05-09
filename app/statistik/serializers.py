"""
Serializers for statistik APIs
"""

from rest_framework import serializers

from core.models import IndikatorBruttoinlandsprodukt


class BruttoinlandsproduktSerializer(serializers.ModelSerializer):
    """Serilaizers for Bruttoinlandsprodukt."""
    class Meta:
        model = IndikatorBruttoinlandsprodukt
        fields = '__all__'
        



