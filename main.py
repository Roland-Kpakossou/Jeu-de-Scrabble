import random

from scrabble.ui.fenetre_partie import FenetrePartie


if __name__ == "__main__":
    # ASTUCE: Fixer une graine pour le générateur de nombres aléatoires pour assurer la reproductibilité des résultats.
    # Ceci permet de garantir que le même ensemble de lettres sera généré à chaque exécution du code.
    # Ce qui peut s'avérer utile lors du débogage et de l'exécution de tests manuels.
    # Pour activer ce comportement, il vous suffit de décommenter la ligne suivante :
    # random.seed(42)

    # Initialisation de la fenêtre principale pour une partie de Scrabble avec deux joueurs.
    fenetre = FenetrePartie(nombre_de_joueurs=2, langue="fr")

    # Démarrage de la boucle principale de l'interface graphique.
    # Cette boucle écoute les événements de l'utilisateur (comme les clics de souris et les frappes au clavier)
    # et répond en conséquence. Elle est essentielle pour afficher la fenêtre et la rendre interactive.
    fenetre.mainloop()
