#pgzero

"""
Version actual: [M7.L1: Actividad #1]

Kodland: https://kenney.nl/assets/roguelike-caves-dungeons
packs de assets: https://kenney.nl/assets/series:Tiny?sort=update
"""

# Ventana de juego hecha de celdas
celda = Actor('border') # Celda que voy a utilizar como referencia para mi mapa

size_w = 5 # Ancho del mapa en celdas
size_h = 5 # Altura del mapa en celdas

WIDTH =  celda.width  * size_w # Ancho de la ventana (en píxeles)
HEIGHT = celda.height * size_h #  Alto de la ventana (en píxeles)

TITLE = "Rogue-like: Mazmorras" # Título de la ventana de juego
FPS = 30 # Número de fotogramas por segundo