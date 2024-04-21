from scrabble.joueur.chevalet import Chevalet

class Joueur:
    """Représente un joueur dans une partie de Scrabble, gérant son nom, son score et son chevalet de jetons.

    Attributes:
        nom (str): Le nom du joueur.
        score (int): Le score actuel du joueur dans la partie.
        chevalet (Chevalet): Le chevalet contenant les jetons actuellement en possession du joueur.
    """

    def __init__(self, nom):
        """Initialise un nouveau joueur avec un nom donné, un score de 0 et un chevalet vide de jetons de taille 7.

        Args:
            nom (str): Le nom du joueur. Doit être une chaîne non vide et non constituée uniquement d'espaces.

        Raises:
            AssertionError: Si le nom est vide ou ne contient que des espaces.
        """
        # TODO
        # On valide les pré-conditions
        if not nom or nom.isspace():
            raise AssertionError("Le nom doit être non vide et ne pas contenir que des espaces.")
        self.nom = nom
        self.score = 0
        self.chevalet = Chevalet()  # Initialisation du chevalet

    def nombre_de_nouveaux_jetons_a_tirer(self):
        """Calcule le nombre de nouveaux jetons qu'un joueur doit tirer pour remplir son chevalet.

        Returns:
            int: Le nombre d'emplacements vides dans le chevalet du joueur.
        """
        # TODO
        return self.chevalet.nombre_emplacements_vides()

    def peut_tirer_de_nouveaux_jetons(self):
        """Détermine si le joueur peut tirer de nouveaux jetons pour son chevalet.

        Returns:
            bool: True si le chevalet du joueur n'est pas plein, False sinon.
        """
        # TODO
        return not self.chevalet.est_plein()

    def __repr__(self):
        """Méthode spéciale indiquant à Python comment représenter une instance de Joueur par une chaîne de
        caractères. Notamment utilisé pour imprimer un joueur à l'écran.

        Returns:
            str: La représentation textuelle du joueur, comprenant son nom, son score et l'état actuel de son chevalet.
        """
        return f"{self.nom}\nScore: {self.score}\n{self.chevalet}"
