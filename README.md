#### - English Version, found later on the page - 

# Wissenschaftliche Methoden: Umfrageanalyse mit Python - DEUTSCH

In diesem Projekt analysieren wir die Ergebnisse einer selbst erstellten Umfrage zur Nutzung von generativer Künstlicher Intelligenz (z. B. ChatGPT) im Arbeitskontext. Ziel war es, Erkenntnisse über die Einstellung, Nutzung und Erfahrungen von Teilnehmenden zu gewinnen.

Die Analyse wurde im Rahmen eines ZHAW-Projekts von **Haris Jusmani**, **Christopher Alvaro** und **Yanick Fischer** durchgeführt.  
Ansprechpartner: [fischya3@students.zhaw.ch](mailto:fischya3@students.zhaw.ch)

---

## 🧭 Projektziel

Das Repository dokumentiert die komplette **explorative Datenanalyse (EDA)** dieser Umfrage.  
Wir haben mit Python systematisch untersucht:

- Wie oft und wofür generative KI genutzt wird
- Welche Erwartungen damit verbunden sind
- Ob diese Erwartungen erfüllt wurden
- Welche positiven und negativen Erfahrungen gemacht wurden
- Wie stark Vertrauen, Weiterempfehlung und Kompetenzempfinden ausgeprägt sind
- Unterschiede zwischen Gruppen (z. B. Studierende vs. Berufstätige, Geschlecht)

Alle Daten sind **vollständig anonymisiert**.

---

## 📋 Überblick über die Umfrage

Die folgende Tabelle zeigt die Struktur der Umfrage mit Fragetypen und Antwortformaten:

| Nr. | Frage | Typ | Antwortoptionen |
|-----|-------|-----|------------------|
| 1 | Geschlecht | Single-Choice | Frau, Mann, Divers |
| 2 | Altersgruppe | Single-Choice | 18–22, 23–27, ..., >52 |
| 3 | E-Mail-Adresse | Textfeld | – |
| 4 | Nutzungshäufigkeit von KI | Skala 0–10 | 0 = nie, 10 = täglich |
| 5 | Einsatzbereiche von KI | Multiple-Choice | Texterstellung, Programmierung, ... |
| 6 | Erwartungen an KI | Matrix (1–5) | Effizienz, Kreativität, ... |
| 7 | Erfüllung der Erwartungen | Dual-Matrix (1–5) | + Ja/Nein |
| 8 | Positive Erfahrungen | Multiple-Choice | Zeitersparnis, Qualität, ... |
| 9 | Negative Erfahrungen | Multiple-Choice | Datenschutz, Fake News, ... |
|10 | Vertrauen in KI | Skala 0–10 | 0 = kein Vertrauen, 10 = voll |
|11 | Veränderte Arbeitsweise | Single-Choice | Ja/Nein |
|12 | Zukunftspläne für KI | Single-Choice | Ja, Nein, Unsicher |

---

## 📊 Visualisierung & Analyse

Im Zentrum der Analyse stehen:
- **Boxplots & Balkendiagramme**: Gruppierte Darstellungen nach Geschlecht und ZHAW-Status
- **Radarplots**: Erwartung vs. Erfüllung
- **Heatmaps**: Korrelationen & Cluster von Erfahrungen
- **Dashboards**: Aggregierte Mittelwerte in übersichtlicher Form
- **Binärmatrizen**: Welche Personen haben welche Erfahrungen gemacht?

Wir legen besonderen Wert auf:
- saubere, farbkodierte Visualisierungen
- intuitive Darstellung auch ohne Vorwissen
- vergleichbare Gruppen (Studierende vs. Berufstätige)

---

## 📂 Dateien im Projekt

| Datei/Ordner | Funktion |
|--------------|----------|
| `main.py` | Führt die vollständige Analyse aus |
| `visualisierungen.py` | Beinhaltet zentrale Plot-Vorlagen |
| `results-survey_anonym_codiert_v2.csv` | Anonymisierter Umfragedatensatz |
| `Collab_ChatGPT/Instruktionen/Poster_GPT-Projekt_Instruktionen.pdf` | Initiales GPT-Prompt zur Strukturierung des Projekts |
| `Poster/POSTER_DRAFT_v2.pdf` | Finale Posterpräsentation für die ZHAW |

---

## 🤖 Einsatz von ChatGPT

Ein zentrales Ziel des Projekts war es, **ChatGPT nicht nur als Tool, sondern als echten Kollaborationspartner** einzusetzen.  
GPT wurde verwendet, um:

- analytische Ideen zu hinterfragen (Sparring-Partner)
- explorative Schritte in Python effizient umzusetzen
- Textbausteine, Visualisierungsstrategien und logische Strukturierung zu optimieren

Die Datei [`Poster_GPT-Projekt_Instruktionen.pdf`](Poster_GPT-Projekt_Instruktionen.pdf) dokumentiert die initiale Aufgabenstellung und Zielsetzung, wie sie GPT vorgelegt wurde.

---

## 🧾 Präsentationsergebnis

Das finale Ergebnis – ein **informatives, visuelles Poster** – wurde an der **ZHAW öffentlich präsentiert**  
👉 Du findest es hier: [`POSTER_DRAFT_v2.pdf`](Poster/POSTER_DRAFT_v2.pdf)

---

## 🧠 Für wen ist das Projekt?

Dieses Repository richtet sich an:

- Studierende und Lehrende im Bereich Datenanalyse
- Interessierte ohne Programmierkenntnisse, die verstehen wollen, wie Umfragedaten interpretiert werden
- Python-Anwender:innen, die EDA-Projekte strukturieren und visualisieren möchten

---

## 📬 Kontakt

Für Fragen oder Anfragen:  
📧 [fischya3@students.zhaw.ch](mailto:fischya3@students.zhaw.ch)

# Scientific Methods: Survey Analysis with Python - ENGLISH

This project analyzes the results of a self-designed survey on the use of generative artificial intelligence (e.g., ChatGPT) in professional contexts.  
The goal was to gain insights into participants' attitudes, usage patterns, and experiences with AI.

The analysis was conducted as part of a ZHAW student project by **Haris Jusmani**, **Christopher Alvaro**, and **Yanick Fischer**.  
Contact: [fischya3@students.zhaw.ch](mailto:fischya3@students.zhaw.ch)

---

## 🧭 Project Objective

This repository documents the full **exploratory data analysis (EDA)** of the survey.  
Using Python, we systematically examined:

- How often and in which contexts people use generative AI
- Expectations towards the technology
- Whether those expectations were met
- Positive and negative experiences with generative AI
- Trust, recommendation intent, and self-perceived competence
- Differences across groups (e.g., students vs. professionals, gender)

All data is fully **anonymized**.

---

## 📋 Survey Structure

The table below outlines the structure of the survey, including question types and answer formats:

| No. | Question | Type | Answer Options |
|-----|----------|------|----------------|
| 1 | Gender | Single Choice | Female, Male, Other |
| 2 | Age group | Single Choice | 18–22, 23–27, ..., >52 |
| 3 | Email address | Text field | – |
| 4 | Frequency of AI use | Scale 0–10 | 0 = never, 10 = daily |
| 5 | Typical AI usage areas | Multiple Choice | Text, creative, coding, learning, translation |
| 6 | Expectations towards AI | Matrix (1–5) | Efficiency, Creativity, etc. |
| 7 | Were expectations fulfilled? | Dual Matrix | + Yes/No |
| 8 | Positive experiences | Multiple Choice | Time-saving, creativity, quality, etc. |
| 9 | Negative experiences | Multiple Choice | Inaccuracy, privacy, misinformation, etc. |
|10 | Trust in AI results | Scale 0–10 | 0 = none, 10 = full |
|11 | Has AI changed your work style? | Single Choice | Yes, No |
|12 | Plan to use AI in the future? | Single Choice | Yes, No, Unsure |

---

## 📊 Visualization & Analysis

Our analysis includes:
- **Boxplots and bar charts**: grouped by gender and student status
- **Radar plots**: comparing expectations vs. fulfillment
- **Heatmaps**: correlation and experience clustering
- **Dashboards**: summarized averages by group
- **Binary matrices**: who experienced what

Key focus points:
- Clean, color-coded visualizations
- Intuitive layout for non-experts
- Comparison of target groups (e.g., students vs. professionals)

---

## 📂 Files in the Project

| File/Folder | Purpose |
|-------------|---------|
| `main.py` | Executes the full analysis |
| `visualisierungen.py` | Contains reusable plot templates |
| `results-survey_anonym_codiert_v2.csv` | Anonymized raw survey data |
| `Collab_ChatGPT/Instruktionen/Poster_GPT-Projekt_Instruktionen.pdf` | Initial GPT prompt and instructions |
| `Poster/POSTER_DRAFT_v2.pdf` | Final presentation poster (ZHAW event) |

---

## 🤖 Use of ChatGPT

A key part of the project was working with **ChatGPT as a collaborative partner**, not just a tool.  
GPT was used to:

- Reflect and challenge ideas (Sparring)
- Efficiently implement EDA logic in Python
- Structure results and refine visualization design

The file [`Poster_GPT-Projekt_Instruktionen.pdf`](Collab_ChatGPT/Instruktionen/Poster_GPT-Projekt_Instruktionen.pdf) contains the original instructions used to kick off GPT collaboration.

---

## 🧾 Presentation Outcome

The final result — an **informative, visual poster** — was publicly presented at ZHAW.  
👉 You can find it here: [`POSTER_DRAFT_v2.pdf`](Poster/POSTER_DRAFT_v2.pdf)

---

## 🧠 Who is this for?

This repository is ideal for:

- Students and educators in data science and social research
- Curious minds without coding knowledge who want to understand survey interpretation
- Python users seeking inspiration for structured, visual EDA workflows

---

## 📬 Contact

Questions or feedback?  
📧 [fischya3@students.zhaw.ch](mailto:fischya3@students.zhaw.ch)
