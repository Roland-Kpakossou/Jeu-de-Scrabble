from scrabble.partie import Partie
from scrabble.jeton import Jeton
from scrabble.common.position import Position


def tests_initialisation_partie():
    partie = Partie(2, "fr")
    assert (
        len(partie.joueurs) == 2
    ), "Erreur: Le nombre de joueurs devrait être correctement initialisé à 2."
    assert (
        partie.joueur_actif in partie.joueurs
    ), "Erreur: Le joueur actif doit faire partie des joueurs de la partie."


def tests_distribution_des_jetons():
    partie = Partie()
    assert (
        len(partie.jetons_libres) > 0
    ), "Erreur: La réserve de jetons doit être initialisée et remplie."
    assert isinstance(
        partie.jetons_libres[0], Jeton
    ), "Erreur: Les objets dans la réserve de jetons doivent être des instances de Jeton."


def tests_gestion_des_jetons():
    partie = Partie()
    jetons_tires = partie.tirer_jetons(7)
    assert (
        len(jetons_tires) == 7
    ), "Erreur: Le nombre de jetons tirés doit correspondre à la demande."
    assert (
        len(partie.jetons_libres) + len(jetons_tires) == len(partie.jetons_libres) + 7
    ), "Erreur: Les jetons tirés doivent être correctement retirés de la réserve."


def tests_validation_de_mots():
    partie = Partie(2, "fr")
    mot_valide = (
        "ARBRE" if "ARBRE" in partie.dictionnaire else next(iter(partie.dictionnaire))
    )
    mot_invalide = "ZZZZZ"
    assert partie.mot_permis(mot_valide), "Erreur: Ce mot devrait être permis."
    assert not partie.mot_permis(
        mot_invalide
    ), "Erreur: Ce mot ne devrait pas être permis."


def tests_passage_au_joueur_suivant():
    partie = Partie(2)
    joueur_initial = partie.joueur_actif
    partie.passer_au_joueur_suivant()
    assert (
        partie.joueur_actif != joueur_initial
    ), "Erreur: Le joueur actif devrait avoir changé."
    assert (
        partie.joueur_actif in partie.joueurs
    ), "Erreur: Le nouveau joueur actif doit encore faire partie des joueurs."


def tests_deplacement_de_jetons_du_chevalet_au_plateau():
    partie = Partie(2)
    position_chevalet = 0  # Supposons que le joueur actif a des jetons à cette position dans son chevalet
    position_plateau = Position(7, 7)  # Position centrale sur le plateau
    partie.joueur_actif.chevalet.ajouter_jeton(Jeton("A", 1), position_chevalet)

    # Tenter de placer un jeton sur le plateau
    assert partie.deplacer_jeton_du_chevalet_au_plateau(
        position_chevalet, position_plateau
    ), "Erreur: Le jeton devrait être placé avec succès sur le plateau."


def tests_jouer_un_tour():
    partie = Partie(2)

    # Nous configurons le joueur[0] comme joueur actif
    partie.joueur_actif = partie.joueurs[0]

    # Simulation d'un ensemble de jetons tirés par le joueur actif (Joueur 0)
    jetons_tires = [
        Jeton("E", 1),
        Jeton("C", 3),
        Jeton("O", 1),
        Jeton("L", 1),
        Jeton("E", 1),
        Jeton("H", 4),
        Jeton("Z", 10),
    ]

    for i, jeton in enumerate(jetons_tires):
        partie.joueur_actif.chevalet.ajouter_jeton(jeton, i)

    # Simuler un tour où le joueur place des jetons formant un mot valide sur le plateau
    partie.deplacer_jeton_du_chevalet_au_plateau(0, Position(7, 4))
    partie.deplacer_jeton_du_chevalet_au_plateau(1, Position(7, 5))
    partie.deplacer_jeton_du_chevalet_au_plateau(2, Position(7, 6))
    partie.deplacer_jeton_du_chevalet_au_plateau(3, Position(7, 7))
    partie.deplacer_jeton_du_chevalet_au_plateau(4, Position(7, 8))

    succes, _ = partie.jouer_un_tour()
    assert succes, "Erreur: Le tour devrait être joué avec succès."

    # Nous configurons le joueur[1] comme joueur actif
    partie.joueur_actif = partie.joueurs[1]

    # Simulation d'un ensemble de jetons tirés par le joueur actif (Joueur 0)
    jetons_tires = [
        Jeton("B", 3),
        Jeton("G", 2),
        Jeton("T", 1),
        Jeton("U", 1),
        Jeton("P", 3),
        Jeton("S", 1),
        Jeton("V", 4),
    ]

    for i, jeton in enumerate(jetons_tires):
        partie.joueur_actif.chevalet.ajouter_jeton(jeton, i)

    partie.deplacer_jeton_du_chevalet_au_plateau(5, Position(10, 6))
    succes, _ = partie.jouer_un_tour()
    assert (
        not succes
    ), "Erreur: Le tour devrait échoué car la position du nouveau jeton est invalide."

    partie.deplacer_jeton_du_chevalet_au_plateau(5, Position(8, 6))
    succes, _ = partie.jouer_un_tour()
    assert succes, "Erreur: Le tour devrait être joué avec succès."


def tests_fin_de_partie():
    partie = Partie()
    partie.jetons_libres = []  # Simuler la fin des jetons disponibles
    assert (
        partie.est_terminee()
    ), "Erreur: La partie devrait être considérée comme terminée."


def tests_determiner_gagnant():
    partie = Partie(2)
    partie.joueurs[0].score = 10
    partie.joueurs[1].score = 20
    gagnant = partie.determiner_gagnant()
    assert (
        gagnant == partie.joueurs[1]
    ), "Erreur: Le joueur avec le score le plus élevé doit être le gagnant."


def tests():
    tests_initialisation_partie()
    tests_distribution_des_jetons()
    tests_gestion_des_jetons()
    tests_validation_de_mots()
    tests_passage_au_joueur_suivant()
    tests_deplacement_de_jetons_du_chevalet_au_plateau()
    tests_jouer_un_tour()
    tests_fin_de_partie()
    tests_determiner_gagnant()


if __name__ == "__main__":
    print('Tests unitaires de la classe "Partie"...')

    tests()

    print("Tests unitaires passés avec succès!")
