import os
import re
import matplotlib.pyplot as plt
import pandas as pd
from visualisierung import batch_plot_slider, batch_plot_single_choice, batch_plot_multiple_choice, batch_plot_matrix

def main():
    # 1. Das anonymisierte Umfragedaten-CSV laden
    df = pd.read_csv('data/results-survey_anonym_codiert.csv')

    df = df.drop(columns=[col for col in df.columns if col.strip() == ''])

    df['Gruppe_ZHAW'] = df['E-Mail'].apply(lambda x: 'ZHAW' if isinstance(x, str) and x.endswith('@students.zhaw.ch') else 'Nicht-ZHAW')
    df['Gruppe_Altersgruppe'] = df['Altersgruppe']
    df['Gruppe_Geschlecht'] = df['Geschlecht']

    # 2. Gruppierungen zuordnen
    gruppierungen = ['Gruppe_ZHAW', 'Gruppe_Altersgruppe', 'Gruppe_Geschlecht']

# 3. Fragen in Typen einteilen – mit exakten Spaltennamen aus der CSV
    slider_fragen = [
    'Wie häufig nutzen Sie aktuell generative KI im Arbeitskontext? [Benutzung KI]',
    'Wie stark vertrauen Sie den Resultaten von Generativer KI?'
    ]

    single_choice_fragen = [
    'Geschlecht',
    'Altersgruppe',
    'Hat Generative KI Ihre Arbeitsweise verändert?',
    'Planen Sie, Generative KI in Zukunft (mehr) zu nutzen?'
    ]

    multiple_choice_fragen = [
    'Wo setzen Sie Generative KI typischerweise ein? [Texterstellung und -bearbeitung (z.B. Verfassung von Mails, Artikel oder Zusammenfassungen)]',
    'Wo setzen Sie Generative KI typischerweise ein? [Kreative Inhalte erstellen (z.B. Bilder, Musik, Videos, Designs etc.)]',
    'Wo setzen Sie Generative KI typischerweise ein? [Programmieren und Automatisieren (z.B. Code schreiben, Fehler beheben etc.)]',
    'Wo setzen Sie Generative KI typischerweise ein? [Lernen und Bildung (z.B. individuelle Erklärungen, Zusammenfassungen, Lernhilfe etc.)]',
    'Wo setzen Sie Generative KI typischerweise ein? [Kommunikation und Übersetzung verbessern (z.B. Korrektur von Texten, Übersetzungen von Artikeln etc.)]',
    'Welche positiven Erfahrungen habe Sie mit Generativer KI gemacht? [Zeitersparnis]',
    'Welche positiven Erfahrungen habe Sie mit Generativer KI gemacht? [Kreative Impulse]',
    'Welche positiven Erfahrungen habe Sie mit Generativer KI gemacht? [Entlastung (Zeit + Aufwand)]',
    'Welche positiven Erfahrungen habe Sie mit Generativer KI gemacht? [Qualität]',
    'Welche positiven Erfahrungen habe Sie mit Generativer KI gemacht? [Keine bemerkbaren Effekte]',
    'Welche negativen Erfahrungen haben Sie mit Generativer KI gemacht? [Ungenaue Resultate]',
    'Welche negativen Erfahrungen haben Sie mit Generativer KI gemacht? [Fehlender Datenschutz]',
    'Welche negativen Erfahrungen haben Sie mit Generativer KI gemacht? [Verbreitung von Fehlinformationen (Fake News)]',
    'Welche negativen Erfahrungen haben Sie mit Generativer KI gemacht? [Abhängigkeit von Technologie]',
    'Welche negativen Erfahrungen haben Sie mit Generativer KI gemacht? [Verlust von Originalität / menschlicher Kreativität]'
    ]

    matrix_fragen = [
        [
            'Welche dieser Erwartungen wurden erfüllt? [Effizienz][Skala 1]',
            'Welche dieser Erwartungen wurden erfüllt? [Kreativität][Skala 1]',
            'Welche dieser Erwartungen wurden erfüllt? [Arbeitsentlastung][Skala 1]',
            'Welche dieser Erwartungen wurden erfüllt? [Zuverlässigkeit][Skala 1]',
            'Welche dieser Erwartungen wurden erfüllt? [Innovation][Skala 1]'
        ],
        [
            'Welche dieser Erwartungen wurden erfüllt? [Effizienz][Skala 2]',
            'Welche dieser Erwartungen wurden erfüllt? [Kreativität][Skala 2]',
            'Welche dieser Erwartungen wurden erfüllt? [Arbeitsentlastung][Skala 2]',
            'Welche dieser Erwartungen wurden erfüllt? [Zuverlässigkeit][Skala 2]',
            'Welche dieser Erwartungen wurden erfüllt? [Innovation][Skala 2]'
        ]
    ]

    # Wert-Mapping und Clean-Funktion für Matrix-Fragen werden nicht mehr benötigt, da Werte bereits codiert sind.
    # matrix_kandidaten = [col for gruppe in matrix_fragen for col in gruppe]
    # for col in matrix_kandidaten:
    #     if col in df.columns:
    #         df[col] = df[col].apply(clean_matrix_value)

    base_plot_dir = '/Users/yanickfischer/Documents/vsCode/WissMethoden/AI_In_Unternehmen/plots'
    
    #Test für Spalten + Gruppennamen
    print("Spalten im df:", df.columns.tolist())

    # Für jede Gruppierung eigene Unterordner anlegen und Plots speichern
    # Debug: Prüfe Matrix-Spalten im DataFrame
    for matrix_cols in matrix_fragen:
        for col in matrix_cols:
            if col not in df.columns:
                print(f"❌ Spalte nicht gefunden (Matrix): '{col}'")
            else:
                print(f"✅ Spalte gefunden (Matrix): '{col}'")
    for gruppe in gruppierungen:
        gruppen_name = gruppe.replace('Gruppe_', '')

        print("Verwende Gruppierung:", gruppe)
        
        slider_dir = os.path.join(base_plot_dir, 'slider', gruppen_name)
        single_dir = os.path.join(base_plot_dir, 'single', gruppen_name)
        multiple_dir = os.path.join(base_plot_dir, 'multiple', gruppen_name)
        matrix_dir = os.path.join(base_plot_dir, 'matrix', gruppen_name)
        
        os.makedirs(slider_dir, exist_ok=True)
        os.makedirs(single_dir, exist_ok=True)
        os.makedirs(multiple_dir, exist_ok=True)
        os.makedirs(matrix_dir, exist_ok=True)

        if gruppe not in df.columns:
            print(f"❌ FEHLER: Gruppierungsspalte '{gruppe}' existiert nicht im DataFrame!")
            print("👉 Vorhandene Spalten:", df.columns.tolist())
            continue
        for frage in slider_fragen:
            gültig = df[[frage, gruppe]].dropna()
            print(f"📊 Check: {frage} | Gruppe: {gruppe} → gültige Zeilen: {gültig.shape[0]}")
        slider_figures = batch_plot_slider(df, slider_fragen, gruppe)
        if not slider_figures:
            print(f"⚠️ Keine Slider-Plots für Gruppierung: {gruppe}")
            continue
        for frage, fig in zip(slider_fragen, slider_figures):
            safe_frage = re.sub(r'[\\/*?:"<>|]', '_', frage)
            filename = f"slider_{safe_frage.replace(' ', '_')}_{gruppe}.png"
            full_path = os.path.join(slider_dir, filename)
            fig.savefig(full_path)
            print(f"✅ Gespeichert: {full_path}")
            plt.close(fig)

        single_choice_figures = batch_plot_single_choice(df, single_choice_fragen, gruppe)
        if not single_choice_figures:
            print(f"⚠️ Keine Single-Choice-Plots für Gruppierung: {gruppe}")
            continue
        for frage, fig in zip(single_choice_fragen, single_choice_figures):
            safe_frage = re.sub(r'[\\/*?:"<>|]', '_', frage)
            filename = f"single_{safe_frage.replace(' ', '_')}_{gruppe}.png"
            full_path = os.path.join(single_dir, filename)
            fig.savefig(full_path)
            print(f"✅ Gespeichert: {full_path}")
            plt.close(fig)

        multiple_choice_figures = batch_plot_multiple_choice(df, multiple_choice_fragen, gruppe)
        if not multiple_choice_figures:
            print(f"⚠️ Keine Multiple-Choice-Plots für Gruppierung: {gruppe}")
            continue
        for frage, fig_list in zip(multiple_choice_fragen, multiple_choice_figures):
            for i, fig in enumerate(fig_list if isinstance(fig_list, list) else [fig_list]):
                safe_frage = re.sub(r'[\\/*?:"<>|]', '_', frage)
                filename = f"multiple_{safe_frage.replace(' ', '_')}_{gruppe}_v{i+1}.png"
                full_path = os.path.join(multiple_dir, filename)
                fig.savefig(full_path)
                print(f"✅ Gespeichert: {full_path}")
                plt.close(fig)

        print(f"✅ Alle Plots für {gruppe} abgeschlossen.\n")
        print("Gruppierungen nach Schlaufe:", gruppe)

if __name__ == "__main__":
    main()