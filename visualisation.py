import numpy as np
import matplotlib.pyplot as plt


def radar_comparaison(df, z_cols, nom_1, nom_2, chemin_sortie=None):
    """Trace un radar chart comparant deux joueurs sur leurs stats z-score."""
    ligne_1 = df[df["name"] == nom_1]
    ligne_2 = df[df["name"] == nom_2]
    if ligne_1.empty or ligne_2.empty:
        raise ValueError("Un des deux joueurs est introuvable")

    valeurs_1 = ligne_1.iloc[0][z_cols].astype(float).tolist()
    valeurs_2 = ligne_2.iloc[0][z_cols].astype(float).tolist()
    labels = [c.replace("_per90_z", "") for c in z_cols]

    angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()
    angles += angles[:1]
    valeurs_1 += valeurs_1[:1]
    valeurs_2 += valeurs_2[:1]

    fig, ax = plt.subplots(figsize=(8, 7), subplot_kw={"polar": True})
    ax.plot(angles, valeurs_1, label=nom_1, linewidth=2)
    ax.fill(angles, valeurs_1, alpha=0.2)
    ax.plot(angles, valeurs_2, label=nom_2, linewidth=2)
    ax.fill(angles, valeurs_2, alpha=0.2)

    ax.set_xticks(angles[:-1])
    ax.set_xticklabels(labels)

    # Graduations radiales : on les place entre deux axes pour éviter le chevauchement
    ax.set_rlabel_position(22.5)
    ax.tick_params(axis="y", labelsize=8, labelcolor="gray")

    ax.set_title(f"{nom_1} vs {nom_2}", pad=20)

    # Légende sous le graphique, donc jamais coupée
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.08), ncol=2)

    if chemin_sortie:
        fig.savefig(chemin_sortie, dpi=150, bbox_inches="tight")
    plt.show()