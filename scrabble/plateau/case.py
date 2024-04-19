class Case:
    """Représente une case sur le plateau de Scrabble, qui peut affecter la valeur des lettres ou des mots.

    Attributes:
        multiplicateur (int): Le facteur par lequel la valeur du jeton ou du mot est multipliée :
                              - vaut 1 si la case n'est pas spéciale;
                              - vaut 2 dans le cas d'une case compte double;
                              - vaut 3 dans le cas d'une case compte triple.
        type_bonus (str, optional): Le type de bonus de la case :
                               - vaut 'M' si la case est spéciale et affecte le pointage des mots;
                               - vaut 'L' si la case est spéciale et affecte le pointage des lettres;
                               - vaut None si la case n'est pas spéciale.
        jeton_occupant (Jeton, optional): Le jeton actuellement placé sur cette case, ou None si la case est vide.
    """

    def __init__(self, multiplicateur=1, type_bonus=None):
        """Initialise une case avec un multiplicateur et un type spécifiés.

        Args:
            multiplicateur (int, optional): Le multiplicateur de score appliqué à la case. Doit être entre 1 et 3 inclusivement.
            type_bonus (str, optional): Le type de bonus de la case ('L' pour lettre, 'M' pour mot),
                                        ou None si la case est standard.

        Raises:
            AssertionError: Si le multiplicateur ou le type est hors des valeurs permises.
        """
        self.multiplicateur = multiplicateur
        self.type_bonus = type_bonus
        # TODO

    def est_vide(self):
        """Vérifie si la case est actuellement vide.

        Returns:
            bool: True si aucun jeton n'occupe la case, False sinon.
        """
        return self.jeton_occupant is None

    def placer_jeton(self, jeton):
        """Place un jeton sur la case, s'il n'y en a pas déjà un.

        Args:
            jeton (Jeton): Le jeton à placer sur la case.

        Raises:
            AssertionError: Si la case est déjà occupée.
        """
        assert self.est_vide(), "Case non vide."
        self.jeton_occupant = jeton

    def retirer_jeton(self):
        """Retire et renvoie le jeton actuellement placé sur la case.

        Returns:
            Jeton: Le jeton retiré de la case.

        Raises:
            AssertionError: Si la case est vide.
        """
        jeton = self.jeton_occupant
        self.jeton_occupant = None
        return jeton
        # TODO

    def valeur_jeton(self):
        """Renvoie la valeur du jeton placé sur cette case.

        Returns:
            int: La valeur du jeton.

        Raises:
            AssertionError: Si aucun jeton n'occupe la case.
        """
        assert not self.est_vide(), "Aucun jeton dans la case."
        return self.jeton_occupant.valeur

    def lettre_jeton(self):
        """Renvoie la lettre du jeton placé sur cette case.

        Returns:
            str: La lettre du jeton.

        Raises:
            AssertionError: Si aucun jeton n'occupe la case.
        """
        assert not self.est_vide(), "Aucun jeton dans la case."
        return self.jeton_occupant.lettre

    def code_couleur(self):
        """Renvoie le code couleur ANSI et hexadécimal de la case, basé sur son type de bonus et multiplicateur.

        Returns:
            tuple: Le code couleur ANSI et la valeur hexadécimale correspondant au type de bonus et multiplicateur de la case.
        """
        if self.type_bonus == "M" and self.multiplicateur == 2:
            return 45, "#ffaccb"
        elif self.type_bonus == "M" and self.multiplicateur == 3:
            return 41, "#ff0000"
        elif self.type_bonus == "L" and self.multiplicateur == 2:
            return 46, "#00c9ff"
        elif self.type_bonus == "L" and self.multiplicateur == 3:
            return 44, "#0051ff"
        else:
            return 0, "#f5ebdc"

    def code_couleur_ansi(self):
        """Renvoie le code couleur ANSI de la case.

        Returns:
            int: Le code couleur ANSI de la case.
        """
        return self.code_couleur()[0]

    def code_couleur_hex(self):
        """Renvoie le code couleur hexadécimal de la case.

        Returns:
            str: La valeur hexadécimale du code couleur de la case.
        """
        return self.code_couleur()[1]

    def texte_descriptif(self):
        """Renvoie le texte descriptif de la case, basé sur son type de bonus et multiplicateur.

        Returns:
            str: La description textuelle du type et multiplicateur de la case, ou une chaîne vide si standard.
        """
        if self.type_bonus == "M" and self.multiplicateur == 2:
            return "Mot\nDouble"
        elif self.type_bonus == "M" and self.multiplicateur == 3:
            return "Mot\nTriple"
        elif self.type_bonus == "L" and self.multiplicateur == 2:
            return "Lettre\nDouble"
        elif self.type_bonus == "L" and self.multiplicateur == 3:
            return "Lettre\nTriple"
        else:
            return ""

    def __repr__(self):
        """Méthode spéciale indiquant à Python comment représenter une instance de Case par une chaîne de
        caractères. Notamment utilisé pour imprimer une case à l'écran.

        Returns:
            str: La représentation textuelle de la case, incluant son contenu (si jeton occupant il y a) et sa couleur.
        """
        s = "" if self.est_vide() else str(self.jeton_occupant)
        return "\x1b[0;30;{}m{:^4s}\x1b[0m".format(self.code_couleur_ansi(), s)
