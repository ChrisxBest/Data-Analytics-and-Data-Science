import pandas as pd
import numpy as np # Wird für schnelle zufällige Zahlen und Auswahl benötigt
import random # Für zufällige Auswahl

# --- 1. Konfiguration ---
NUM_RECORDS = 5000  # Wir erstellen 5000 Zeilen

# Listen mit möglichen Werten
produkte = ['Laptop', 'Smartphone', 'Tablet', 'Smartwatch', 'Kopfhörer', 'Tastatur', 'Monitor']
regionen = ['Nord', 'Süd', 'Ost', 'West']
bewertungen = [1, 2, 3, 4, 5]

# --- 2. Daten erzeugen ---
data = {
    # 5000 zufällige Produkte aus der Liste 'produkte'
    'Produkt': np.random.choice(produkte, NUM_RECORDS), 
    
    # 5000 zufällige Regionen aus der Liste 'regionen'
    'Region': np.random.choice(regionen, NUM_RECORDS),
    
    # Zufällige Verkaufszahlen zwischen 50 und 500
    'Verkaufszahl': np.random.randint(50, 501, NUM_RECORDS),
    
    # Zufälliger Einzelpreis (Float-Werte) zwischen 100.00 und 1500.00
    'Einzelpreis': np.round(np.random.uniform(100, 1500), 2),
    
    # Zufällige Kundenbewertung (Integer)
    'Kundenbewertung': np.random.choice(bewertungen, NUM_RECORDS, p=[0.05, 0.1, 0.25, 0.3, 0.3]),
    
    # Zufällige Kaufdaten innerhalb des letzten Jahres
    'Kaufdatum': pd.to_datetime(pd.to_datetime('today') - pd.to_timedelta(np.random.randint(0, 365, NUM_RECORDS), unit='D'))
}

"""# 3. DataFrame erstellen
df = pd.DataFrame(data)

# --- 4. Zusätzliche Spalte für den Gesamtumsatz berechnen ---
df['Gesamtumsatz'] = df['Verkaufszahl'] * df['Einzelpreis']
df['Gesamtumsatz'] = df['Gesamtumsatz'].round(2)


# 5. DataFrame anzeigen
print(f"DataFrame erstellt mit {len(df)} Zeilen und {len(df.columns)} Spalten.")
print("-" * 30)

# Zeige die ersten 5 Zeilen an (df.head())
print(df.head(100))"""
