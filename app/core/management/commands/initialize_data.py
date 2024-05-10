from django.core.management.base import BaseCommand
from core.models import MetaDaten


class Command(BaseCommand):
    def initialize_metadata(self):
        titel = "Bruttoinlandsprodukt, Bruttowertschöpfung in den kreisfreien Städten und Landkreisen der Bundesrepublik Deutschland 1992 und 1994 bis 2021\n"\
                "Reihe 2, Kreisergebnisse Band 1"

        herausgegeben_vom = "Arbeitskreis „Volkswirtschaftliche Gesamtrechnungen der Länder“ im Auftrag der Statistischen Ämter der 16 Bundesländer, des Statistischen Bundesamtes und des Statistischen Amtes Wirtschaft und Kultur der Landeshauptstadt Stuttgart."

        erscheinungs_folge = 'jährlich'
        erschienen_im = 'Juli 2023'
        herstellung_und_redaktion = """Statistisches Landesamt Baden-Württemberg
Böblinger Straße 68
70199 Stuttgart
Telefon: 0711 641 - 0
Fax: 0711 641 - 2440
E-Mail: poststelle@stala.bwl.de
Internet: www.statistik-bw.de"""

        berechnungsstand_information = """Berechnungsstand des Statistischen Bundesamtes: August 2022
Korrektur der Einwohnerzahlen 2020 bei den Kreisergebnissen für Thüringen.
Korrektur am 14. Dezember 2023: Kreisergebnisse zu BIP und BWS für Baden-Württemberg, Jahre 2018 bis 
2021 (Tabellen 1.1, 1.2, 1.3 und 2.1, 2.1.1, 2.1.2, 2.2, 2.3, 2.3.1, 2.3.1.1, 2.4, 2.4.1, 2.4.2, 2.4.3, 4, 6 und 8).
Korrektur am 12. März 2024: Kreisergebnisse „Erwerbstätige“, „Bruttoinlandsprodukt in jeweiligen Preisen je
erwerbstätige Person (Inlandskonzept)“, „Standard-Arbeitsvolumen der Erwerbstätigen (Inlandskonzept)“
und „Bruttoinlandsprodukt in jeweiligen Preisen je Arbeitsstunde der Erwerbstätigen (Inlandskonzept)“ für 
Nordrhein-Westfalen, Jahre 2018 bis 2021 (Tabellen 3.1 bis 3.4.3, 4, 7.1 bis 7.4.3 und 8).
[Revision 2019/ESVG 2010/WZ 2008]"""
        if MetaDaten.objects.count() == 0 :
            metadata = MetaDaten(
                titel=titel,
                herausgegeben_vom=herausgegeben_vom,
                herstellung_und_redaktion=herstellung_und_redaktion,
                erscheinungs_folge=erscheinungs_folge,
                erschienen_im=erschienen_im,
                berechnungsstand_information=berechnungsstand_information
            )
            metadata.save()
    def handle(self, *args, **options):
        self.initialize_metadata()
