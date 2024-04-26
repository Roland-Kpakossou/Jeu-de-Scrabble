from tkinter import Button, Frame, Label, NSEW, Tk, messagebox

from scrabble.partie import Partie
from scrabble.ui.canvas_plateau import CanvasPlateau
from scrabble.ui.canvas_chevalet import CanvasChevalet
from scrabble.common.position import Position
from scrabble.utilitaires import dessiner_jeton


class FenetrePartie(Tk):
    """
    Crée une fenêtre de jeu pour une partie de Scrabble, intégrant un plateau de jeu, un chevalet pour chaque joueur,
    et divers contrôles pour gérer le déroulement de la partie.

    Cette interface graphique permet aux joueurs de voir leur chevalet, le plateau, de mélanger les jetons,
    passer leur tour ou jouer un coup. Les interactions sont principalement gérées par des clics sur les jetons
    et les cases du plateau.

    Attributes:
        partie (Partie): L'instance de la p artie de Scrabble en cours.
        canvas_plateau (CanvasPlateau): Le canvas tkinter qui affiche le plateau de jeu.
        canvas_chevalet (CanvasChevalet): Le canvas tkinter qui affiche le chevalet du joueur actif.
        label_joueur_actif (Label): Affiche le nom du joueur actif.
        label_scores_joueurs (Label): Affiche les scores de tous les joueurs.
    """

    def __init__(self, nombre_de_joueurs=2, langue="fr"):
        """
        Initialise la fenêtre de jeu, incluant le plateau, le chevalet, et les contrôles de jeu.

        Args:
            nombre_de_joueurs (int): Le nombre de joueurs dans la partie, entre 2 et 4.
            langue (str): La langue du jeu, 'fr' pour français et 'en' pour anglais.
        """
        # Appel du constructeur de la classe parente «Tk»
        super().__init__()

        # Titre de la fenêtre («title» est une méthode de la classe parente «Tk»)
        self.title("Jeu de Scrabble")

        # La partie
        self.partie = Partie(nombre_de_joueurs, langue)

        self.emplacement_jeton_selectionne_chevalet = None

        # Création du canvas plateau.
        self.canvas_plateau = CanvasPlateau(self, self.partie.plateau, 50)
        self.canvas_plateau.grid(row=0, column=0, sticky=NSEW)

        # Création du canvas chevalet.
        self.canvas_chevalet = CanvasChevalet(
            self, self.partie.joueur_actif.chevalet, 50
        )
        self.canvas_chevalet.grid(row=1, column=0)

        # Création du cadre de droite
        police_de_caracteres = ("Deja Vu", "20")
        cadre_de_droite = Frame(self)
        cadre_de_droite.grid(row=0, column=1)

        self.label_joueur_actif = Label(
            cadre_de_droite,
            text="",
            fg="#ec4899",
            font=police_de_caracteres,
        )
        self.label_joueur_actif.grid(padx=10, pady=5, sticky=NSEW)

        self.label_scores_joueurs = Label(
            cadre_de_droite,
            text="",
            fg="#6366f1",
            font=police_de_caracteres,
        )
        self.label_scores_joueurs.grid(padx=10, pady=5, sticky=NSEW)

        bouton_melanger_jetons_chevaler = Button(
            cadre_de_droite,
            text="Mélanger le chevalet",
            font=police_de_caracteres,
            padx=10,
            pady=10,
            command=self.gerer_clic_bouton_melanger_jetons_chevalet,
        )
        bouton_melanger_jetons_chevaler.grid(padx=10, pady=5, sticky=NSEW)

        bouton_passer_tour = Button(
            cadre_de_droite,
            text="Passer mon tour",
            font=police_de_caracteres,
            padx=10,
            pady=10,
            command=self.gerer_clic_bouton_passer_tour,
        )
        bouton_passer_tour.grid(padx=10, pady=5, sticky=NSEW)

        bouton_jouer = Button(
            cadre_de_droite,
            text="Jouer",
            font=police_de_caracteres,
            padx=10,
            pady=10,
            command=self.gerer_clic_bouton_jouer_un_tour,
        )
        bouton_jouer.grid(padx=10, pady=5, sticky=NSEW)

        # Associe les évènements aux méthodes de rappel correspondantes
        self.canvas_plateau.tag_bind("case", "<Button-1>", self.gerer_clic_case_plateau)
        self.canvas_chevalet.tag_bind(
            "jeton", "<Button-1>", self.gerer_clic_jeton_chevalet
        )
        self.bind("<Escape>", self.annuler_tous_les_deplacements_en_attente)

        # Configuration pour le redimensionnement automatique des éléments de la fenêtre.
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # TODO
        self.actualiser_statut_jeu()
        self.actualiser_chevalet()

    def actualiser_statut_jeu(self):
        """
        Met à jour les affichages du joueur actif et des scores des joueurs dans les labels correspondants.
        """
        # TODO
        self.label_joueur_actif["text"] = "Joueur Actif: " + self.partie.joueur_actif.nom
        scores_text = ""
        for joueur in self.partie.joueurs:
            scores_text += joueur.nom + ": " + str(joueur.score) + "\n"
        self.label_scores_joueurs["text"] = scores_text

    def gerer_clic_bouton_melanger_jetons_chevalet(self):
        """
        Gère le clic sur le bouton pour mélanger les jetons du chevalet du joueur actif.
        Annule les déplacements en attente et mélange les jetons du chevalet.
        """
        """
        Modifie aléatoirement l'ordre des jetons sur le chevalet du joueur actif.
        """
        self.annuler_tous_les_deplacements_en_attente()
        self.partie.joueur_actif.chevalet.melanger_jetons()
        self.actualiser_chevalet()

    def gerer_clic_bouton_passer_tour(self):
        """
        Gère le clic sur le bouton pour passer le tour du joueur actif.
        Annule les déplacements en attente et passe au joueur suivant.
        """
        # TODO
        self.annuler_tous_les_deplacements_en_attente()
        self.actualiser_statut_jeu()
        self.passer_au_joueur_suivant()
        self.actualiser_chevalet()

    def gerer_clic_bouton_jouer_un_tour(self):
        """
        Tente de jouer un tour avec les déplacements effectués par le joueur actif.
        Affiche un message approprié en fonction du succès ou de l'échec du tour.

        Note: Vous devez compéter cette méthode afin de passer au joueur suivant!
        """
        success, message = self.partie.jouer_un_tour()

        if success:
            messagebox.showinfo("Bravo!", message, parent=self)
            self.confirmer_tous_les_deplacements_effectues()
            # TODO
            self.actualiser_statut_jeu()
            self.passer_au_joueur_suivant()
        else:
            messagebox.showerror("Oups!", message, parent=self)
            self.annuler_tous_les_deplacements_en_attente()

    def confirmer_tous_les_deplacements_effectues(self):
        """
        Confirme et applique tous les déplacements de jetons effectués pendant le tour en cours.
        """
        self.partie.appliquer_deplacements_en_attente()
        self.emplacement_jeton_selectionne_chevalet = None
        self.canvas_plateau.actualiser()

    def annuler_tous_les_deplacements_en_attente(self, event=None):
        """
        Annule tous les déplacements de jetons en attente sur le plateau et remet les jetons dans le chevalet du joueur actif.

        Args:
            event (tkinter.Event): L'évènement ayant causé l'appel de la méthode (non utilisé).
        """
        self.partie.annuler_deplacements_en_attente()
        self.emplacement_jeton_selectionne_chevalet = None
        self.canvas_plateau.actualiser()
        self.actualiser_chevalet()

    def gerer_clic_jeton_chevalet(self, event):
        """
        Gère le clic sur un jeton dans le chevalet du joueur, sélectionnant ou désélectionnant le jeton pour le déplacement.

        Args:
            event (tkinter.Event): L'évènement ayant causé l'appel de la méthode.
        """
        emplacement_jeton_selectionne = self.determiner_emplacement_jeton_chevalet(
            event
        )
        self.gerer_selection_jeton_chevalet(emplacement_jeton_selectionne)
        self.actualiser_chevalet()

    def determiner_emplacement_jeton_chevalet(self, event):
        """
        Détermine l'emplacement du jeton cliqué dans le chevalet à partir de l'événement de clic.

        Args:
            event (tkinter.Event): L'évènement du clic.

        Returns:
            int: L'index du jeton dans le chevalet basé sur la position du clic.
        """
        # TODO
        return event.x // self.canvas_chevalet.n_pixels_par_case

    def gerer_selection_jeton_chevalet(self, emplacement_jeton_selectionne):
        """
        Gère la sélection ou la désélection d'un jeton dans le chevalet. Sélectionne un nouveau jeton ou
        désélectionne le jeton actuellement sélectionné si le même jeton est cliqué à nouveau.

        Args:
            emplacement_jeton_selectionne (int): L'index du jeton cliqué.
        """
        if (
            self.emplacement_jeton_selectionne_chevalet is None
            or self.emplacement_jeton_selectionne_chevalet
            != emplacement_jeton_selectionne
        ):
            self.emplacement_jeton_selectionne_chevalet = emplacement_jeton_selectionne
        else:
            self.emplacement_jeton_selectionne_chevalet = None

    def gerer_clic_case_plateau(self, event):
        """
        Gère le clic sur une case du plateau pour tenter de placer un jeton sélectionné précédemment dans le chevalet.

        Args:
            event (tkinter.Event): L'évènement ayant causé l'appel de la méthode.
        """
        # TODO
        x, y = event.x, event.y
        ligne = y // self.canvas_plateau.n_pixels_par_case
        colonne = x // self.canvas_plateau.n_pixels_par_case
        position_plateau = Position(ligne, colonne)

        # Vérifier si une position du jeton a été sélectionnée dans le chevalet avant de tenter de placer le jeton
        if self.emplacement_jeton_selectionne_chevalet is not None:
            jeton = self.partie.joueur_actif.chevalet.obtenir_jeton(self.emplacement_jeton_selectionne_chevalet)
            if jeton and self.partie.plateau.ajouter_jeton(jeton, position_plateau):
                self.canvas_plateau.actualiser()

            else:
                messagebox.showerror("Erreur!", "Impossible de placer le jeton à cet emplacement.", parent=self)
        else:
            messagebox.showinfo("Information", "Veuillez sélectionner un jeton de votre chevalet.", parent=self)

    def passer_au_joueur_suivant(self):
        """
        Passe le contrôle au joueur suivant, met à jour l'affichage du joueur actif et du chevalet.
        """
        # TODO
        self.partie.passer_au_joueur_suivant()
        self.actualiser_statut_jeu()
        self.actualiser_chevalet()

    def actualiser_chevalet(self):
        """
        Redessine les jetons dans le chevalet du joueur actif, mettant en évidence le jeton sélectionné si nécessaire.
        """
        self.canvas_chevalet.delete("jeton")

        for j, jeton in enumerate(self.partie.joueur_actif.chevalet.emplacements):
            if jeton is not None:
                surligner = j == self.emplacement_jeton_selectionne_chevalet
                dessiner_jeton(
                    self.canvas_chevalet,
                    jeton,
                    Position(0, j),
                    self.canvas_chevalet.n_pixels_par_case,
                    surligner,
                )
