import tests_jeton
import tests_chevalet
import tests_joueur
import tests_position
import tests_case
import tests_plateau
import tests_partie


if __name__ == "__main__":
    print("Tests unitaires de l'ensemble du projet...")

    tests_jeton.tests()
    tests_chevalet.tests()
    tests_joueur.tests()
    tests_position.tests()
    tests_case.tests()
    tests_plateau.tests()
    tests_partie.tests()

    print("Tests unitaires passés avec succès!")
