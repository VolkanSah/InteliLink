import unittest
from loader import load_proxies, load_domains, load_csv_database, save_csv_database
import os

class TestLoader(unittest.TestCase):

    def setUp(self):
        # Temporäre Dateien für Tests
        with open('test_proxies.txt', 'w') as f:
            f.write("192.168.0.1:8080\n192.168.0.2:8080\n")
        
        with open('test_domains.txt', 'w') as f:
            f.write("example.com\nexample.org\n")
        
        with open('test_contacts.csv', 'w', newline='') as f:
            f.write("Name,Adresse,Telefon,Fax,Handy,Email,Webseite,Social Netzwerk Accounts\n")
            f.write("Test Name,Test Adresse,1234567890,0987654321,1234567890,test@example.com,https://www.example.com,\n")
    
    def tearDown(self):
        os.remove('test_proxies.txt')
        os.remove('test_domains.txt')
        os.remove('test_contacts.csv')

    def test_load_proxies(self):
        proxies = load_proxies('test_proxies.txt')
        self.assertEqual(proxies, ['192.168.0.1:8080', '192.168.0.2:8080'])

    def test_load_domains(self):
        domains = load_domains('test_domains.txt')
        self.assertEqual(domains, ['example.com', 'example.org'])

    def test_load_csv_database(self):
        contacts = load_csv_database('test_contacts.csv')
        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0]['Name'], 'Test Name')

    def test_save_csv_database(self):
        contacts = [
            {'Name': 'New Name', 'Adresse': 'New Adresse', 'Telefon': '0987654321', 'Fax': '1234567890', 'Handy': '0987654321', 'Email': 'new@example.com', 'Webseite': 'https://www.new.com', 'Social Netzwerk Accounts': ''}
        ]
        save_csv_database('test_contacts.csv', contacts)
        updated_contacts = load_csv_database('test_contacts.csv')
        self.assertEqual(len(updated_contacts), 1)
        self.assertEqual(updated_contacts[0]['Name'], 'New Name')

if __name__ == '__main__':
    unittest.main()
