import requests
from bs4 import BeautifulSoup
import logging

logger = logging.getLogger(__name__)

def fetch_linkedin_profile(company_name):
    search_url = f"https://www.linkedin.com/company/{company_name}"
    try:
        response = requests.get(search_url)
        response.raise_for_status()
        logger.info(f"Erfolgreich abgerufen: {search_url}")
        return response.text
    except requests.RequestException as e:
        logger.error(f"Fehler beim Abrufen der LinkedIn-Seite {search_url}: {e}")
        return None

def parse_linkedin_profile(html):
    soup = BeautifulSoup(html, 'html.parser')
    contact_info = {}

    # Beispielhafte Extraktion von Kontaktdaten
    company_name = soup.find('h1', class_='org-top-card-summary__title')
    if company_name:
        contact_info['Name'] = company_name.get_text(strip=True)

    website = soup.find('a', class_='org-top-card-summary__website')
    if website:
        contact_info['Webseite'] = website['href']

    return contact_info
