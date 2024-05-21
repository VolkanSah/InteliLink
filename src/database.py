import sqlite3
import logging

logger = logging.getLogger(__name__)

def create_connection(db_file):
    try:
        conn = sqlite3.connect(db_file)
        logger.info(f"Verbindung zur SQLite-Datenbank hergestellt: {db_file}")
        return conn
    except sqlite3.Error as e:
        logger.error(f"Fehler beim Herstellen der Verbindung zur SQLite-Datenbank: {e}")
        return None

def create_table(conn):
    try:
        sql_create_contacts_table = """CREATE TABLE IF NOT EXISTS contacts (
                                            id integer PRIMARY KEY,
                                            name text NOT NULL,
                                            address text,
                                            phone text,
                                            fax text,
                                            mobile text,
                                            email text,
                                            website text UNIQUE,
                                            social_media text
                                        );"""
        conn.execute(sql_create_contacts_table)
        logger.info("Tabelle 'contacts' erfolgreich erstellt oder existiert bereits.")
    except sqlite3.Error as e:
        logger.error(f"Fehler beim Erstellen der Tabelle: {e}")

def insert_contact(conn, contact):
    sql = '''INSERT OR IGNORE INTO contacts(name, address, phone, fax, mobile, email, website, social_media)
             VALUES(?,?,?,?,?,?,?,?)'''
    cur = conn.cursor()
    cur.execute(sql, (contact['Name'], contact['Adresse'], contact['Telefon'], contact['Fax'],
                      contact['Handy'], contact['Email'], contact['Webseite'], contact['Social Netzwerk Accounts']))
    conn.commit()
    logger.info(f"Kontakt hinzugefügt: {contact['Name']}")

def fetch_all_contacts(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    rows = cur.fetchall()
    contacts = []
    for row in rows:
        contact = {
            'Name': row[1],
            'Adresse': row[2],
            'Telefon': row[3],
            'Fax': row[4],
            'Handy': row[5],
            'Email': row[6],
            'Webseite': row[7],
            'Social Netzwerk Accounts': row[8]
        }
        contacts.append(contact)
    return contacts
