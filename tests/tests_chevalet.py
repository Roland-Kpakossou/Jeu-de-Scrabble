import random

from scrabble.joueur.chevalet import Chevalet
from scrabble.jeton import Jeton


def tests_creation_d_un_chevalet_de_taille_standard():
    chevalet = Chevalet()
    assert (
        chevalet.taille() == 7
    ), "Erreur : La taille initiale du chevalet devrait être de 7"


def tests_creation_d_un_chevalet_avec_une_taille_specifique():
    chevalet = Chevalet(10)
    assert chevalet.taille() == 10, "Erreur : La taille du chevalet devrait être de 10"


def tests_des_emplacements_initialement_vides():
    chevalet = Chevalet(7)
    assert (
        chevalet.nombre_emplacements_vides() == 7
    ), "Erreur : Tous les emplacements devraient être initialement vides"


def tests_de_la_fonctionnalite_d_ajout_de_jetons():
    chevalet = Chevalet(7)
    jeton = Jeton("A", 1)
    chevalet.ajouter_jeton(jeton)
    assert (
        chevalet.nombre_emplacements_vides() == 6
    ), "Erreur : L'ajout d'un jeton devrait réduire le nombre d'emplacements vides à 6"
    assert (
        chevalet.emplacements[0] == jeton
    ), "Erreur : Le jeton devrait être dans le premier emplacement vide"


def tests_chevalet_plein():
    chevalet = Chevalet(7)

    assert (
        not chevalet.est_plein()
    ), "Erreur : Le chevalet ne devrait pas être plein initialement"

    jetons = [Jeton(lettre, 1) for lettre in "AEILNOR"]  # Création de 7 jetons

    # Ajouter des jetons jusqu'à ce que le chevalet soit plein
    for i in range(chevalet.taille()):
        chevalet.ajouter_jeton(jetons[i], i)

    assert (
        chevalet.est_plein()
    ), "Erreur : Le chevalet devrait être plein après l'ajout de 7 jetons"

    # Test de retrait de jeton pour vérifier que le chevalet n'est plus plein
    chevalet.retirer_jeton(0)
    assert (
        not chevalet.est_plein()
    ), "Erreur : Le chevalet ne devrait plus être plein après le retrait d'un jeton"


def tests_de_validation_des_emplacements():
    chevalet = Chevalet(7)
    assert chevalet.emplacement_est_valide(
        0
    ), "Erreur : L'emplacement 0 devrait être valide"
    assert chevalet.emplacement_est_valide(
        6
    ), "Erreur : L'emplacement 6 devrait être valide"
    assert not chevalet.emplacement_est_valide(
        -1
    ), "Erreur : L'emplacement -1 ne devrait pas être valide"
    assert not chevalet.emplacement_est_valide(
        7
    ), "Erreur : L'emplacement 7 ne devrait pas être valide"


def tests_d_ajout_de_jeton_a_un_emplacement_specifique():
    chevalet = Chevalet(7)
    jeton = Jeton("J", 8)
    chevalet.ajouter_jeton(jeton, 3)
    assert (
        chevalet.emplacements[3] == jeton
    ), "Erreur : Le jeton devrait être à l'index 3"


def tests_de_validation_d_emplacement_et_de_retrait_de_jeton():
    chevalet = Chevalet(7)
    jeton = Jeton("J", 8)
    chevalet.ajouter_jeton(jeton, 3)
    assert (
        chevalet.obtenir_jeton(3) == jeton
    ), "Erreur : Devrait obtenir le jeton à l'index 3"
    assert (
        chevalet.retirer_jeton(3) == jeton
    ), "Erreur : Le jeton2 devrait être retiré de l'index 3"
    assert chevalet.emplacement_est_vide(
        3
    ), "Erreur : L'emplacement 3 devrait être vide après le retrait du jeton"


def tests_de_melange_des_jetons():
    # Création d'un chevalet avec 7 emplacements
    chevalet = Chevalet(7)

    # Lettres pour les jetons, typiques du Scrabble
    lettres_jetons = "AEILNOR"

    # Création des jetons avec les lettres spécifiées, chacun ayant une valeur de 1 point
    jetons = [Jeton(lettre, 1) for lettre in lettres_jetons]

    # Remplissage du chevalet avec les jetons, chaque jeton placé dans un emplacement correspondant
    for i in range(chevalet.taille()):
        chevalet.ajouter_jeton(jetons[i], i)

    # Vérification de l'ordre initial des jetons dans le chevalet
    for i in range(chevalet.taille()):
        assert (
            chevalet.obtenir_jeton(i).lettre == lettres_jetons[i]
        ), "L'ordre initial des jetons est incorrect"

    # Fixation de la graine pour garantir que le mélange est reproductible
    random.seed(42)

    # Mélange des jetons dans le chevalet
    chevalet.melanger_jetons()

    # Vérification que les emplacements sont toujours une liste après le mélange
    assert isinstance(
        chevalet.emplacements, list
    ), "Erreur : Les emplacements doivent toujours être une liste après le mélange"

    # Ordre attendu des lettres après le mélange, basé sur la graine fixée à 42
    lettres_jetons_apres_melanges = "ELNIRAO"

    # Vérification que chaque jeton dans le chevalet correspond à l'ordre attendu après le mélange
    for i in range(chevalet.taille()):
        assert (
            chevalet.obtenir_jeton(i).lettre == lettres_jetons_apres_melanges[i]
        ), "L'ordre des jetons après le mélange est incorrect"


def tests():
    tests_creation_d_un_chevalet_de_taille_standard()
    tests_creation_d_un_chevalet_avec_une_taille_specifique()
    tests_des_emplacements_initialement_vides()
    tests_de_la_fonctionnalite_d_ajout_de_jetons()
    tests_chevalet_plein()
    tests_de_validation_des_emplacements()
    tests_d_ajout_de_jeton_a_un_emplacement_specifique()
    tests_de_validation_d_emplacement_et_de_retrait_de_jeton()
    tests_de_melange_des_jetons()


if __name__ == "__main__":
    print('Tests unitaires de la classe "Chevalet"...')

    tests()

    print("Tests unitaires passés avec succès!")
