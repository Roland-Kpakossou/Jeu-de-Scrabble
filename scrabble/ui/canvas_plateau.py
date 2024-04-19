from tkinter import Canvas, CENTER

from scrabble.common.position import Position
from scrabble.utilitaires import coordonnees_case, dessiner_jeton


class CanvasPlateau(Canvas):
    """
    Représente graphiquement un plateau de Scrabble à l'aide d'un objet Canvas de tkinter.
    Ce canvas gère le dessin des cases du plateau, des jetons, et s'adapte aux changements de taille de fenêtre.

    Attributes:
        plateau (Plateau): Référence au plateau de jeu de Scrabble contenant la configuration des cases et des jetons.
        n_pixels_par_case (int): Le nombre de pixels utilisé pour représenter une case sur le plateau.
    """

    def __init__(self, parent, plateau, n_pixels_par_case=50):
        """
        Initialise le Canvas pour le plateau de Scrabble avec une taille basée sur le nombre de lignes et de colonnes
        du plateau et la taille des cases spécifiée.

        Args:
            parent (tkinter.Widget): Le widget parent de ce canvas, généralement une instance de tkinter.Tk ou tkinter.Frame.
            plateau (Plateau): Le plateau de jeu à afficher.
            n_pixels_par_case (int): La dimension initiale de chaque case en pixels.
        """
        # Appel du constructeur de la classe de base (Canvas).
        largeur = plateau.n_lignes * n_pixels_par_case
        hauteur = plateau.n_colonnes * n_pixels_par_case
        super().__init__(parent, width=largeur, height=hauteur)

        self.plateau = plateau

        # Nombre de pixels par case, variable.
        self.n_pixels_par_case = n_pixels_par_case

        # On fait en sorte que le redimensionnement du canvas redimensionne son contenu.
        # Cet événement étant également généré lors de la création de la fenêtre,
        # nous n'avons pas à dessiner les cases et les jetons dans le constructeur.
        self.bind("<Configure>", self.redimensionner)

    def redimensionner(self, event):
        """
        Gère l'événement de redimensionnement du canvas. Ajuste la taille des cases en fonction de la nouvelle taille
        du canvas tout en conservant l'aspect carré du plateau.

        Args:
            event (tkinter.Event): L'événement contenant les nouvelles dimensions du canvas.
        """
        # Nous recevons dans le "event" la nouvelle dimension dans les attributs width et height.
        # Nous voulons un plateau carré, alors on ne conserve que la plus petite de ces deux valeurs.
        nouvelle_taille = min(event.width, event.height)

        # Adaptation de la taille des cases en fonction de la nouvelle taille du canvas
        self.n_pixels_par_case = nouvelle_taille // self.plateau.n_lignes

        self.actualiser()

    def actualiser(self):
        """
        Redessine les cases et les jetons à chaque appel, permettant de mettre à jour l'affichage après un redimensionnement
        ou une modification du plateau.
        """
        self.delete("case")
        self.delete("jeton")
        self.dessiner()

    def dessiner(self):
        """
        Dessine l'ensemble du plateau de Scrabble sur le canvas, incluant les cases et les jetons si présents.
        """
        for i in range(self.plateau.n_lignes):
            for j in range(self.plateau.n_colonnes):
                position = Position(i, j)
                self.dessiner_case(position)

                if not self.plateau.case_est_vide(position):
                    dessiner_jeton(
                        self,
                        self.plateau.cases[position].jeton_occupant,
                        position,
                        self.n_pixels_par_case,
                    )

        for position, jeton in zip(
            self.plateau.positions_en_jeu, self.plateau.jetons_en_jeu
        ):
            dessiner_jeton(
                self, jeton, position, self.n_pixels_par_case, surligner=True
            )

    def dessiner_case(self, position):
        """
        Dessine une case individuelle du plateau, en y plaçant le texte approprié (lettres ou symboles spéciaux) et
        en ajustant la couleur de fond selon les spécifications du plateau.

        Args:
            position (Position): La position de la case à dessiner.
        """
        # Dessin d'une case individuelle avec gestion de la couleur et du texte
        debut_ligne, debut_colonne, fin_ligne, fin_colonne = coordonnees_case(
            position, self.n_pixels_par_case
        )
        self.create_rectangle(
            debut_colonne,
            debut_ligne,
            fin_colonne,
            fin_ligne,
            fill=self.plateau.cases[position].code_couleur_hex(),
            tags="case",
        )
        texte_case = (
            "\u2605"
            if position.ligne == position.colonne == 7
            else self.plateau.cases[position].texte_descriptif()
        )
        moitie_n_pixels_par_case = self.n_pixels_par_case // 2
        police_de_caracteres = (
            "Deja Vu",
            moitie_n_pixels_par_case // 2,
        )
        coordonnee_x = debut_colonne + moitie_n_pixels_par_case
        coordonnee_y = debut_ligne + moitie_n_pixels_par_case
        self.create_text(
            coordonnee_x,
            coordonnee_y,
            justify=CENTER,
            font=police_de_caracteres,
            text=texte_case,
            tags="case",
        )

