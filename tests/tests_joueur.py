from scrabble.joueur import Joueur
from scrabble.joueur.chevalet import Chevalet
from scrabble.jeton import Jeton


def tests_initialisation_d_un_joueur():
    joueur = Joueur("Alice")
    assert (
        joueur.nom == "Alice"
    ), "Erreur: Le nom du joueur n'est pas correctement initialisé."
    assert joueur.score == 0, "Erreur: Le score initial du joueur devrait être 0."
    assert isinstance(
        joueur.chevalet, Chevalet
    ), "Erreur: Le chevalet du joueur doit être une instance de Chevalet."
    assert (
        joueur.chevalet.taille() == 7
    ), "Erreur: Le chevalet du joueur devrait avoir 7 emplacements."


def tests_validation_du_nom():
    try:
        joueur_invalide = Joueur("")
        assert False, "Erreur: Un nom vide aurait dû déclencher une AssertionError."
    except AssertionError:
        pass  # succès

    try:
        joueur_invalide = Joueur("    ")
        assert False, "Erreur: Un nom constitué uniquement d'espaces aurait dû déclencher une AssertionError."
    except AssertionError:
        pass  # succès


def tests_nombre_de_nouveaux_jetons_a_tirer():
    joueur = Joueur("Alice")
    assert (
        joueur.nombre_de_nouveaux_jetons_a_tirer() == 7
    ), "Erreur: Le chevalet doit initialement avoir 7 emplacements vides."
    assert (
        joueur.peut_tirer_de_nouveaux_jetons() is True
    ), "Erreur: Le joueur doit pouvoir tirer des jetons si le chevalet n'est pas plein."

    # Test pour le chevalet plein
    for i in range(7):
        jeton = Jeton("A", 1)
        joueur.chevalet.ajouter_jeton(jeton, i)

    assert (
        joueur.nombre_de_nouveaux_jetons_a_tirer() == 0
    ), "Erreur: Le chevalet doit être plein, donc aucun emplacement vide."
    assert (
        joueur.peut_tirer_de_nouveaux_jetons() is False
    ), "Erreur: Le joueur ne devrait pas pouvoir tirer de nouveaux jetons si le chevalet est plein."


def tests():
    tests_initialisation_d_un_joueur()
    tests_validation_du_nom()
    tests_nombre_de_nouveaux_jetons_a_tirer()


if __name__ == "__main__":
    print('Tests unitaires de la classe "Joueur"...')

    tests()

    print("Tests unitaires passés avec succès!")
