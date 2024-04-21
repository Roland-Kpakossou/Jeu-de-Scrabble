from scrabble.plateau.case import Case
from scrabble.jeton import Jeton


def tests_initialisation_case_sans_bonus():
    # TODO
    # Création d'une case sans bonus
    case = Case()
    # Vérification des attributs initiaux
    assert case.multiplicateur == 1, "Le multiplicateur devrait être 1 par défaut"
    assert case.type_bonus is None, "Le type de bonus devrait être None par défaut"
    assert case.est_vide(), "La case devrait être initialement vide"
    assert case.jeton_occupant is None, "Le jeton occupant devrait être None à l'initialisation"

    assert False, "Erreur: Compléter tests_initialisation_case_sans_bonus"


def tests_initialisation_avec_des_parametres_incorrects():
    # TODO
    # Test d'initialisation avec un multiplicateur incorrect
    try:
        case = Case(multiplicateur=5)
    except AssertionError:
        pass  # On attend une erreur AssertionError

    # Test d'initialisation avec un type de bonus incorrect
    try:
        case = Case(type_bonus="A")
    except AssertionError:
        pass  # On attend une erreur AssertionError

    assert (
        False
    ), "Erreur: Compléter tests_initialisation_avec_des_parametres_incorrects"


def tests_placement_et_de_retrait_de_jeton():
    # TODO
    # Création d'une case
    case = Case()
    # Création d'un jeton
    jeton = Jeton("A", 1)

    # Test du placement d'un jeton sur la case
    case.placer_jeton(jeton)
    assert not case.est_vide(), "La case devrait être occupée après avoir placé un jeton"
    assert case.jeton_occupant == jeton, "Le jeton placé devrait être celui que nous avons inséré"

    # Test du retrait du jeton de la case
    jeton_retire = case.retirer_jeton()
    assert jeton_retire == jeton, "Le jeton retiré devrait être le même que celui placé précédemment"
    assert case.est_vide(), "La case devrait être vide après avoir retiré le jeton"
    assert case.jeton_occupant is None, "Le jeton retiré devrait être None"
    assert False, "Erreur: Compléter tests_placement_et_de_retrait_de_jeton"


def tests_de_la_valeur_du_jeton_sur_une_case_avec_multiplicateur_de_lettre():
    case_lettre_double = Case(multiplicateur=2, type_bonus="L")
    jeton = Jeton("A", 1)
    case_lettre_double.placer_jeton(jeton)
    assert (
        case_lettre_double.valeur_jeton() == jeton.valeur
    ), "Erreur: La valeur du jeton devrait correspondre à celle du jeton sans multiplication."


def tests_des_couleurs_et_des_descriptions_de_bonus():
    case_lettre_double = Case(multiplicateur=2, type_bonus="L")
    assert (
        case_lettre_double.texte_descriptif() == "Lettre\nDouble"
    ), "Erreur: La description de la case à lettre double est incorrecte."
    assert case_lettre_double.code_couleur_ansi() == 46
    assert (
        case_lettre_double.code_couleur_hex() == "#00c9ff"
    ), "Erreur: Le code couleur hexadécimal pour une case à lettre double est incorrect."


def tests_assertions():
    # Création d'une case standard et d'un jeton pour les tests
    case = Case()
    jeton = Jeton("A", 1)

    # Placement d'un jeton sur une case vide
    case.placer_jeton(jeton)
    assert (
        not case.est_vide()
    ), "Erreur: La case devrait être occupée après le placement d'un jeton."

    # Test de placement d'un jeton sur une case déjà occupée
    try:
        case.placer_jeton(Jeton("B", 2))
        assert False, "Erreur: Une AssertionError aurait dû être levée car la case est déjà occupée."
    except AssertionError:
        pass  # succès

    # Test de retrait d'un jeton d'une case vide
    # D'abord, retirons le jeton existant
    case.retirer_jeton()
    try:
        case.retirer_jeton()
        assert (
            False
        ), "Erreur: Une AssertionError aurait dû être levée car la case est vide."
    except AssertionError:
        pass  # succès

    # Test de récupération de la valeur d'un jeton d'une case vide
    try:
        _ = case.valeur_jeton()
        assert False, "Erreur: Une AssertionError aurait dû être levée car aucun jeton n'est présent."
    except AssertionError:
        pass  # succès

    # Test de récupération de la lettre d'un jeton d'une case vide
    try:
        _ = case.lettre_jeton()
        assert False, "Erreur: Une AssertionError aurait dû être levée car aucun jeton n'est présent."
    except AssertionError:
        pass  # succès


def tests():
    tests_initialisation_case_sans_bonus()
    tests_initialisation_avec_des_parametres_incorrects()
    tests_placement_et_de_retrait_de_jeton()
    tests_de_la_valeur_du_jeton_sur_une_case_avec_multiplicateur_de_lettre()
    tests_des_couleurs_et_des_descriptions_de_bonus()
    tests_assertions()


if __name__ == "__main__":
    print('Tests unitaires de la classe "Case"...')

    tests()

    print("Tests unitaires passés avec succès!")
