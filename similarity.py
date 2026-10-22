import pandas as pd


def charger_donnees(chemin):
    """Charge le CSV et retourne un DataFrame."""
    return pd.read_csv(chemin)


def standardiser(df):
    """Ajoute une colonne _z pour chaque stat _per90 (z-score).

    Retourne le DataFrame et la liste des colonnes _z.
    """
    df = df.copy()
    stats_cols = [c for c in df.columns if c.endswith("_per90")]
    z_cols = []
    for col in stats_cols:
        z_col = col + "_z"
        df[z_col] = (df[col] - df[col].mean()) / df[col].std()
        z_cols.append(z_col)
    return df, z_cols


def joueurs_similaires(df, z_cols, nom_joueur, n=5):
    """Retourne les n joueurs les plus proches de nom_joueur."""
    ligne = df[df["name"] == nom_joueur]
    if ligne.empty:
        raise ValueError(f"Joueur introuvable : {nom_joueur}")

    reference = ligne.iloc[0][z_cols]
    distances = ((df[z_cols] - reference) ** 2).sum(axis=1) ** 0.5

    resultat = df.copy()
    resultat["distance"] = distances
    resultat = resultat[resultat["name"] != nom_joueur]
    return resultat.sort_values("distance").head(n)[
        ["name", "team", "position", "distance"]
    ]