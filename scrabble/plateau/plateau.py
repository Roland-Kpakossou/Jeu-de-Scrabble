from scrabble.plateau.case import Case
from scrabble.jeton import Jeton
from scrabble.common.position import Position


class Plateau:
    """Représente le plateau de jeu, incluant la gestion des cases et des placements de jetons.

    Attributes:
        n_lignes (int): Le nombre de lignes du plateau, fixé à 15 pour le Scrabble standard.
        n_colonnes (int): Le nombre de colonnes du plateau, également fixé à 15.
        cases (dict[Position, Case]): Un dictionnaire associant chaque position sur le plateau à un objet Case.
        jetons_en_jeu (list[Jeton]): Liste temporaire des jetons placés sur le plateau par le joueur actuel durant son
                                     tour. Ces jetons ne sont pas encore validés et peuvent être modifiés ou retirés
                                     avant la validation du tour.
        positions_en_jeu (list[Position]): Liste des positions occupées par les `jetons_en_jeu`. Chaque position est une
                                           instance de la classe `Position`, indiquant les coordonnées spécifiques d'un
                                           jeton sur le plateau.
    """

    def __init__(self):
        """Initialise le plateau de jeu avec des cases standard et spéciales selon les règles du Scrabble."""
        # Nombre de lignes et de colonnes du plateau de Scrabble
        self.n_lignes = 15
        self.n_colonnes = 15

        # Initialisation du dictionnaire pour stocker les cases du plateau
        # La clé est un objet Position et la valeur est un objet Case
        self.cases = {}

        # Remplir le plateau avec des cases vides standard
        for ligne in range(self.n_lignes):
            for colonne in range(self.n_colonnes):
                self.cases[Position(ligne, colonne)] = Case()

        # Définir les cases "lettre compte triple"
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
            self.cases[Position(i, j)] = Case(3, "L")

        # Définir des cases "lettre compte double" en formant un motif autour du centre
        for i, j in [(1, 1), (4, 0), (0, 4), (5, 1), (1, 5), (7, 4), (4, 7)]:
            self.cases[Position(7 - i, 7 - j)] = Case(2, "L")
            self.cases[Position(7 - i, 7 + j)] = Case(2, "L")
            self.cases[Position(7 + i, 7 - i)] = Case(2, "L")
            self.cases[Position(7 - i, 7 + i)] = Case(2, "L")
            self.cases[Position(7 + i, 7 + j)] = Case(2, "L")
            self.cases[Position(7 + i, 7 - j)] = Case(2, "L")

        # Définir les cases "mot compte double" en diagonale depuis chaque coin
        for i in [1, 2, 3, 4]:
            self.cases[Position(i, i)] = Case(2, "M")
            self.cases[Position(i, self.n_colonnes - i - 1)] = Case(2, "M")
            self.cases[Position(self.n_lignes - i - 1, self.n_colonnes - i - 1)] = Case(
                2, "M"
            )
            self.cases[Position(self.n_lignes - i - 1, i)] = Case(2, "M")

        # Définir les cases "mot compte triple" aux positions spécifiques
        for i, j in [
            (0, 0),
            (0, 7),
            (0, 14),
            (7, 0),
            (7, 14),
            (14, 0),
            (14, 7),
            (14, 14),
        ]:
            self.cases[Position(i, j)] = Case(3, "M")

        # La case centrale du plateau, qui est une case "mot compte double"
        self.cases[Position(7, 7)] = Case(2, "M")

        # Initialise une liste vide pour stocker temporairement les jetons placés sur le plateau pendant le tour actuel.
        self.jetons_en_jeu = []

        # Initialise une liste vide pour stocker les positions des jetons qui sont temporairement en jeu
        # pendant le tour actuel.
        self.positions_en_jeu = []

    def position_est_valide(self, position):
        """Vérifie si une position donnée est valide sur le plateau.

        Args:
            position (Position): La position à vérifier.

        Returns:
            bool: True si la position est dans les limites du plateau, False sinon.
        """
        # TODO
        if 0 <= position.ligne < self.n_lignes and 0 <= position.colonne < self.n_colonnes:
            return True
        else:
            return False

    def case_est_vide(self, position):
        """Vérifie si une case à une position donnée est vide.

        Args:
            position (Position): La position de la case à vérifier.

        Returns:
            bool: True si la case est vide, False sinon.
        """
        return self.cases[position].est_vide()

    def est_vide(self):
        """Vérifie si le plateau est entièrement vide (autrement dit, si toutes les cases du plateau sont vides).

        Returns:
            bool: True si le plateau est entièrement vide, False sinon.
        """
        # TODO
        for position in self.cases:
            if not self.case_est_vide(position):
                return False
        return True

    def ajouter_jeton(self, jeton, position):
        """
        Place un jeton sur une case vide du plateau.

        Args:
            jeton (Jeton): Le jeton à placer.
            position (Position): La position sur le plateau où placer le jeton.

        Returns:
            bool: True si le jeton a été placé avec succès; False sinon (si la case est déjà occupée).
        """
        # TODO
        if self.case_est_vide(position):
            self.cases[position].placer_jeton(jeton)
            return True
        else:
            return False

    def retirer_jeton(self, position):
        """Retire un jeton de la position donnée sur le plateau.

        Args:
            position (Position): La position du jeton à retirer.

        Returns:
             Jeton: Le jeton retiré de la position spécifiée, ou None si la case est vide.
        """
        # TODO
        if self.position_est_valide(position):
            # Vérifie si la case à la position donnée contient un jeton
            if not self.case_est_vide(position):
                # récupère le jeton et le retire de la case
                jeton_retire = self.cases[position]
                self.cases[position] = Case()  # Remplace le jeton par une case vide
                return jeton_retire
            else:
                return None
        else:
            return None

    def cases_adjacentes_occupees(self, position):
        """
        Étant donné une position, cette méthode permet de voir si au moins l'une de ses positions voisines est occupée.
        Les cases voisines sont les cases juste en haut, en bas, à gauche et à droite de la case concernée.
        NB: Les cases voisines diagonales ne comptent pas.

        Args:
            position (Position): La position autour de laquelle vérifier les cases voisines.

        Returns:
            bool: True si au moins une case adjacente est occupée, False sinon.
        """
        positions_adjacentes = position.obtenir_quatre_positions_adjacentes()
        positions_adjacentes_valides = [
            position
            for position in positions_adjacentes
            if self.position_est_valide(position)
        ]
        return any(
            [
                not self.case_est_vide(position)
                for position in positions_adjacentes_valides
            ]
        )

    def valider_positions_avant_ajout(self, positions):
        """Vérifie si un ensemble de positions est valide pour placer des jetons de manière consécutive.

        Args:
            positions (list[Position]): Liste des positions à vérifier.

        Returns:
            bool: True si l'ensemble des positions est valide pour l'ajout, False sinon.
        """
        # Extraire les numéros de lignes et de colonnes des positions proposées
        lignes = [position.ligne for position in positions]
        colonnes = [position.colonne for position in positions]

        # Supprimer les doublons pour voir si les positions sont sur la même ligne/colonne
        lignes_uniques = list(set(lignes))
        colonnes_uniques = list(set(colonnes))

        # Vérifier si toutes les positions sont sur une même ligne ou une même colonne
        sur_meme_ligne = len(lignes_uniques) == 1
        sur_meme_colonne = len(colonnes_uniques) == 1

        # L'ajout est initialement valide si toutes les positions sont alignées et chaque case est vide
        ajout_valide = (sur_meme_ligne or sur_meme_colonne) and all(
            [self.case_est_vide(position) for position in positions]
        )

        # Si l'ajout est toujours considéré valide
        if ajout_valide:
            # Si le plateau est vide, une des positions doit être le centre du plateau
            if self.est_vide():
                ajout_valide = Position(7, 7) in positions
            else:
                # Sinon, au moins une des positions doit être adjacente à une case déjà occupée
                ajout_valide = any(
                    [self.cases_adjacentes_occupees(position) for position in positions]
                )

            # Si l'ajout est sur la même ligne, vérifier qu'aucune case entre les positions n'est vide
            if ajout_valide and sur_meme_ligne:
                ligne_concernee = lignes_uniques[0]
                colonne_min, colonne_max = min(colonnes), max(colonnes)
                ajout_valide = all(
                    [
                        not self.case_est_vide(Position(ligne_concernee, i))
                        for i in range(colonne_min, colonne_max + 1)
                        if i not in colonnes
                    ]
                )
            # Si l'ajout est sur la même colonne, appliquer la même vérification pour les lignes
            elif ajout_valide and sur_meme_colonne:
                colonne_concernee = colonnes_uniques[0]
                ligne_min, ligne_max = min(lignes), max(lignes)
                ajout_valide = all(
                    [
                        not self.case_est_vide(Position(i, colonne_concernee))
                        for i in range(ligne_min, ligne_max + 1)
                        if i not in lignes
                    ]
                )

        return ajout_valide

    def ajouter_jeton_en_jeu(self, jeton, position):
        """
        Ajoute un jeton à la liste temporaire des jetons en jeu pour un tour actuel,
        en vérifiant que la position est valide et la case est vide.

        Args:
            jeton (Jeton): Le jeton à ajouter.
            position (Position): La position sur le plateau où le jeton doit être placé.

        Returns:
            bool: True si le jeton a été ajouté avec succès, False sinon.
        """
        if not self.position_est_valide(position):
            return False

        if not self.case_est_vide(position) or position in self.positions_en_jeu:
            return False

        self.positions_en_jeu.append(position)
        self.jetons_en_jeu.append(jeton)

        return True

    def consulter_jetons_en_jeu(self):
        """
        Renvoie les jetons et les positions actuellement en jeu dans le tour actuel.

        Returns:
            tuple: Un tuple contenant deux listes, une de jetons et l'autre de leurs positions correspondantes.
        """
        return self.jetons_en_jeu, self.positions_en_jeu

    def retirer_jetons_en_jeu(self):
        """
        Retire tous les jetons actuellement en jeu, réinitialisant ainsi les jetons et positions pour le tour.

        Returns:
            tuple: Un tuple contenant les jetons retirés et leurs positions.
        """
        jetons, positions = self.consulter_jetons_en_jeu()

        self.jetons_en_jeu = []
        self.positions_en_jeu = []

        return jetons, positions

    def placer_jetons(self, jetons_a_placer, positions):
        """Place plusieurs jetons sur le plateau à des positions spécifiées et calcule les scores
        basés sur les mots formés par les placements.

        Args:
            jetons_a_placer (list[Jeton]): La liste des jetons à placer..
            positions (list[Position]): Les positions correspondantes sur le plateau.

        Returns:
            list[str]: Les mots formés après le placement des jetons.
            int: Le score total obtenu à partir des mots formés.

        Raises:
            AssertionError: Si le nombre de jetons ne correspond pas au nombre de positions, ou si les positions sont invalides.
        """
        assert len(jetons_a_placer) == len(
            positions
        ), "Le nombre de jetons est différent du nombre de positions."
        assert self.valider_positions_avant_ajout(
            positions
        ), "Les positions pour l'ajout sont invalides."

        # Parcourir chaque jeton et sa position correspondante pour les placer sur le plateau.
        # La méthode `ajouter_jeton` est appelée pour chaque couple jeton-position.
        for jeton, position in zip(jetons_a_placer, positions):
            self.ajouter_jeton(jeton, position)

        mots, points = self.trouver_mots_et_calculer_points(positions)

        return mots, points

    def trouver_mots_et_calculer_points(self, positions):
        """
        Identifie tous les mots nouvellement formés après un placement de jetons et calcule les points correspondants.

        Args:
            positions (list[Position]): Les positions où les jetons ont été placés récemment.

        Returns:
            tuple: Un tuple contenant une liste des mots formés et le total de points accumulés.
        """
        total_points = 0

        # Extraire les numéros de lignes et de colonnes des positions proposées
        lignes_affectees = [position.ligne for position in positions]
        colonnes_affectees = [position.colonne for position in positions]

        # Supprimer les doublons
        lignes_affectees_uniques = list(set(lignes_affectees))
        colonnes_affectees_uniques = list(set(colonnes_affectees))

        mots_formes = []

        # Pour chaque ligne affectée par les nouvelles positions,
        # calculer les mots formés et les points obtenus sur cette ligne.
        for ligne in lignes_affectees_uniques:
            mots, points = self.calculer_mots_et_points_ligne_ou_colonne(
                positions, ligne=ligne
            )
            mots_formes += mots
            total_points += points

        # Répéter le processus pour chaque colonne affectée par les nouvelles positions.
        for colonne in colonnes_affectees_uniques:
            mots, points = self.calculer_mots_et_points_ligne_ou_colonne(
                positions, colonne=colonne
            )
            mots_formes += mots
            total_points += points

        return mots_formes, total_points

    def calculer_mots_et_points_ligne_ou_colonne(
        self, positions, ligne=None, colonne=None
    ):
        """
        Évalue une ligne ou colonne pour identifier des mots formés et calculer les points après un ajout de jetons.

        Args:
            positions (list[Position]): Les positions de jetons récemment ajoutés.
            ligne (int, optional): Numéro de la ligne à évaluer.
            colonne (int, optional): Numéro de la colonne à évaluer.

        Returns:
            tuple: Liste des mots formés et le total de points obtenus sur la ligne ou colonne évaluée.

        Raises:
            AssertionError: Si ni ligne ni colonne n'est spécifiée, ou si les deux sont spécifiées.
        """

        # S'assurer que soit une ligne soit une colonne est spécifiée, mais pas les deux.
        assert (ligne is None) ^ (
            colonne is None
        ), "Précisez seulement la ligne ou la colonne, pas les deux."

        mots_formes, total_points = [], 0
        mot_en_cours, points_mot, multiplicateur_mot, positions_mot = "", 0, 1, []

        # Parcourir chaque case de la ligne ou de la colonne spécifiée.
        for i in range(
            self.n_lignes
        ):  # Utiliser n_lignes arbitrairement; n_colonnes aurait la même valeur.
            # Déterminer la position actuelle en fonction de si une ligne ou une colonne est spécifiée.
            position_actuelle = (
                Position(ligne, i) if ligne is not None else Position(i, colonne)
            )
            case = self.cases[position_actuelle]

            # Si la case est vide et que le mot en cours de formation a plus d'une lettre,
            # et qu'il inclut au moins une nouvelle lettre placée, ajouter ce mot à la liste des mots
            # et calculer les points.
            if case.est_vide():
                if len(mot_en_cours) > 1 and any(
                    position in positions_mot for position in positions
                ):
                    mots_formes.append(mot_en_cours)
                    total_points += points_mot * multiplicateur_mot

                # Réinitialiser les variables pour le prochain mot.
                mot_en_cours, points_mot, multiplicateur_mot, positions_mot = (
                    "",
                    0,
                    1,
                    [],
                )
            else:
                # Sinon, ajouter la lettre de la case au mot en cours de formation,
                # et ajuster les points et multiplicateurs selon le type de case.
                mot_en_cours += case.lettre_jeton()
                positions_mot.append(position_actuelle)
                points_actuels = (
                    case.valeur_jeton() * case.multiplicateur
                    if position_actuelle in positions and case.type_bonus == "L"
                    else case.valeur_jeton()
                )
                points_mot += points_actuels
                if position_actuelle in positions and case.type_bonus == "M":
                    multiplicateur_mot *= case.multiplicateur

        # Après avoir parcouru toutes les cases, vérifier une dernière fois si un mot
        # doit être ajouté à la liste des mots formés.
        if len(mot_en_cours) > 1 and any(
            position in positions_mot for position in positions
        ):
            mots_formes.append(mot_en_cours)
            total_points += points_mot * multiplicateur_mot

        return mots_formes, total_points

    def __str__(self):
        """
        Méthode spéciale indiquant à Python comment représenter une instance de Plateau par une chaîne de
        caractères. Notamment utilisé pour imprimer un plateau à l'écran.

        Returns:
            str: La représentation textuelle du plateau de jeu.
        """
        # Créer une ligne de séparation utilisée pour séparer les lignes du plateau,
        # composée de '+----+' répété pour chaque ligne du plateau.
        ligne_separation = "  +" + "----+" * self.n_lignes + "\n"

        # Initialiser la chaîne de caractères représentant le plateau avec les numéros de colonne
        # en en-tête. Chaque numéro de colonne est centré dans un espace de 5 caractères.
        representation_plateau = (
            "   "  # Espaces pour aligner avec les lettres des lignes.
        )
        for colonne in range(self.n_colonnes):
            representation_plateau += "{:^5d}".format(
                colonne + 1
            )  # Ajouter le numéro de la colonne (1-indexé).

        representation_plateau += "\n"  # Nouvelle ligne après les en-têtes de colonnes.
        representation_plateau += ligne_separation  # Ajouter la ligne de séparation.

        # Boucler sur chaque ligne du plateau pour ajouter les cases et leurs contenus.
        for ligne in range(self.n_lignes):
            lettre_ligne = chr(
                ord("A") + ligne
            )  # Convertir l'indice de la ligne en lettre.
            representation_plateau += "{} |".format(
                lettre_ligne
            )  # Ajouter la lettre de la ligne à gauche.

            # Parcourir chaque colonne de la ligne actuelle.
            for colonne in range(self.n_colonnes):
                case_actuelle = self.cases[
                    Position(ligne, colonne)
                ]  # Obtenir la case à la position courante.

                # Si la case est la case centrale du plateau et est vide, afficher une étoile
                # en utilisant un code de couleur spécifique (centre du plateau).
                if ligne == colonne and ligne == 7 and case_actuelle.est_vide():
                    contenu_case = "\x1b[0;30;{}m{:^4s}\x1b[0m".format(
                        case_actuelle.code_couleur_ansi(), "\u2605"
                    )
                else:
                    # Sinon, utiliser la représentation standard de la case (peut être vide ou contenir un jeton).
                    contenu_case = "{:^4s}".format(str(case_actuelle))

                representation_plateau += (
                    contenu_case + "|"
                )  # Ajouter la représentation de la case à la ligne.

            # Après avoir ajouté toutes les cases de la ligne, ajouter la lettre de la ligne à droite et le séparateur.
            representation_plateau += " {}\n".format(lettre_ligne)
            representation_plateau += ligne_separation

        # Ajouter de nouveau les numéros de colonne en bas pour faciliter la lecture.
        representation_plateau += (
            "   "  # Espaces pour aligner avec les lettres des lignes.
        )
        for colonne in range(self.n_colonnes):
            representation_plateau += "{:^5d}".format(colonne + 1)
        representation_plateau += "\n"  # Nouvelle ligne à la fin.

        return representation_plateau
