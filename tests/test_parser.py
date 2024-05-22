import unittest
from parser import extract_contact_info
from bs4 import BeautifulSoup

class TestParser(unittest.TestCase):

    def test_extract_contact_info(self):
        html_content = '''
        <html>
            <body>
                <address>1234 Test St, Test City, Test Country</address>
                <a href="mailto:test@example.com">test@example.com</a>
                <a href="tel:+123456789">+123456789</a>
                <div>Fax: +987654321</div>
                <div>Mobil: +192837465</div>
                <a href="https://www.facebook.com/test">Facebook</a>
                <a href="https://www.twitter.com/test">Twitter</a>
                <a href="https://www.linkedin.com/in/test">LinkedIn</a>
            </body>
        </html>
        '''
        soup = BeautifulSoup(html_content, 'html.parser')
        contact_info = extract_contact_info(soup)

        self.assertEqual(contact_info['Adresse'], '1234 Test St, Test City, Test Country')
        self.assertEqual(contact_info['Email'], 'test@example.com')
        self.assertEqual(contact_info['Telefon'], '+123456789')
        self.assertEqual(contact_info['Fax'], 'Fax: +987654321')
        self.assertEqual(contact_info['Handy'], 'Mobil: +192837465')
        self.assertIn('https://www.facebook.com/test', contact_info['Social Netzwerk Accounts'])
        self.assertIn('https://www.twitter.com/test', contact_info['Social Netzwerk Accounts'])
        self.assertIn('https://www.linkedin.com/in/test', contact_info['Social Netzwerk Accounts'])

if __name__ == '__main__':
    unittest.main()
