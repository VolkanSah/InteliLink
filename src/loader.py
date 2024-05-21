import csv

def load_proxies(file_path):
    proxies = []
    with open(file_path, 'r') as file:
        for line in file:
            proxies.append(line.strip())
    return proxies

def load_domains(file_path):
    domains = []
    with open(file_path, 'r') as file:
        for line in file:
            domains.append(line.strip())
    return domains

def load_csv_database(file_path):
    contacts = []
    with open(file_path, 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            contacts.append(row)
    return contacts

def save_csv_database(file_path, contacts):
    with open(file_path, 'w', newline='') as file:
        fieldnames = ['Name', 'Adresse', 'Telefon', 'Fax', 'Handy', 'Email', 'Webseite', 'Social Netzwerk Accounts']
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(contacts)
