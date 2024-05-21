import requests
import random
from bs4 import BeautifulSoup
import re
import logging

logger = logging.getLogger(__name__)

def fetch_website(url, proxies):
    proxy = random.choice(proxies)
    proxy_dict = {"http": proxy, "https": proxy}
    try:
        response = requests.get(url, proxies=proxy_dict, timeout=10)
        response.raise_for_status()
        logger.info(f"Erfolgreich abgerufen: {url} mit Proxy {proxy}")
        return response.text
    except requests.RequestException as e:
        logger.error(f"Fehler beim Abrufen der Webseite {url} mit Proxy {proxy}: {e}")
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

def extract_contact_info(soup):
    contact_info = {}

    # Adresse
    address = soup.find('address')
    if address:
        contact_info['Adresse'] = address.get_text(strip=True)
    else:
        address_patterns = re.compile(r'\d{1,4}\s\w+\s\w+,?\s?\w*,?\s?\w*')
        address_match = soup.find(string=address_patterns)
        if address_match:
            contact_info['Adresse'] = address_match.strip()

    # Email
    email_patterns = re.compile(r'[\w\.-]+@[\w\.-]+')
    email_match = soup.find(string=email_patterns)
    if email_match:
        contact_info['Email'] = email_match.strip()

    # Telefonnummern
    phone_patterns = re.compile(r'\+?\d[\d -]{8,}\d')
    phone_match = soup.find(string=phone_patterns)
    if phone_match:
        contact_info['Telefon'] = phone_match.strip()

    # Fax
    fax_patterns = re.compile(r'\b[Ff]ax\b[:\s]*\+?\d[\d -]{8,}\d')
    fax_match = soup.find(string=fax_patterns)
    if fax_match:
        contact_info['Fax'] = fax_match.strip()

    # Handy
    mobile_patterns = re.compile(r'\b[Mm]obil\b|\b[Hh]andy\b[:\s]*\+?\d[\d -]{8,}\d')
    mobile_match = soup.find(string=mobile_patterns)
    if mobile_match:
        contact_info['Handy'] = mobile_match.strip()

    # Social Media Accounts
    social_media = {}
    social_links = soup.find_all('a', href=True)
    for link in social_links:
        if any(platform in link['href'] for platform in ['facebook.com', 'twitter.com', 'linkedin.com', 'instagram.com']):
            social_media[link['href']] = link.get_text(strip=True)
    
    if social_media:
        contact_info['Social Netzwerk Accounts'] = ', '.join(social_media.keys())

    return contact_info
