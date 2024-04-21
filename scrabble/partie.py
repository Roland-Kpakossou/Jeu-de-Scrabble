import random
from pathlib import Path
from scrabble.joueur import Joueur
from scrabble.plateau import Plateau
from scrabble.jeton import Jeton


DOSSIER_RACINE = Path(__file__).resolve().parent.parent


class Partie:
    """
    Gère une partie de Scrabble, incluant l'initialisation du jeu, la gestion des joueurs,
    la distribution des jetons, et le déroulement des tours jusqu'à la détermination du gagnant.

    Cette classe est responsable de la création du plateau de jeu, de l'initialisation des joueurs,
    et de la gestion de la logique de jeu conformément aux règles du Scrabble. Elle contrôle également
    le flux de jeu en passant d'un joueur à l'autre et en vérifiant la validité des mots placés sur le plateau.

    Attributes:
        plateau (Plateau): Le plateau de jeu où les jetons sont placés pour former des mots.
        joueurs (list[Joueur]): Liste des joueurs participant à la partie.
        joueur_actif (Joueur): Le joueur qui est actuellement en train de jouer son tour.
        jetons_libres (list[Jeton]): La réserve de jetons qui reste à distribuer aux joueurs.
        dictionnaire (set[str]): Un ensemble de mots valides, chargé à partir d'un fichier de dictionnaire.
    """

    def __init__(self, nombre_de_joueurs=2, langue="fr"):
        """
        Initialise une nouvelle partie de Scrabble avec un nombre spécifié de joueurs et une langue.

        Args:
            nombre_de_joueurs (int): Le nombre de joueurs dans la partie, doit être entre 2 et 4.
            langue (str): La langue utilisée pour les mots du jeu, actuellement supporte 'fr' (français) et 'en' (anglais).

        Raises:
            AssertionError: Si la langue n'est pas supportée ou si le nombre de joueurs est hors des limites.
        """
        assert langue.lower() in ["fr", "en"], "Langue non supportée."
        assert 2 <= nombre_de_joueurs <= 4, "Il faut entre 2 et 4 personnes pour jouer."

        self.plateau = Plateau()

        self.joueurs = [Joueur(f"Joueur {i + 1}") for i in range(nombre_de_joueurs)]
        self.joueur_actif = random.choice(self.joueurs)

        # Source: https://fr.wikipedia.org/wiki/Lettres_du_Scrabble
        chemin_fichier_dictionnaire = (
            DOSSIER_RACINE / "ressources" / "dictionnaire_francais.txt"
        )
        distribution_lettres = [
            ("E", 15, 1),
            ("A", 9, 1),
            ("I", 8, 1),
            ("N", 6, 1),
            ("O", 6, 1),
            ("R", 6, 1),
            ("S", 6, 1),
            ("T", 6, 1),
            ("U", 6, 1),
            ("L", 5, 1),
            ("D", 3, 2),
            ("M", 3, 2),
            ("G", 2, 2),
            ("B", 2, 3),
            ("C", 2, 3),
            ("P", 2, 3),
            ("F", 2, 4),
            ("H", 2, 4),
            ("V", 2, 4),
            ("J", 1, 8),
            ("Q", 1, 8),
            ("K", 1, 10),
            ("W", 1, 10),
            ("X", 1, 10),
            ("Y", 1, 10),
            ("Z", 1, 10),
        ]

        if langue.upper() == "en":
            chemin_fichier_dictionnaire = (
                DOSSIER_RACINE / "ressources" / "dictionnaire_anglais.txt"
            )
            distribution_lettres = [
                ("E", 12, 1),
                ("A", 9, 1),
                ("I", 9, 1),
                ("N", 6, 1),
                ("O", 8, 1),
                ("R", 6, 1),
                ("S", 4, 1),
                ("T", 6, 1),
                ("U", 4, 1),
                ("L", 4, 1),
                ("D", 4, 2),
                ("M", 2, 3),
                ("G", 3, 2),
                ("B", 2, 3),
                ("C", 2, 3),
                ("P", 2, 3),
                ("F", 2, 4),
                ("H", 2, 4),
                ("V", 2, 4),
                ("J", 1, 8),
                ("Q", 1, 10),
                ("K", 1, 5),
                ("W", 2, 4),
                ("X", 1, 8),
                ("Y", 2, 4),
                ("Z", 1, 10),
            ]

        self.jetons_libres = []
        for lettre, occurences, valeur in distribution_lettres:
            for _ in range(occurences):
                self.jetons_libres.append(Jeton(lettre, valeur))

        with open(chemin_fichier_dictionnaire, "r") as fichier:
            self.dictionnaire = set(ligne.strip().upper() for ligne in fichier)

    def melanger_jetons_chevalet_du_joueur_actif(self):
        """
        Mélange les jetons sur le chevalet du joueur actif et annule tous les déplacements en attente.
        """
        self.annuler_deplacements_en_attente()
        self.joueur_actif.chevalet.melanger_jetons()

    def mot_permis(self, mot):
        """
        Vérifie si un mot est permis en le recherchant dans le dictionnaire de la partie.

        Args:
            mot (str): Le mot à vérifier.

        Returns:
            bool: True si le mot est dans le dictionnaire, False sinon.
        """
        # TODO
        with open("dictionnaire_francais.txt", "r") as fichier:
            if mot in fichier.read():
                return True
            else:
                return False

    def determiner_gagnant(self):
        """
        Détermine le gagnant de la partie en comparant les scores des joueurs.

        Returns:
            Joueur: Le joueur avec le score le plus élevé.

        Note: Si plusieurs sont à égalité, on en retourne un seul parmi ceux-ci.
        """
        # TODO
        # Initialise le joueur avec le score le plus élevé au premier joueur
        joueur_gagnant = self.joueurs[0]

        # Parcourt tous les joueurs pour trouver celui avec le score le plus élevé
        for joueur in self.joueurs:
            # Si le score du joueur actuel est plus élevé que celui du joueur gagnant actuel
            if joueur.score > joueur_gagnant.score:
                # Met à jour le joueur gagnant
                joueur_gagnant = joueur

        # Retourne le joueur avec le score le plus élevé
        return joueur_gagnant

    def est_terminee(self):
        """
        Vérifie si la partie est terminée, ce qui peut arriver si tous les jetons ont été utilisés
        ou s'il y a moins de deux joueurs.

        Returns:
            bool: True si la partie est terminée, False sinon.

        Note: C'est la règle que nous avons choisi d'utiliser pour ce travail, donc vous pouvez ignorer les autres
        reègles que vous connaissez ou avez lu sur Internet.
        """
        return len(self.jetons_libres) == 0 or len(self.joueurs) < 2

    def passer_au_joueur_suivant(self):
        """
        Passe le tour au joueur suivant dans la séquence et lui tire de nouveaux jetons si nécessaire.

        Note: Le nouveau joueur actif est celui à l'index du joueur actif + 1, le tout modulo le nombre de joueurs.
        """
        self.joueur_actif = self.joueurs[
            (self.joueurs.index(self.joueur_actif) + 1) % len(self.joueurs)
        ]

        if self.joueur_actif.peut_tirer_de_nouveaux_jetons():
            for jeton in self.tirer_jetons(
                self.joueur_actif.nombre_de_nouveaux_jetons_a_tirer()
            ):
                self.joueur_actif.chevalet.ajouter_jeton(jeton)

    def tirer_jetons(self, n):
        """
        Tire un nombre spécifié de jetons du sac de jetons disponibles.

        Args:
            n (int): Le nombre de jetons à tirer.

        Returns:
            list: Les jetons tirés.

        Raises:
            AssertionError: Si le nombre spécifié est invalide (négatif ou supérieur au nombre de jetons disponibles).

        Note: Il s'agit de prendre au hasard des jetons dans self.jetons_libres et de les retourner.
        """
        assert (
            0 <= n <= len(self.jetons_libres)
        ), "n doit être compris entre 0 et le nombre total de jetons libres."
        random.shuffle(self.jetons_libres)
        res = self.jetons_libres[:n]
        self.jetons_libres = self.jetons_libres[n:]
        return res

    def deplacer_jeton_du_chevalet_au_plateau(
        self, emplacement_source_chevalet, position_destination_plateau
    ):
        """
        Déplace un jeton du chevalet du joueur actif vers une position spécifiée sur le plateau.

        Args:
            emplacement_source_chevalet (int): L'index du jeton sur le chevalet.
            position_destination_plateau (Position): La position cible sur le plateau.

        Returns:
            bool: True si le jeton a été placé avec succès, False sinon (retour au chevalet si échoué).
        """
        jeton = self.joueur_actif.chevalet.retirer_jeton(emplacement_source_chevalet)

        if not self.plateau.ajouter_jeton_en_jeu(jeton, position_destination_plateau):
            self.joueur_actif.chevalet.ajouter_jeton(jeton, emplacement_source_chevalet)
            return False

        return True

    def annuler_deplacements_en_attente(self):
        """
        Annule tous les déplacements de jetons qui n'ont pas encore été finalisés sur le plateau.
        """
        liste_jetons, liste_positions = self.plateau.retirer_jetons_en_jeu()

        for position in liste_positions:
            self.plateau.retirer_jeton(position)

        for jeton in liste_jetons:
            self.joueur_actif.chevalet.ajouter_jeton(jeton)

    def appliquer_deplacements_en_attente(self):
        """
        Applique et finalise tous les déplacements en attente, retirant les jetons de la liste temporaire en jeu.
        """
        self.plateau.retirer_jetons_en_jeu()

    def jouer_un_tour(self):
        """
        Exécute le processus de jeu pour un tour, en plaçant des jetons et en validant la formation des mots.

        Returns:
            tuple: Un booléen indiquant si le tour a réussi et un message décrivant le résultat du tour.
        """
        # TODO
        # Étape 1: Vérifier la validité des placements
        liste_jetons, liste_positions = self.plateau.consulter_jetons_en_jeu()
        mots_formes, points = self.plateau.placer_jetons(liste_jetons, liste_positions)

        if not mots_formes:  # Si aucun mot formé ou mot invalide
            self.annuler_deplacements_en_attente()
            return False, "Placement invalide ou aucun mot formé."

        # Étape 2: Vérifier si tous les mots formés sont valides
        for mot in mots_formes:
            if not self.mot_permis(mot):
                self.annuler_deplacements_en_attente()
                return False, f"Le mot {mot} n'est pas valide selon le dictionnaire."

        # Étape 3: Appliquer les points au score du joueur
        self.joueur_actif.score += points
        self.appliquer_deplacements_en_attente()

        # Étape 4: Passer au joueur suivant
        self.passer_au_joueur_suivant()

        # Étape 5: Vérifier la fin de la partie
        if self.est_terminee():
            gagnant = self.determiner_gagnant()
            return True, f"Partie terminée. Le gagnant est {gagnant.nom} avec un score de {gagnant.score} points."

        return True, f"Tour terminé avec succès. {points} points ajoutés au score. C'est maintenant au tour de {self.joueur_actif.nom}."