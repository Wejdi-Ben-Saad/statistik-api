from django.core.management.base import BaseCommand
from core.models import MetaDaten, IndikatorErwerbstaetige, IndikatorBruttoinlandsprodukt
from django.db import transaction
import pandas as pd
import numpy as np
import json


class Command(BaseCommand):
    def initialize_indicator_data(self, indicator_model_class, csv_file_path):
        """initialize indicator data Assuming the CSV file has columns that match 
        the model fields and . is the decimal separator"""
        fields = indicator_model_class._meta.get_fields()
        # Extract field names
        field_names = [field.name for field in fields]
        # make sure the data is not already imported
        if indicator_model_class.objects.count() == 0:
            df = pd.read_csv(
                csv_file_path, delimiter=',', names=field_names)

            # Function to strip spaces and convert to appropriate type
            def clean_and_convert(x):
                if isinstance(x, str):
                    x = x.replace(' ', '')
                    if x == '.':
                        return None
                    elif '.' in x:
                        return float(x)
                    else:
                        return int(x)
                return x

            # Specify columns to convert to numeric
            columns_to_convert = ['jahr_1992'] + \
                [f'jahr_{year}' for year in range(1994, 2022)]

            # Apply the cleaning function to specified columns
            df[columns_to_convert] = df[columns_to_convert].map(
                clean_and_convert)
            # Convert pandas nan  to None
            df = df.replace(np.nan, None)
            data = df.to_dict(orient='records')

            with transaction.atomic():
                # Iterate over the data list and insert row by row
                for row in data:
                    indicator_model_class.objects.create(**row)

    def initialize_metadata(self, impressum_file_path):
        with open(impressum_file_path, "r", encoding="utf-8") as impressum_file:
            impressum_data = json.load(impressum_file)
        if MetaDaten.objects.count() == 0:
            metadata = MetaDaten(
                titel=impressum_data['titel'],
                herausgegeben_vom=impressum_data['herausgegeben_vom'],
                erscheinungs_folge=impressum_data['erscheinungs_folge'],
                erschienen_im=impressum_data['erschienen_im'],
                berechnungsstand_information=impressum_data['berechnungsstand_information']
            )
            metadata.save()

    def handle(self, *args, **options):
        self.initialize_indicator_data(
            IndikatorBruttoinlandsprodukt, './data/bruttoinlandsprodukt.csv')
        self.initialize_indicator_data(
            IndikatorErwerbstaetige, './data/erwerbtaetige.csv')
        self.initialize_metadata('./data/impressum.json')
