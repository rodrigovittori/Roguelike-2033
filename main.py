#pgzero

"""
Version actual: [M7.L1: Actividad #3]

Objetivo: Crear actores para nuestra paleta de terreno
          Crear función que dibuje en pantalla el mapa, (segun los valores en la lista)
          -> Extra: Agregar distintos modelos de mapa

Kodland: https://kenney.nl/assets/roguelike-caves-dungeons
packs de assets: https://kenney.nl/assets/series:Tiny?sort=update
"""

# Ventana de juego hecha de celdas
celda = Actor('border') # Celda que voy a utilizar como referencia para mi mapa

# Paleta de terrenos:
pared =  Actor("border") # 0: Pared de bloques
piso =   Actor("floor")  # 1: Suelo liso (sin decoración)
crack =  Actor("crack")  # 2: Suelo resquebrajado/quebradizo
huesos = Actor("bones")  # 3: Suelo con una pilita de huesos

size_w = 7 # Ancho del mapa en celdas
size_h = 7 # Altura del mapa en celdas

WIDTH =  celda.width  * size_w # Ancho de la ventana (en píxeles)
HEIGHT = celda.height * size_h #  Alto de la ventana (en píxeles)

TITLE = "Rogue-like: Mazmorras" # Título de la ventana de juego
FPS = 30 # Número de fotogramas por segundo

################## MAPAS ##################

mapa = [ [0, 0, 0, 0, 0, 0, 0],
         [0, 1, 2, 1, 3, 1, 0],
         [0, 1, 1, 2, 1, 1, 0],
         [0, 3, 2, 1, 1, 3, 0],
         [0, 1, 1, 1, 3, 1, 0],
         [0, 1, 3, 1, 1, 2, 0],
         [0, 0, 0, 0, 0, 0, 0] ]

mapa2 = [[0, 0, 0, 0, 0, 0, 0],
         [0, 1, 1, 3, 1, 1, 0],
         [0, 1, 3, 1, 3, 1, 0],
         [0, 3, 1, 1, 1, 3, 0],
         [0, 3, 1, 1, 1, 3, 0],
         [0, 1, 3, 3, 3, 1, 0],
         [0, 0, 0, 0, 0, 0, 0]]

###########################################

mapa_actual = mapa # mapa a dibujar // cambiar valor si cambiamos de habitación

def dibujar_mapa(mapa):

  for fila in range(len(mapa)):
    for columna in range(len(mapa[fila])):

      """
      0: pared
      1: piso (sin nada)
      2: piso (roto/resquebrajado)
      3: piso (c/ huesitos)
      """

      if (mapa[fila][columna] == 0): # pared
        pared.left = pared.width * columna
        pared.top = pared.height * fila
        pared.draw()

      elif (mapa[fila][columna] == 1): # piso (sin nada)
        piso.left = piso.width * columna
        piso.top = piso.height * fila
        piso.draw()

      elif (mapa[fila][columna] == 2): # piso (roto/resquebrajado)
        crack.left = crack.width * columna
        crack.top = crack.height * fila
        crack.draw()

      elif (mapa[fila][columna] == 3): # piso (c/ huesitos)
        huesos.left = huesos.width * columna
        huesos.top = huesos.height * fila
        huesos.draw()

def draw():
  dibujar_mapa(mapa_actual)
      