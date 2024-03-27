from PIL import Image
import os

# Chemin vers le dossier contenant les pièces individuelles
DOSSIER_PIECES = "chemin_vers_le_dossier_pieces"
# Chemin vers l'image du plateau d'échecs
IMAGE_PLATEAU = "chemin_vers_l_image_plateau"

def charger_pieces(chemin_dossier):
    pieces = {}
    for fichier in os.listdir(chemin_dossier):
        if fichier.endswith(".png") or fichier.endswith(".jpg"):
            chemin_piece = os.path.join(chemin_dossier, fichier)
            nom_piece = os.path.splitext(fichier)[0]  # Nom de la pièce sans extension
            pieces[nom_piece] = Image.open(chemin_piece)
    return pieces

def trouver_pieces_sur_plateau(image_plateau, pieces):
    largeur_plateau, hauteur_plateau = image_plateau.size
    for nom_piece, piece in pieces.items():
        largeur_piece, hauteur_piece = piece.size
        for y in range(hauteur_plateau - hauteur_piece + 1):
            for x in range(largeur_plateau - largeur_piece + 1):
                zone = image_plateau.crop((x, y, x + largeur_piece, y + hauteur_piece))
                if comparer_images(zone, piece):
                    print(f"{nom_piece} trouvé à la position ({x}, {y})")

def comparer_images(image1, image2):
    diff = ImageChops.difference(image1, image2)
    diff = diff.getbbox()
    return diff is None

# Charger les pièces individuelles
pieces = charger_pieces(DOSSIER_PIECES)

# Charger l'image du plateau d'échecs
image_plateau = Image.open(IMAGE_PLATEAU)

# Trouver les pièces sur le plateau
trouver_pieces_sur_plateau(image_plateau, pieces)
