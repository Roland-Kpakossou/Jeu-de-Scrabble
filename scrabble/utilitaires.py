def coordonnees_case(position, n_pixels_par_case):
    """
    Calcule les coordonnées d'une case sur un canvas en fonction de sa position dans la grille du plateau
    et de la taille de case spécifiée.

    Args:
        position (Position): La position de la case.
        n_pixels_par_case (int): La taille de chaque case en pixels.

    Returns:
        tuple[int, int, int, int]: Un tuple contenant les coordonnées du début de ligne, du début de colonne,
                                    de la fin de ligne et de la fin de colonne.
    """
    debut_ligne = position.ligne * n_pixels_par_case
    fin_ligne = debut_ligne + n_pixels_par_case
    debut_colonne = position.colonne * n_pixels_par_case
    fin_colonne = debut_colonne + n_pixels_par_case
    return debut_ligne, debut_colonne, fin_ligne, fin_colonne


def dessiner_jeton(
    canvas, jeton, position, n_pixels_par_case, surligner=False, tag="jeton"
):
    """
    Dessine un jeton sur un canvas à la position spécifiée avec la possibilité de surlignage.

    Cette fonction place un rectangle et le caractère du jeton sur le canvas à l'endroit approprié selon la grille du jeu,
    en utilisant les coordonnées déterminées par la position et la taille des cases.

    Args:
        canvas (Canvas): Le canvas de tkinter où le jeton sera dessiné.
        jeton (Jeton): L'objet jeton à dessiner, qui doit avoir une représentation sous forme de chaîne.
        position (Position): La position du jeton sur le plateau.
        n_pixels_par_case (int): La taille de chaque case en pixels.
        surligner (bool): Si True, le jeton est dessiné avec une couleur de fond spéciale pour le mettre en évidence.
        tag (str): Le tag tkinter utilisé pour regrouper les éléments graphiques jeton sur le canvas ("jeton" par défaut).
    """
    debut_ligne, debut_colonne, fin_ligne, fin_colonne = coordonnees_case(
        position, n_pixels_par_case
    )
    centre = (
        debut_colonne + n_pixels_par_case // 2,
        debut_ligne + n_pixels_par_case // 2,
    )

    canvas.create_rectangle(
        debut_colonne,
        debut_ligne,
        fin_colonne,
        fin_ligne,
        fill="orange" if surligner else "#b9936c",
        tags=tag,
    )
    canvas.create_text(
        centre,
        font=("Deja Vu", n_pixels_par_case // 2),
        text=str(jeton),
        tags=tag,
    )
