#pgzero

"""
Version actual: [M7.L1: Actividad 1/9]
packs de assets: https://kenney.nl/assets/series:Tiny?sort=update
"""

# Ventana de juego hecha de celdas
celda = Actor('border')
size_w = 5 # Ancho del mapa en celdas
size_h = 5 # Altura del mapa en celdas

WIDTH =  celda.width  * size_w
HEIGHT = celda.height * size_h

TITLE = "Mazmorras" # Título de la ventana de juego
FPS = 30 # Número de fotogramas por segundo