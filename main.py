from similarity import charger_donnees, standardiser, joueurs_similaires
from visualisation import radar_comparaison

CHEMIN_DONNEES = "data/players.csv"
NOM_JOUEUR = "Joueur 05"

df = charger_donnees(CHEMIN_DONNEES)
df, z_cols = standardiser(df)

resultats = joueurs_similaires(df, z_cols, NOM_JOUEUR, n=5)
print(f"Joueurs les plus proches de {NOM_JOUEUR} :")
print(resultats)

# Radar entre le joueur de référence et son plus proche voisin
plus_proche = resultats.iloc[0]["name"]
radar_comparaison(df, z_cols, NOM_JOUEUR, plus_proche,
                  chemin_sortie="radar.png")