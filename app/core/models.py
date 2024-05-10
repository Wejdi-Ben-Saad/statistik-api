"""
Database models.
"""
from django.db import models  
from rest_framework import serializers



class BaseIndikator(models.Model):
    """Base indicator for similar data structure"""

    lfd_nr = models.IntegerField(primary_key=True)
    eu_code = models.CharField(max_length=5)
    regional_schluessel = models.CharField(max_length=5)
    land = models.CharField(max_length=2)
    nuts_1 = models.IntegerField(null=True)
    nuts_2 = models.IntegerField(null=True)
    nuts_3 = models.IntegerField(null=True)
    gebietseinheit = models.CharField(max_length=50)

    class Meta:
        abstract = True  # Declare the base class as abstract to prevent Django from creating a table for it


class IndikatorBruttoinlandsprodukt (BaseIndikator):
    """Bruttoinlandsprodukt in jeweiligen Preisen"""
    jahr_1992 = models.BigIntegerField(null=True)
    jahre_fields = {f'jahr_{year}': models.BigIntegerField(
        null=True) for year in range(1994, 2022)}
    # Use dictionary unpacking to define fields in the class
    locals().update(jahre_fields)
    class Meta:
        # Define the table name for the Bruttoinlandsprodukt indicator
        db_table = 'indikator_bruttoinlandsprodukt'

    def __str__(self):
        return self.Meta.db_table


class IndikatorErwerbstaetige(BaseIndikator):
    """Erwerbstätige (Inlandskonzept)"""
    jahr_1992 = models.FloatField(null=True)
    jahre_fields = {f'jahr_{year}': models.FloatField(
        null=True) for year in range(1994, 2022)}
    # Use dictionary unpacking to define fields in the class
    locals().update(jahre_fields)
    class Meta:
        # Define the table name for the Erwerbstätige indicator
        db_table = 'indikator_erwerbstaetige'

    def __str__(self):
        return self.Meta.db_table
    
class MetaDaten(models.Model):
    """Metadaten zur Quelle"""
    titel = models.TextField()
    herausgegeben_vom = models.TextField()
    herstellung_und_redaktion = models.TextField()
    erscheinungs_folge = models.CharField(max_length=10, default = 'jährlich')
    erschienen_im = models.CharField(max_length=10)
    berechnungsstand_information = models.TextField()


