# Wissenschaftliche Methoden Umfrage
In diesem ZHAW-Projekt von Haris Jusmani, Christopher Alvaro und Yanick Fischer ist die Explorative Datenanlyse einer Umfrage dargestellt.

Sämtliche Daten sind hier bewusst anonymisiert.
Anfragen dazu bei fischya3@students.zhaw.ch platzieren

## Überblick über die Umfragefragen

Die folgende Tabelle zeigt alle 12 Hauptfragen der Umfrage, den jeweiligen Fragetyp sowie die Antwortoptionen:

| Frage-Nr | Frage | Fragetyp | Antwortmöglichkeiten |
|----------|-------|-----------|------------------------|
| 1 | Geschlecht | Single-Choice | Frau, Mann, Divers |
| 2 | Altersgruppe | Single-Choice | 18–22, 23–27, 28–32, 33–37, 38–42, 43–47, 48–52, >52 |
| 3 | E-Mail-Adresse | Text (Demografie) | – |
| 4 | Wie häufig nutzen Sie aktuell generative KI im Arbeitskontext? | Slider 0–10 | 0 = nie bis 10 = täglich |
| 5 | Wo setzen Sie Generative KI typischerweise ein? | Multiple-Choice | Texterstellung, Kreative Inhalte, Programmierung, Lernen, Übersetzung |
| 6 | Welche Erwartungen hatten Sie an Generative KI vor der Nutzung? | Matrix | Effizienz, Kreativität, Arbeitsentlastung, Zuverlässigkeit, Innovation (Skala 1–5) |
| 7 | Welche dieser Erwartungen wurden erfüllt? | Dual-Matrix | Für jede Erwartung: Erfüllt 1–5 und Erwartung erfüllt Ja/Nein |
| 8 | Welche positiven Erfahrungen haben Sie mit Generativer KI gemacht? | Multiple-Choice | Zeitersparnis, Kreative Impulse, Entlastung, Qualität, Keine Effekte |
| 9 | Welche negativen Erfahrungen haben Sie mit Generativer KI gemacht? | Multiple-Choice | Ungenaue Resultate, Datenschutz, Fake News, Abhängigkeit, Verlust Originalität |
| 10 | Wie stark vertrauen Sie den Resultaten von Generativer KI? | Slider 0–10 | 0 = kein Vertrauen bis 10 = vollständiges Vertrauen |
| 11 | Hat Generative KI Ihre Arbeitsweise verändert? | Single-Choice | Ja stark, Ja leicht, Nein, gar nicht |
| 12 | Planen Sie, Generative KI in Zukunft (mehr) zu nutzen? | Single-Choice | Ja, Unsicher, Nein |

## Dateien im Projekt

* visualisierungen.py dient als Speicher für Plot-templates
* main.py dient als Hauptklasse -> durch ausführen werden für alle Fragetypen die Templates angewendet und Plots erstellt