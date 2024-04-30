import random


class Chevalet:
    """Gère un ensemble d'emplacements pour des jetons.

    Attributes:
        emplacements (list): Liste des emplacements sur le chevalet, pouvant être occupés par des jetons ou vides (None).
    """
    class EmplacementInvalidException(Exception):
        """Exception levée si l'emplacement spécifié est invalide."""
        pass

    class EmplacementOccupeException(Exception):
        """Exception levée si l'emplacement spécifié est déjà occupé."""
        pass

    class EmplacementVideException(Exception):
        """Exception levée si l'emplacement spécifié est vide."""
        pass


    def __init__(self, taille=7):
        """Initialise le chevalet avec une taille donnée.

        Args:
            taille (int, optional): Le nombre d'emplacements sur le chevalet. La valeur par défaut est de 7.
        """
        self.emplacements = [None] * taille

    def taille(self):
        """Renvoie la taille du chevalet, c'est-à-dire le nombre d'emplacements.

        Returns:
            int: Le nombre d'emplacements sur le chevalet.
        """
        return len(self.emplacements)

    def nombre_emplacements_vides(self):
        """Compte le nombre d'emplacements vides sur le chevalet.

        Returns:
            int: Le nombre d'emplacements vides.
        """
        # TODO
        return self.emplacements.count(None)

    def est_plein(self):
        """Vérifie si le chevalet est plein, c'est-à-dire s'il n'y a plus d'emplacements vides pour des jetons supplémentaires.

        Returns:
            bool: True si le chevalet est plein, False sinon.
        """
        # TODO
        return self.nombre_emplacements_vides() == 0

    def emplacement_est_valide(self, index_emplacement):
        """Vérifie si un emplacement donné est valide (dans les limites de la taille du chevalet).

        Args:
            index_emplacement (int): L'index de l'emplacement à vérifier.

        Returns:
            bool: True si l'emplacement est valide, False sinon.
        """
        # TODO
        return index_emplacement is not None and 0 <= index_emplacement < self.taille()

    def emplacement_est_vide(self, index_emplacement):
        """Vérifie si un emplacement donné est vide.

        Args:
            index_emplacement (int): L'index de l'emplacement à vérifier.

        Returns:
            bool: True si l'emplacement est vide, False sinon.
        """
        return self.emplacements[index_emplacement] is None

    def ajouter_jeton(self, jeton, index_emplacement=None):
        """Ajoute un jeton à un emplacement spécifique ou au premier emplacement vide si aucun index n'est fourni.

        Args:
            jeton (Jeton): L'objet jeton à ajouter sur le chevalet.
            index_emplacement (int, optional): L'index de l'emplacement où ajouter le jeton.
                                               Si None, le jeton est ajouté au premier emplacement vide.

        Raises:
            AssertionError: Si l'emplacement spécifié est invalide ou déjà occupé.
        """
        # TODO
        if index_emplacement is None:
            index_emplacement = self.emplacements.index(None) if None in self.emplacements else -1
            if index_emplacement == -1:
                raise self.EmplacementOccupeException("Aucun emplacement vide disponible.")
        else:
            if not self.emplacement_est_valide(index_emplacement):
                raise self.EmplacementInvalidException("L'emplacement spécifié est invalide.")
            if not self.emplacement_est_vide(index_emplacement):
                raise self.EmplacementOccupeException("L'emplacement spécifié est déjà occupé.")
        self.emplacements[index_emplacement] = jeton

    def obtenir_jeton(self, index_emplacement):
        """Obtient le jeton d'un emplacement spécifique.

        Args:
            index_emplacement (int): L'index de l'emplacement à consulter.

        Returns:
            Jeton: L'objet jeton à l'emplacement spécifié.

        Raises:
            AssertionError: Si l'emplacement spécifié est invalide ou vide.
        """
        # TODO
        if not self.emplacement_est_valide(index_emplacement):
            raise self.EmplacementInvalidException("L'emplacement spécifié est invalide.")
        if self.emplacement_est_vide(index_emplacement):
            raise self.EmplacementVideException("L'emplacement spécifié est vide.")
        return self.emplacements[index_emplacement]

    def retirer_jeton(self, index_emplacement):
        """Retire et renvoie le jeton d'un emplacement spécifique.

        Args:
            index_emplacement (int): L'index de l'emplacement duquel retirer le jeton.

        Returns:
            Jeton: L'objet jeton retiré de l'emplacement spécifié.

        Raises:
            AssertionError: Si l'emplacement spécifié est invalide ou vide.
        """
        # TODO
        if not self.emplacement_est_valide(index_emplacement):
            raise self.EmplacementInvalidException("L'emplacement spécifié est invalide.")
        if self.emplacement_est_vide(index_emplacement):
            raise self.EmplacementVideException("L'emplacement spécifié est vide.")
        jeton = self.emplacements[index_emplacement]
        self.emplacements[index_emplacement] = None
        return jeton
    def melanger_jetons(self):
        """Mélange les jetons présents sur le chevalet, changeant leur ordre de manière aléatoire."""
        random.shuffle(self.emplacements)

    def __repr__(self):
        """Méthode spéciale indiquant à Python comment représenter une instance de Chevalet par une chaîne de
        caractères. Notamment utilisé pour imprimer un chevalet à l'écran.

        Returns:
            str: Une représentation textuelle du chevalet et de son contenu.
        """
        s = "            " + "".join(
            ["{:<3s}".format(str(x)) if x else "  " for x in self.emplacements]
        )
        s += (
            "\nChevalet: \\_"
            + "__".join([chr(0x2080 + i + 1) for i in range(self.taille())])
            + "_/\n"
        )
        return s