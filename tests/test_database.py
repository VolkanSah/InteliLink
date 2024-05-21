import unittest
import sqlite3
from database import create_connection, create_table, insert_contact, fetch_all_contacts

class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.conn = create_connection(':memory:')
        create_table(self.conn)

    def tearDown(self):
        self.conn.close()

    def test_insert_and_fetch_contact(self):
        contact = {
            'Name': 'Test Name',
            'Adresse': 'Test Adresse',
            'Telefon': '1234567890',
            'Fax': '0987654321',
            'Handy': '1234567890',
            'Email': 'test@example.com',
            'Webseite': 'https://www.example.com',
            'Social Netzwerk Accounts': 'https://www.twitter.com/test'
        }
        insert_contact(self.conn, contact)
        contacts = fetch_all_contacts(self.conn)
        self.assertEqual(len(contacts), 1)
        self.assertEqual(contacts[0]['Name'], 'Test Name')

if __name__ == '__main__':
    unittest.main()
