from scrabble.jeton import Jeton


def tests_initialisation_jeton_avec_des_valeurs_valides():
    jeton = Jeton("X", 10)
    assert (
        jeton.lettre == "X" and jeton.valeur == 10
    ), "Erreur d'initialisation avec des paramètres valides"


def tests_erreurs_sur_la_lettre():
    try:
        Jeton("a", 5)
        assert False, "Erreur : une lettre minuscule a été acceptée"
    except AssertionError:
        pass  # succès

    try:
        Jeton("1", 5)
        assert False, "Erreur : un chiffre a été accepté comme lettre"
    except AssertionError:
        pass  # succès

    try:
        Jeton("AB", 5)
        assert False, "Erreur : une chaîne de plus d'une lettre a été acceptée"
    except AssertionError:
        pass  # succès


def tests_erreurs_sur_la_valeur():
    try:
        Jeton("A", -1)
        assert False, "Erreur : une valeur négative a été acceptée"
    except AssertionError:
        pass  # succès

    try:
        Jeton("A", 21)
        assert False, "Erreur : une valeur hors des limites autorisées a été acceptée"
    except AssertionError:
        pass  # succès


def tests_de_la_representation_du_jeton():
    jeton_valeur_un_chiffre = Jeton("M", 2)
    jeton_valeur_deux_chiffres = Jeton("Z", 10)
    assert (
        str(jeton_valeur_un_chiffre) == "M₂"
    ), "Erreur dans la représentation du jeton avec une valeur à un chiffre"
    assert (
        str(jeton_valeur_deux_chiffres) == "Z₁₀"
    ), "Erreur dans la représentation du jeton avec une valeur à deux chiffres"


def tests():
    tests_initialisation_jeton_avec_des_valeurs_valides()
    tests_erreurs_sur_la_lettre()
    tests_erreurs_sur_la_valeur()
    tests_de_la_representation_du_jeton()


if __name__ == "__main__":
    print('Tests unitaires de la classe "Jeton"...')

    tests()

    print("Tests unitaires passés avec succès!")
