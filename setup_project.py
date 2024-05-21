import os

# Basis-Ordnerstruktur
folders = [
    "InteliLink/data",
    "InteliLink/src",
    "InteliLink/logs",
    "InteliLink/tests"
]

# Leere Dateien
files = [
    "InteliLink/data/domains.txt",
    "InteliLink/data/proxies.txt",
    "InteliLink/data/contacts.csv",
    "InteliLink/src/__init__.py",
    "InteliLink/src/main.py",
    "InteliLink/src/loader.py",
    "InteliLink/src/scraper.py",
    "InteliLink/src/parser.py",
    "InteliLink/src/database.py",
    "InteliLink/tests/__init__.py",
    "InteliLink/tests/test_loader.py",
    "InteliLink/tests/test_scraper.py",
    "InteliLink/tests/test_parser.py",
    "InteliLink/tests/test_database.py",
    "InteliLink/requirements.txt"
]

# Ordner erstellen
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Dateien erstellen
for file in files:
    with open(file, 'w') as f:
        pass

print("Basis-Ordnerstruktur und Dateien wurden erfolgreich erstellt.")
