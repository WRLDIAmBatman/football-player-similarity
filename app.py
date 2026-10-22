import streamlit as st
from similarity import charger_donnees, standardiser, joueurs_similaires

st.title("Football Player Similarity")

df = charger_donnees("data/players.csv")
df, z_cols = standardiser(df)

player = st.selectbox("Choisis un joueur", df["name"])

# Stats du joueur (sans les colonnes _z)
colonnes_visibles = [c for c in df.columns if not c.endswith("_z")]
stats_joueur = df[df["name"] == player][colonnes_visibles]

st.subheader(f"Statistiques de {player}")
st.dataframe(stats_joueur)

# Joueurs similaires
result = joueurs_similaires(df, z_cols, player, n=5)

st.subheader(f"Joueurs les plus proches de {player}")
st.dataframe(result)