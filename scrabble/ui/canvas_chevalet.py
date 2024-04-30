from tkinter import Canvas


class CanvasChevalet(Canvas):
    """
    Représente graphiquement un chevalet à l'aide d'un objet Canvas de tkinter.
    Chaque case du chevalet peut afficher un jeton et est dessinée en fonction du nombre de pixels spécifié par case.

    Attributes:
        chevalet (Chevalet): Une référence au chevalet du joueur qui contient les jetons à afficher.
        n_pixels_par_case (int): Le nombre de pixels utilisé pour la largeur et la hauteur de chaque case.
    """

    def __init__(self, parent, chevalet, n_pixels_par_case=50):
        """
        Initialise un nouveau canvas pour représenter un chevalet de Scrabble, avec les dimensions appropriées
        pour afficher tous les jetons contenus dans le chevalet.

        Le fond du canvas est configuré à une couleur spécifique qui simule l'aspect d'un chevalet en bois.

        Args:
            parent (tkinter.Widget): Le widget parent de ce canvas, typiquement une instance de tkinter.Tk ou tkinter.Frame.
            chevalet (Chevalet): L'objet chevalet associé à ce canvas, contenant les jetons à afficher.
            n_pixels_par_case (int): Taille en pixels pour chaque case représentant un emplacement de jeton sur le chevalet.
        """
        self.chevalet = chevalet
        self.n_pixels_par_case = n_pixels_par_case

        # Calcul de la largeur et de la hauteur totales du canvas basé sur le nombre de jetons dans le chevalet.
        largeur = self.chevalet.taille() * n_pixels_par_case
        hauteur = n_pixels_par_case

        # Initialisation du canvas avec la taille calculée et une couleur de fond choisie pour ressembler à du bois.
        super().__init__(parent, width=largeur, height=hauteur, bg="#645b4b")

