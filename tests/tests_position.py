from scrabble.common.position import Position


def tests_initialisation_position():
    position = Position(3, 5)
    assert position.ligne == 3, "Erreur: La ligne n'est pas correctement initialisée."
    assert (
        position.colonne == 5
    ), "Erreur: La colonne n'est pas correctement initialisée."


def tests_egalite_positions():
    position = Position(3, 5)
    position_identique = Position(3, 5)
    position_different = Position(5, 3)
    assert (
        position == position_identique
    ), "Erreur: Les positions identiques ne sont pas considérées comme égales."
    assert (
        position != position_different
    ), "Erreur: Les positions différentes sont considérées comme égales."


def tests_hachages_positions():
    position = Position(3, 5)
    position_identique = Position(3, 5)
    position_different = Position(5, 3)

    assert hash(position) == hash(
        position_identique
    ), "Erreur: Les hachages des positions identiques devraient être égaux."
    assert hash(position) != hash(
        position_different
    ), "Erreur: Les hachages des positions différentes devraient être distincts."


def tests_positions_adjacentes():
    # TODO
    position_test = Position(3, 3)

    # Appel de la méthode obtenir_quatre_positions_adjacentes()
    positions_adjacentes = position_test.obtenir_quatre_positions_adjacentes()

    # Vérification des positions adjacentes attendues
    assert len(positions_adjacentes) == 4
    assert Position(3, 4) in positions_adjacentes  # Droite
    assert Position(3, 2) in positions_adjacentes  # Gauche
    assert Position(4, 3) in positions_adjacentes  # Bas
    assert Position(2, 3) in positions_adjacentes  # Haut

    print("Tests positions adjacentes réussis !")


def tests_representation_position():
    position = Position(3, 5)
    assert (
        repr(position) == "(3, 5)"
    ), "Erreur: La représentation textuelle de la position est incorrecte."


def tests():
    tests_initialisation_position()
    tests_egalite_positions()
    tests_hachages_positions()
    tests_positions_adjacentes()
    tests_representation_position()


if __name__ == "__main__":
    print('Tests unitaires de la classe "Position"...')

    tests()

    print("Tests unitaires passés avec succès!")
