#!/usr/bin/env python
# -*- coding: utf-8 -*-

import json


class Conf():
    '''class for internal configuration of scrap bienIci'''
    def __init__(self, **kwargs):
        self.scrap_infos = kwargs.get('scrap_infos', {
            'source': 'bienIci',
            'site_url': 'https://www.bienici.com',
            'api_url': 'https://www.bienici.com/realEstateAds.json',
            'payload': json.dumps({
                "filters": {
                    "page": 1,
                    "size": 50,  # Nombre d'annonces par page
                    "propertyType": ["apartment", "house"],  # Types de biens
                    "minPrice": 50000,  # Prix minimum
                    "maxPrice": 1000000,  # Prix maximum
                    "zoneIds": ["75056"]  # Code pour Paris, adapter si nécessaire
                }
            })
        })

        # Configuration des logs (si nécessaire)
        self.log_config = kwargs.get('log_config', {
            'log_level': 'DEBUG',
            'log_file': './output.log'  # Nom du fichier log
        })

        # Configuration des proxies (si nécessaire)
        self.proxies = kwargs.get('proxies', {
            'enabled': False,
            'list': []  # Ajouter une liste de proxies si activé
        })


# BASE_URL = "https://www.bienici.com/realEstateAds.json"
# HEADERS = {
#     'Accept': 'application/json',
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
# }

# # Paramètres par défaut (exemple)
# DEFAULT_PARAMS = {
#     "filters": json.dumps({
#         "page": 1,
#         "size": 50,  # Nombre d'annonces par page
#         "propertyType": ["apartment", "house"],  # Types de biens
#         "minPrice": 50000,  # Prix minimum
#         "maxPrice": 1000000,  # Prix maximum
#         "zoneIds": ["75056"],  # Paris (Zone Bien’ici)
#     })
# }
