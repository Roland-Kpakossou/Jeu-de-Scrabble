class Position:
    """Une position à deux coordonnées: ligne et colonne. La convention utilisée est celle de la notation matricielle :
    le coin supérieur gauche d'une matrice est dénoté (0, 0) (ligne 0 et colonne 0). On additionne une unité de colonne
    lorsqu'on se déplace vers la droite, et une unité de ligne lorsqu'on se déplace vers le bas.

    +-------+-------+-------+-------+
    | (0,0) | (0,1) | (0,2) |  ...  |
    | (1,0) | (1,1) | (1,2) |  ...  |
    | (2,0) | (2,1) | (2,2) |  ...  |
    |  ...  |  ...  |  ...  |  ...  |
    +-------+-------+-------+-------+

    Attributes:
        ligne (int): La ligne associée à la position.
        colonne (int): La colonne associée à la position.
    """

    def __init__(self, ligne, colonne):
        """Constructeur de la classe Position. Initialise une nouvelle position avec des coordonnées spécifiées.

        Args:
            ligne (int): Le numéro de la ligne de la position, où 0 représente la première ligne.
            colonne (int): Le numéro de la colonne de la position, où 0 représente la première colonne.
        """
        self.ligne = int(ligne)
        self.colonne = int(colonne)

    def obtenir_quatre_positions_adjacentes(self):
        """Retourne une liste contenant les quatre positions adjacentes à cette position.

        Returns:
            list[Position]: Une liste contenant les positions adjacentes.
        """
        return [
            Position(self.ligne, self.colonne + 1),  # Droite
            Position(self.ligne, self.colonne - 1),  # Gauche
            Position(self.ligne + 1, self.colonne),  # Bas
            Position(self.ligne - 1, self.colonne)  # Haut
         ]
        # TODO

    def __eq__(self, autre_position):
        """Méthode spéciale indiquant à Python comment vérifier si deux positions sont égales. On compare simplement
        la ligne et la colonne de l'objet actuel et de l'autre objet.

        Args:
            autre_position (Position): L'autre position à comparer.

        Returns:
            bool: True si les deux positions ont les mêmes coordonnées de ligne et de colonne, False sinon.
        """
        return (
            self.ligne == autre_position.ligne
            and self.colonne == autre_position.colonne
        )

    def __hash__(self):
        """Méthode spéciale indiquant à Python comment "hasher" une Position.

        Note: Cette méthode est nécessaire si nous voulons utiliser un objet d'une classe que nous avons définie
        nous mêmes comme clé d'un dictionnaire.
        Les étudiants(es) curieux(ses) peuvent consulter wikipédia pour en savoir plus:
            https://fr.wikipedia.org/wiki/Fonction_de_hachage

        Returns:
            int: Le hash de la représentation sous forme de chaîne de la position.
        """
        return hash(str(self))

    def __repr__(self):
        """Méthode spéciale indiquant à Python comment représenter une instance de Position par une chaîne de
        caractères. Utile pour le débogage.

        Returns:
            str: La représentation textuelle de la position sous la forme '(ligne, colonne)'.
        """
        return "({}, {})".format(self.ligne, self.colonne)
