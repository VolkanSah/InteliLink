import requests
from bs4 import BeautifulSoup
import logging
import random
from parser import extract_contact_info  # Importiere die neue Funktion

logger = logging.getLogger(__name__)

def fetch_website(url, proxies):
    for attempt in range(3):  # Versuche bis zu 3 Mal, die Webseite abzurufen
        proxy = random.choice(proxies)
        proxy_dict = {"http": proxy, "https": proxy}
        try:
            response = requests.get(url, proxies=proxy_dict, timeout=10)
            response.raise_for_status()
            logger.info(f"Erfolgreich abgerufen: {url} mit Proxy {proxy}")
            return response.text
        except requests.RequestException as e:
            logger.error(f"Fehler beim Abrufen der Webseite {url} mit Proxy {proxy}: {e}")
            proxies.remove(proxy)  # Entferne den fehlerhaften Proxy aus der Liste
    logger.error(f"Fehlgeschlagen, die Webseite {url} nach 3 Versuchen abzurufen")
    return None

def parse_website(html, url, proxies):
    if not html:
        logger.warning(f"Leeres HTML-Dokument für {url}")
        return {}

    soup = BeautifulSoup(html, 'html.parser')
    contact_info = {}

    # Suche nach Impressum- oder Kontakt-Links
    links = soup.find_all('a', href=True)
    for link in links:
        if 'impressum' in link['href'].lower() or 'kontakt' in link['href'].lower():
            contact_page_url = link['href']
            if not contact_page_url.startswith('http'):
                contact_page_url = f"{url.rstrip('/')}/{contact_page_url.lstrip('/')}"
            contact_page_html = fetch_website(contact_page_url, proxies)
            if contact_page_html:
                contact_soup = BeautifulSoup(contact_page_html, 'html.parser')
                contact_info.update(extract_contact_info(contact_soup))
            break

    # Falls keine spezifischen Seiten gefunden, extrahiere Infos aus der Hauptseite
    if not contact_info:
        contact_info.update(extract_contact_info(soup))

    return contact_info
