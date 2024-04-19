from scrabble.plateau.plateau import Plateau
from scrabble.plateau.case import Case
from scrabble.common.position import Position
from scrabble.jeton import Jeton


def tests_initialisation_plateau():
    plateau = Plateau()
    assert (
        plateau.n_lignes == 15 and plateau.n_colonnes == 15
    ), "Erreur: Les dimensions du plateau sont incorrectes."

    # Vérification que toutes les cases sont correctement initialisées et vides
    for position in plateau.cases:
        assert isinstance(
            plateau.cases[position], Case
        ), "Erreur: Une case du plateau n'est pas une instance de Case."
        assert plateau.case_est_vide(
            position
        ), "Erreur: Les cases doivent être initialement vides."

    # Vérification des bonus spécifiques sur le plateau: cases "mot compte triple"
    for i, j in [(0, 0), (0, 7), (0, 14), (7, 0), (7, 14), (14, 0), (14, 7), (14, 14)]:
        mot_compte_triple = plateau.cases[Position(i, j)]
        assert (
            mot_compte_triple.type_bonus == "M"
            and mot_compte_triple.multiplicateur == 3
        ), "Erreur: Bonus incorrect pour la case mot compte triple."

    # Vérification des bonus spécifiques sur le plateau: cases "mot compte triple"
    for i, j in [
        (1, 5),
        (1, 9),
        (5, 1),
        (5, 5),
        (5, 9),
        (5, 13),
        (9, 1),
        (9, 5),
        (9, 9),
        (9, 13),
        (13, 5),
        (13, 9),
    ]:
        lettre_compte_triple = plateau.cases[Position(i, j)]
        assert (
            lettre_compte_triple.type_bonus == "L"
            and lettre_compte_triple.multiplicateur == 3
        ), "Erreur: Bonus incorrect pour la case lettre compte triple."

    # Vérification des bonus spécifiques sur le plateau: cases "mot compte double"
    for i in [1, 2, 3, 4]:
        assert (
            plateau.cases[Position(i, i)].type_bonus == "M"
            and plateau.cases[Position(i, i)].multiplicateur == 2
        ), "Erreur: Bonus incorrect pour la case mot compte double."
        assert (
            plateau.cases[Position(i, plateau.n_colonnes - i - 1)]
            and plateau.cases[Position(i, plateau.n_colonnes - i - 1)].multiplicateur
            == 2
        ), "Erreur: Bonus incorrect pour la case mot compte double."
        assert (
            plateau.cases[
                Position(plateau.n_lignes - i - 1, plateau.n_colonnes - i - 1)
            ]
            and plateau.cases[
                Position(plateau.n_lignes - i - 1, plateau.n_colonnes - i - 1)
            ].multiplicateur
            == 2
        ), "Erreur: Bonus incorrect pour la case mot compte double."
        assert (
            plateau.cases[Position(plateau.n_lignes - i - 1, i)]
            and plateau.cases[Position(plateau.n_lignes - i - 1, i)].multiplicateur == 2
        ), "Erreur: Bonus incorrect pour la case mot compte double."

    # Vérification des bonus spécifiques sur le plateau: cases "lettre compte double"
    for i, j in [(1, 1), (4, 0), (0, 4), (5, 1), (1, 5), (7, 4)]:
        assert (
            plateau.cases[Position(7 - i, 7 - j)].type_bonus == "L"
            and plateau.cases[Position(7 - i, 7 - j)].multiplicateur == 2
        ), "Erreur: Bonus incorrect pour la case lettre compte double."
        assert (
            plateau.cases[Position(7 - i, 7 + j)].type_bonus == "L"
            and plateau.cases[Position(7 - i, 7 + j)].multiplicateur == 2
        ), "Erreur: Bonus incorrect pour la case lettre compte double."
        if (i, j) not in [(0, 4), (4, 0), (5, 1), (7, 4)]:
            assert (
                plateau.cases[Position(7 + i, 7 - i)].type_bonus == "L"
                and plateau.cases[Position(7 + i, 7 - i)].multiplicateur == 2
            ), "Erreur: Bonus incorrect pour la case lettre compte double."
        if (i, j) not in [(0, 4), (4, 0), (5, 1), (7, 4)]:
            assert (
                plateau.cases[Position(7 - i, 7 + i)].type_bonus == "L"
                and plateau.cases[Position(7 - i, 7 + i)].multiplicateur == 2
            ), "Erreur: Bonus incorrect pour la case lettre compte double."
        assert (
            plateau.cases[Position(7 + i, 7 + j)].type_bonus == "L"
            and plateau.cases[Position(7 + i, 7 + j)].multiplicateur == 2
        ), "Erreur: Bonus incorrect pour la case lettre compte double."
        assert (
            plateau.cases[Position(7 + i, 7 - j)].type_bonus == "L"
            and plateau.cases[Position(7 + i, 7 - j)].multiplicateur == 2
        ), "Erreur: Bonus incorrect pour la case lettre compte double."

    # Vérification du bonus de la case centrale "mot compte double"
    assert (
        plateau.cases[Position(7, 7)].type_bonus == "M"
        and plateau.cases[Position(7, 7)].multiplicateur == 2
    ), "Erreur: Bonus incorrect pour la case centrale mot compte double."


def tests_methode_position_est_valide():
    plateau = Plateau()

    assert plateau.position_est_valide(
        Position(0, 0)
    ), "Erreur: La position (0, 0) devrait être valide."
    assert not plateau.position_est_valide(
        Position(-1, 0)
    ), "Erreur: La position (-1, 0) devrait être invalide."
    assert not plateau.position_est_valide(
        Position(15, 15)
    ), "Erreur: La position (15, 15) devrait être invalide."


def tests_methode_est_vide():
    plateau = Plateau()

    assert (
        plateau.est_vide()
    ), "Erreur: Le plateau devrait être vide à l'initialisation."

    # Test d'ajout et de retrait de jeton
    jeton = Jeton("A", 1)
    position_valide = Position(7, 7)
    position_invalide = Position(15, 15)

    assert plateau.ajouter_jeton(
        jeton, position_valide
    ), "Erreur: Le jeton devrait être ajouté avec succès."
    assert (
        not plateau.est_vide()
    ), "Erreur: Le plateau devrait être vide à l'initialisation."
    assert not plateau.case_est_vide(
        position_valide
    ), "Erreur: La case ne devrait plus être vide après l'ajout du jeton."
    assert not plateau.ajouter_jeton(
        jeton, position_invalide
    ), "Erreur: Ne devrait pas pouvoir ajouter un jeton à une position invalide."

    # Retirer le jeton ajouté
    assert isinstance(
        plateau.retirer_jeton(position_valide), Jeton
    ), "Erreur: Devrait retourner le jeton ajouté."
    assert plateau.case_est_vide(
        position_valide
    ), "Erreur: La case devrait être vide après le retrait du jeton."
    assert plateau.est_vide(), "Erreur: Le plateau devrait être de nouveau vide."


def tests_methode_cases_adjacentes_occupees():
    plateau = Plateau()

    # Validation des cases adjacentes
    assert not plateau.cases_adjacentes_occupees(
        Position(7, 7)
    ), "Erreur: Aucune case voisine ne devrait être occupée au début."

    # Ajouter des jetons pour tester les cases adjacentes
    plateau.ajouter_jeton(Jeton("B", 2), Position(7, 8))

    assert plateau.cases_adjacentes_occupees(
        Position(7, 7)
    ), "Erreur: Devrait détecter qu'une case voisine est maintenant occupée."


def tests_ajouter_jeton_en_jeu():
    plateau = Plateau()
    jeton_1 = Jeton("A", 1)
    jeton_2 = Jeton("B", 3)
    position_centre = Position(7, 7)
    position_invalide = Position(20, 20)

    assert plateau.ajouter_jeton_en_jeu(
        jeton_1, position_centre
    ), "Erreur: Le jeton devrait être ajouté en jeu avec succès."
    assert not plateau.ajouter_jeton_en_jeu(
        jeton_2, position_centre
    ), "Erreur: Ne devrait pas pouvoir ajouter un deuxième jeton à la même position en jeu."
    assert not plateau.ajouter_jeton_en_jeu(
        jeton_2, position_invalide
    ), "Erreur: Ne devrait pas pouvoir ajouter un jeton à une position invalide."


def tests_consulter_jetons_en_jeu():
    plateau = Plateau()
    jeton = Jeton("A", 1)
    position_centre = Position(7, 7)

    plateau.ajouter_jeton_en_jeu(jeton, position_centre)
    jetons_en_jeu, positions_en_jeu = plateau.consulter_jetons_en_jeu()

    assert (
        jetons_en_jeu == [jeton] and positions_en_jeu == [position_centre]
    ), "Erreur: La consultation des jetons en jeu devrait renvoyer le jeton et la position corrects."


def tests_retirer_jetons_en_jeu():
    plateau = Plateau()
    jeton = Jeton("A", 1)
    position_centre = Position(7, 7)

    plateau.ajouter_jeton_en_jeu(jeton, position_centre)
    jetons_retires, positions_retirees = plateau.retirer_jetons_en_jeu()
    assert jetons_retires == [jeton] and positions_retirees == [
        position_centre
    ], "Erreur: Les jetons et positions retirés devraient correspondre à ceux ajoutés."
    assert plateau.consulter_jetons_en_jeu() == (
        [],
        [],
    ), "Erreur: Il ne devrait plus y avoir de jetons en jeu après le retrait."


def tests_valider_positions_avant_ajout():
    plateau = Plateau()

    positions_valides = [Position(7, i) for i in range(7, 10)]
    positions_invalides = [Position(7, 7), Position(8, 8), Position(20, 20)]

    assert plateau.valider_positions_avant_ajout(
        positions_valides
    ), "Erreur: Les positions devraient être validées pour l'ajout."
    assert not plateau.valider_positions_avant_ajout(
        positions_invalides
    ), "Erreur: Les positions devraient être invalidées pour l'ajout."


def tests_placer_jetons():
    plateau = Plateau()

    jeton_1 = Jeton("A", 1)
    jeton_2 = Jeton("B", 3)

    assert plateau.placer_jetons(
        [jeton_1, jeton_2], [Position(7, 7), Position(7, 8)]
    ) == (["AB"], 8), "Erreur: Les jetons devraient être placés avec succès."


def tests_trouver_mots_et_calculer_points():
    plateau = Plateau()
    jeton_1 = Jeton("A", 1)
    jeton_2 = Jeton("B", 3)
    plateau.placer_jetons([jeton_1, jeton_2], [Position(7, 7), Position(7, 8)])
    plateau.ajouter_jeton(Jeton("C", 3), Position(7, 9))
    mots, points = plateau.trouver_mots_et_calculer_points(
        [Position(7, 7), Position(7, 8), Position(7, 9)]
    )

    assert "ABC" in mots, "Erreur: Le mot formé devrait être détecté."
    assert points > 0, "Erreur: Des points devraient être calculés pour le mot formé."


def tests_calculer_mots_et_points_ligne_ou_colonne():
    plateau = Plateau()
    jeton_1 = Jeton("A", 1)
    jeton_2 = Jeton("B", 3)
    plateau.placer_jetons([jeton_1, jeton_2], [Position(7, 7), Position(7, 8)])
    plateau.ajouter_jeton(Jeton("C", 3), Position(7, 9))
    mots, points = plateau.calculer_mots_et_points_ligne_ou_colonne(
        [Position(7, 7), Position(7, 8), Position(7, 9)], ligne=7
    )

    assert "ABC" in mots, "Erreur: Le mot 'ABC' devrait être calculé sur la ligne 7."
    assert (
        points > 0
    ), "Erreur: Des points devraient être calculés pour le mot sur la ligne 7."


def tests():
    tests_initialisation_plateau()
    tests_methode_position_est_valide()
    tests_methode_est_vide()
    tests_methode_cases_adjacentes_occupees()
    tests_ajouter_jeton_en_jeu()
    tests_consulter_jetons_en_jeu()
    tests_retirer_jetons_en_jeu()
    tests_valider_positions_avant_ajout()
    tests_placer_jetons()
    tests_trouver_mots_et_calculer_points()
    tests_calculer_mots_et_points_ligne_ou_colonne()


if __name__ == "__main__":
    print('Tests unitaires de la classe "Plateau"...')

    tests()

    print("Tests unitaires passés avec succès!")
