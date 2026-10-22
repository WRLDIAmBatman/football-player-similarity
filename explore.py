import pandas as pd

df = pd.read_csv("data/players.csv")

print(df.columns.tolist())
print(df.shape)

# 1. Récupérer automatiquement toutes les colonnes "par 90 minutes"
stats = [c for c in df.columns if c.endswith("_per90")]
print("Stats utilisées :", stats)

# 2. Transformer chaque stat en z-score (même échelle pour toutes)
for s in stats:
    df[s + "_z"] = (df[s] - df[s].mean()) / df[s].std()

z_cols = [s + "_z" for s in stats]

# 3. Choisir le joueur de référence par son nom
nom_joueur = "Joueur 05"

ligne = df[df["name"] == nom_joueur]
if ligne.empty:
    raise SystemExit(f"Joueur introuvable : {nom_joueur}")

joueur_1 = ligne.iloc[0][z_cols]
tous = df[z_cols]
distances = ((tous - joueur_1) ** 2).sum(axis=1) ** 0.5

# 4. Afficher les 5 joueurs les plus proches (hors le joueur lui-même)
df["distance"] = distances
resultat = df[df["name"] != nom_joueur].sort_values("distance").head(5)
print(f"Joueurs les plus proches de {nom_joueur} :")
print(resultat[["name", "team", "position", "distance"]])