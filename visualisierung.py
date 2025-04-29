#In diesem Script sind alle Templates für die Plots zuHause.

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

def plot_slider_box(df, frage, gruppierung=None, titel=None, return_fig=False):
    if frage not in df.columns:
        print(f"❌ Frage '{frage}' nicht in DataFrame.")
        return None
    if gruppierung and gruppierung not in df.columns:
        print(f"❌ Gruppierung '{gruppierung}' nicht in DataFrame.")
        return None

    # Plot vorbereiten
    fig, ax = plt.subplots(figsize=(10, 5))

    if gruppierung:
        sns.boxplot(data=df, x=gruppierung, y=frage, ax=ax)
        ax.set_title(titel or f"{frage} nach {gruppierung}")
    else:
        sns.histplot(df[frage].dropna(), bins=10, kde=True, ax=ax)
        ax.set_title(titel or f"{frage}")

    ax.grid(True)
    fig.tight_layout()

    if return_fig:
        return fig
    return None


def plot_single_choice(df, frage, gruppierung=None, titel=None, return_fig=False):
    if frage not in df.columns:
        print(f"Warnung: '{frage}' nicht in DataFrame-Spalten gefunden.")
        return None
    if gruppierung and gruppierung not in df.columns:
        print(f"Warnung: Gruppierungsspalte '{gruppierung}' nicht in DataFrame-Spalten gefunden.")
        return None
    fig, ax = plt.subplots(figsize=(8, 4))
    if gruppierung:
        ct = pd.crosstab(df[frage], df[gruppierung], normalize='columns')
        ct.plot(kind="bar", stacked=True, ax=ax)
        ax.set_title(titel or f"{frage} nach {gruppierung}")
        ax.set_ylabel("Anteil")
        ax.grid(axis="y")
        # Set figure size proportional to number of columns for better display
        fig.set_size_inches(max(8, len(ct.columns)*1.5), 4)
    else:
        sns.countplot(y=df[frage], order=df[frage].value_counts().index, ax=ax)
        ax.set_title(titel or f"{frage}")
    fig.tight_layout()
    if return_fig:
        return fig
    return None


def plot_multiple_choice(df, fragenliste, gruppierung=None, titel=None, return_fig=False):
    for frage in fragenliste:
        if frage not in df.columns:
            print(f"Warnung: '{frage}' nicht in DataFrame-Spalten gefunden.")
            return None
    if gruppierung and gruppierung not in df.columns:
        print(f"Warnung: Gruppierungsspalte '{gruppierung}' nicht in DataFrame-Spalten gefunden.")
        return None
    if gruppierung:
        gruppen = df[gruppierung].dropna().unique()
        figs = []
        for group in gruppen:
            subset = df[df[gruppierung] == group]
            counts = subset[fragenliste].notna().sum().sort_values()
            fig, ax = plt.subplots(figsize=(8, 4))
            counts.plot(
                kind="barh", title=f"{titel or 'Mehrfachauswahl'} – {group}", ax=ax)
            ax.set_xlabel("Anzahl Nennungen")
            fig.tight_layout()
            if return_fig:
                figs.append(fig)
        if return_fig:
            return figs
        return None
    else:
        counts = df[fragenliste].notna().sum().sort_values()
        fig, ax = plt.subplots(figsize=(8, 4))
        counts.plot(kind="barh", title=titel or "Mehrfachauswahl", ax=ax)
        ax.set_xlabel("Anzahl Nennungen")
        fig.tight_layout()
        if return_fig:
            return fig
        return None

def plot_matrix_heatmap(df, matrix_cols, gruppierung=None, titel=None, return_fig=False):
    df = df.copy()
    for col in matrix_cols:
        if col not in df.columns:
            print(f"Warnung: '{col}' nicht in DataFrame-Spalten gefunden.")
            return None
    if gruppierung and gruppierung not in df.columns:
        print(f"Warnung: Gruppierungsspalte '{gruppierung}' nicht in DataFrame-Spalten gefunden.")
        return None
    # Konvertiere alle Matrix-Spalten in numerische Werte
    df[matrix_cols] = df[matrix_cols].apply(pd.to_numeric, errors="coerce")
    if gruppierung:
        data = df.groupby(gruppierung)[matrix_cols].mean()
    else:
        data = df[matrix_cols].mean().to_frame().T
    if data.empty:
        print(f"⚠️ Keine Daten für Heatmap '{titel}'")
        return None
    if data.isna().all().all():
        print(f"⚠️ Alle Werte in '{titel}' sind NaN – kein Plot möglich.")
        return None
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.heatmap(data, annot=True, cmap="YlGnBu", linewidths=0.5, ax=ax)
    ax.set_title(titel or "Mittelwerte Heatmap")
    # Set figure size proportional to number of columns for better display
    fig.set_size_inches(max(10, len(matrix_cols)*1.2), 0.6 * len(matrix_cols) + 2)
    fig.tight_layout()
    if return_fig:
        return fig
    return None


def batch_plot_slider(df, fragenliste, gruppierung=None):
    figures = []
    for frage in fragenliste:
        if frage in df.columns:
            fig = plot_slider_box(df, frage, gruppierung, return_fig=True)
            if fig is not None:
                figures.append(fig)
    return figures


# Ergänzung: Batch-Funktionen für Single-Choice und Matrix
def batch_plot_single_choice(df, fragenliste, gruppierung=None):
    """
    Erstellt für jede Frage in fragenliste einen Single-Choice-Plot.
    """
    figures = []
    for frage in fragenliste:
        if frage in df.columns:
            fig = plot_single_choice(df, frage, gruppierung, return_fig=True)
            if fig is not None:
                figures.append(fig)
    return figures



def batch_plot_matrix(df, matrix_prefix="Welche dieser Erwartungen wurden erfüllt?", gruppierung=None):
    """
    Sucht automatisch alle Matrixfragen-Spalten anhand eines Prefixes und gruppiert sie thematisch.
    Erstellt eine Heatmap pro Gruppe (z. B. nach Gruppierung).
    """
    from collections import defaultdict
    matrix_groups = defaultdict(list)
    for col in df.columns:
        if matrix_prefix in col:
            # Extrahiere Basislabel, z. B. 'Effizienz' aus '[Effizienz][Skala 1]'
            import re
            match = re.search(r"\[(.*?)\]\s*\[Skala \d\]", col)
            if match:
                key = match.group(1)
                matrix_groups[key].append(col)
    figures = []
    for label, cols in matrix_groups.items():
        if len(cols) >= 1:
            fig = plot_matrix_heatmap(df, cols, gruppierung=gruppierung, titel=label, return_fig=True)
            if fig:
                figures.append(fig)
        else:
            print(f"⚠️ Keine gültigen Spalten für Matrixgruppe: {label}")
    return figures


# Neue Funktion: batch_plot_multiple_choice
def batch_plot_multiple_choice(df, fragenliste, gruppierung=None):
    """
    Erstellt für jede Frage in fragenliste einen Multiple-Choice-Plot (einzeln) und gibt eine Liste der Figure-Objekte zurück.
    """
    figures = []
    for frage in fragenliste:
        # Wir rufen plot_multiple_choice für jede Frage einzeln mit return_fig=True auf
        fig = plot_multiple_choice(df, [frage], gruppierung=gruppierung, return_fig=True)
        # plot_multiple_choice gibt None zurück, falls Frage nicht gefunden wurde
        if fig is not None:
            figures.append(fig)
    return figures
