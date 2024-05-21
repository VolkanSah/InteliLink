Zusammenfassung des Vorhabens für InteliLink
Projektziel

Einen AI-gesteuerten Webscraper namens InteliLink erstellen, der öffentlich zugängliche Webseiten aus einer Domainliste überprüft, Impressum- und Kontaktdaten extrahiert und diese mit einer CSV-Datenbank abgleicht. Falls die Kontaktdaten nicht in der Datenbank vorhanden sind, werden sie hinzugefügt.
Datenquellen

    Domainliste: Eine Textdatei mit zu überprüfenden Domains.
    Proxy-Liste: Eine Textdatei mit Proxies im Format ip:port.
    CSV-Datenbank: Eine CSV-Datei mit bestehenden Kontaktdaten (Spalten: Name, Adresse, Telefon, Fax, Handy, Email, Webseite, Social Netzwerk Accounts).

Funktionalitäten

    Proxies laden: Proxies aus einer Datei laden.
    Domains laden: Domains aus einer Datei laden.
    CSV-Datenbank laden und speichern: CSV-Datei lesen und aktualisieren.
    Webseite abrufen: Webseite über einen zufällig ausgewählten Proxy abrufen.
    Daten extrahieren: Impressum und Kontaktinformationen aus dem HTML-Inhalt extrahieren.
    Daten abgleichen: Neue Daten mit bestehenden Daten in der CSV-Datenbank abgleichen.
    Neue Daten speichern: Neue Daten in die CSV-Datenbank einfügen.

Muster und Kriterien für die Datenerkennung

    Impressum und Kontaktinformationen befinden sich häufig im Footer, im Impressum oder im Kontaktbereich der Webseite.

Fehlerbehandlung und Wiederholungsversuche

    Fehlende Informationen: Falls Informationen nicht gefunden werden, wird n.A. (nicht angegeben) in die CSV-Datei eingetragen.
    Soziale Netzwerke: Nur Einträge machen, wenn Informationen vorhanden sind.

Workflow

    Initialisierung:
        Lade Proxies und Domains aus den entsprechenden Dateien.
        Lade die bestehenden Kontaktdaten aus der CSV-Datenbank.
    Webseitenprüfung:
        Für jede Domain:
            Wähle einen zufälligen Proxy aus.
            Rufe die Webseite ab.
            Extrahiere Impressum und Kontaktdaten.
    Datenabgleich:
        Vergleiche die extrahierten Daten mit den bestehenden Daten in der CSV-Datenbank.
        Füge neue Daten hinzu, falls diese nicht vorhanden sind.
    Speichern:
        Speichere die aktualisierte CSV-Datenbank.

Nächste Schritte

    Implementiere die Funktionen zum Laden der Proxies und Domains.
    Implementiere die Funktionen zum Laden und Speichern der CSV-Datenbank.
    Entwickle eine Methode zum Abrufen und Parsen von Webseiteninhalten.
    Entwickle eine AI-Komponente zur Erkennung und Extraktion von Impressum- und Kontaktdaten.
    Implementiere die Logik zum Abgleich und Speichern der Daten.


