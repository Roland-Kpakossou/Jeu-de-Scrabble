import string


class Jeton:
    """Représente un jeton de Scrabble, incluant une lettre et sa valeur en points.

    Attributes:
        lettre (str): La lettre inscrite sur le jeton. Doit être une lettre majuscule de l'alphabet français.
        valeur (int): La valeur en points de la lettre.

    Note:
        Dans ce travail, nous ne considérons pas les jetons jokers qui n'ont aucune lettre inscrite.
    """

    def __init__(self, lettre, valeur):
        """Initialise un jeton avec une lettre et une valeur spécifiées.

        Args:
            lettre (str): La lettre pour le jeton. Doit être une majuscule de A à Z.
            valeur (int): La valeur en points du jeton. Doit être un entier entre 0 et 20, inclus.

        Raises:
            AssertionError: Si la lettre n'est pas une lettre majuscule ou si la valeur n'est pas dans l'intervalle autorisé.
        """
        #### TODO
        self.lettre = lettre
        self.valeur = valeur


    def __repr__(self):
        """Méthode spéciale indiquant à Python comment représenter une instance de Jeton par une chaîne de
        caractères. Notamment utilisé pour imprimer un jeton à l'écran.

        Returns:
            str: La représentation textuelle du jeton, incluant sa lettre et sa valeur en notation subscript.
        """
        if self.valeur < 10:
            return "{}{}".format(self.lettre, chr(0x2080 + self.valeur))
        else:
            return "{}{}{}".format(
                self.lettre,
                chr(0x2080 + int(self.valeur / 10)),
                chr(0x2080 + int(self.valeur % 10)),
            )
