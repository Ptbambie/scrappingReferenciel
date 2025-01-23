import os
import sys
sys.path.append(os.path.join(os.path.split(__file__)[0], "dependencies"))

import json
import re
import requests 


from conf import Conf

class BienIci:
    '''Class for scraping BienIci real estate ads.'''

    def __init__(self, department):
        self.conf = Conf()
        self.conf.scrap_infos['department'] = department
        # Accéder aux informations nécessaires
        self.source = self.conf.scrap_infos['source']
        self.site_url = self.conf.scrap_infos['site_url']
        self.api_url = self.conf.scrap_infos['api_url']
        self.payload = json.loads(self.conf.scrap_infos['payload'])  # Charger le JSON
        self.payload['filters']['zoneIds'] = [department]  # Ajouter le département au filtre
        self.header = {
            'Accept': 'application/json',
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }

    # Fonction pour scraper une page
    def scrape_page(self, page):
        self.payload['filters']['page'] = page  # Met à jour le numéro de la page
        response = requests.get(
            self.api_url,
            headers=self.header,
            params={'filters': json.dumps(self.payload['filters'])}
        )
        if response.status_code == 200:
            return response.json().get('realEstateAds', [])
        else:
            print(f"Erreur lors de la requête: {response.status_code}")
            return []

    # Fonction principale pour scraper plusieurs pages
    def scrape_ads(self, pages=5):
        ads = []
        for page in range(1, pages + 1):
            print(f"Scraping page {page}...")
            ads_on_page = self.scrape_page(page)
            if not ads_on_page:  # Arrête si aucune annonce n'est récupérée
                print("Pas d'annonces trouvées, arrêt du scraping.")
                break
            ads.extend(ads_on_page)
        print(f"Total d'annonces récupérées : {len(ads)}")
        return ads


# Exemple d'utilisation
if __name__ == "__main__":
    # Définir le département à scraper (exemple : "75056" pour Paris)
    scraper = BienIci(department="75056")
    ads = scraper.scrape_ads(pages=5)  # Scraper les 5 premières pages
    print(ads)  # Afficher les annonces récupérées