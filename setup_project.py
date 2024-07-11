import os

# Basis-Ordnerstruktur
folders = [
    "InteliLink/tests"
]

# Leere Dateien
files = [
    "data/domains.txt",
    "data/proxies.txt",
    "data/contacts.csv",
    "tests/__init__.py"

]

# Ordner erstellen
for folder in folders:
    os.makedirs(folder, exist_ok=True)

# Dateien erstellen
for file in files:
    with open(file, 'w') as f:
        pass

print("Basis-Ordnerstruktur und Dateien wurden erfolgreich erstellt.")
