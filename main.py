#pgzero
import random

"""
Version actual: [M7.L2: Actividad Extra #1 "¿Ganas o pierdes?"]
Objetivo: Crear una función que verifique si la partida debe terminar

Kodland: https://kenney.nl/assets/roguelike-caves-dungeons
packs de assets: https://kenney.nl/assets/series:Tiny?sort=update

>> TAREAS:

RESOLVER LOS TO-DO
UNIFICAR LAS COLISIONES
AGREGAR GAME-OVER
AGREGAR TIPOS DE ENEMIGOS
AGREGAR QUE LA SALUD Y EL ATK DE LOS ENEMIGOS AUMENTE ENTRE CADA SPAWN (P/EVITAR PWR CREEP)
"""

# Ventana de juego hecha de celdas
celda = Actor('border') # Celda que voy a utilizar como referencia para mi mapa

# Paleta de terrenos:
pared =  Actor("border") # 0: Pared de bloques
piso =   Actor("floor")  # 1: Suelo liso (sin decoración)
crack =  Actor("crack")  # 2: Suelo resquebrajado/quebradizo
huesos = Actor("bones")  # 3: Suelo con una pilita de huesos

size_w = 9 # Ancho del mapa en celdas
size_h = 10 # Altura del mapa en celdas

WIDTH =  celda.width  * size_w # Ancho de la ventana (en píxeles)
HEIGHT = celda.height * size_h #  Alto de la ventana (en píxeles)

TITLE = "Rogue-like: Mazmorras" # Título de la ventana de juego
FPS = 30 # Número de fotogramas por segundo

# Personaje:

personaje = Actor("stand")
personaje.salud = 100
# Nota: si quieren llevar control de la vida, pueden crear dos atributos: "salud_max" y "salud_actual"
personaje.ataque = 5

# Variables:
CANT_ENEMIGOS_A_SPAWNEAR = 5
colision = -2 # ¿XQ -2 como valor inicial?: porque es un valor que NO nos puede devolver collidelist.
modo_actual = "juego"
partida_finalizada = False # To-do: agregar variable para la habitación (no la partida)
resultado_partida = "jugando" # valores: "jugando"/"victoria"/"derrota"

# Listas:
lista_enemigos = []
lista_bonus = []

################## MAPAS ##################

mapa =   [[0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 1, 1, 2, 1, 3, 1, 1, 0], 
          [0, 1, 1, 1, 2, 1, 1, 1, 0], 
          [0, 1, 3, 2, 1, 1, 3, 1, 0], 
          [0, 1, 1, 1, 1, 3, 1, 1, 0], 
          [0, 1, 1, 3, 1, 1, 2, 1, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1] ] # Fila extra para mostrar el texto

mapa2 = [ [0, 0, 0, 0, 0, 0, 0, 0, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 1, 1, 3, 1, 3, 1, 1, 0], 
          [0, 1, 1, 3, 1, 3, 1, 1, 0], 
          [0, 1, 1, 1, 1, 1, 1, 1, 0], 
          [0, 3, 1, 1, 1, 1, 1, 3, 0], 
          [0, 1, 3, 1, 1, 1, 3, 1, 0], 
          [0, 1, 1, 3, 3, 3, 1, 1, 0], 
          [0, 0, 0, 0, 0, 0, 0, 0, 0],
          [-1, -1, -1, -1, -1, -1, -1, -1, -1] ] # Fila extra para mostrar el texto

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

"""  #####################
    # FUNCIONES PROPIAS #
   #####################   """

# To-Do: migrar a función
for enemigo_a_spawnear in range(CANT_ENEMIGOS_A_SPAWNEAR):
    x = (random.randint(2, size_w - 2) * celda.width)
    y = (random.randint(2, size_h - 3) * celda.height)
    # To-Do: Agregar variable para determinar tipo de enemigo a spawnear
    # To-do: agregar una posicion especifica para que spawnee el jugador
    
    nvo_enemigo = Actor("enemy", topleft = (x, y))

    # Checkeamos que no se repitan las coordenadas
    posicion_duplicada = False
    for enemigo in lista_enemigos:
        if (nvo_enemigo.pos == enemigo.pos): # Si la posición de nvo_enemigo es IGUAL a la de CUALQUIER enemigo en la lista,
            posicion_duplicada = True        # Actualizamos la flag que indica que la posicion está duplicada
    if (posicion_duplicada):
        enemigo_a_spawnear -= 1              # restamos 1 al iterando (del for ppal)
    else:
        # Si la posición del nvo_enemigo es válida,
        nvo_enemigo.salud = random.randint(10, 20)
        nvo_enemigo.ataque = random.randint(5, 10)
        nvo_enemigo.bonus = random.randint(0, 2) # 0: nada, 1: curacion, 2: +atk
        lista_enemigos.append(nvo_enemigo)
    
def comprobar_fin_de_juego():
    global modo_actual, partida_finalizada, resultado_partida
    
    if (personaje.salud <= 0): # El personaje fue derrotado
        modo_actual = "transicion"
        partida_finalizada = True
        resultado_partida = "derrota"

    elif ((lista_enemigos == []) and (personaje.salud > 0)): # NOTA: tener en cuenta si se modifica el juego (bonus, transciciones, etc)
        modo_actual = "transicion"
        partida_finalizada = True
        resultado_partida = "victoria"
        
def draw():
    if (modo_actual == "juego"):
      screen.fill("#2f3542") # rgb = (47, 53, 66)
      dibujar_mapa(mapa_actual)
    
      for bonus in lista_bonus:
          bonus.draw()
    
      for enemigo in lista_enemigos:
          enemigo.draw()
    
      personaje.draw()
    
      screen.draw.text(("Salud: " + str(personaje.salud)), midleft=(30, (HEIGHT - int(celda.height/2))), color = 'white', fontsize = 24)
      screen.draw.text(("Ataque: " + str(personaje.ataque)), midright=((WIDTH - 30), (HEIGHT - int(celda.height/2))), color = 'white', fontsize = 24)
    
    elif (modo_actual == "transicion"):
        screen.fill("#2f3542")  # rgb = (47, 53, 66)
        if (partida_finalizada):
            if (resultado_partida == "victoria"):
                screen.draw.text("¡Ganaste!", center=(WIDTH/2, HEIGHT/3), color = 'white', fontsize = 46)
                screen.draw.text("Presiona [Espacio] para reiniciar", center=(WIDTH/2, HEIGHT/3 *2), color = 'white', fontsize = 24)
            else:
                screen.draw.text("¡Perdiste!", center=(WIDTH/2, HEIGHT/3), color = 'white', fontsize = 46)
                screen.draw.text("Presiona [Espacio] para reiniciar", center=(WIDTH/2, HEIGHT/3 *2), color = 'white', fontsize = 24)
        

def on_key_down(key):

  if (not partida_finalizada):
          
      global colision, resultado_partida
    
      pos_previa = personaje.pos
      
      if ((keyboard.right or keyboard.d) and (personaje.x < (WIDTH - celda.width * 2))):
        # ¿Xq 2?: Una (a la que me voy a desplazar) y otra (por la pared, que NO puedo atravesar)
        personaje.x += celda.width
        personaje.image = "stand" # xq stand mira a la dcha
            
      elif ((keyboard.left or keyboard.a) and (personaje.x > (celda.width * 2))):
        personaje.x -= celda.width
        personaje.image = "left" # xq mira a la izq
            
      elif ((keyboard.down or keyboard.s) and (personaje.y < HEIGHT - celda.height * 3)):
        # ¿Xq 3?: Una (a la que me voy a desplazar), otra (por la pared, que NO puedo atravesar) Y UNA TERCERA (para mostrar el texto)
        personaje.y += celda.height
        
      elif ((keyboard.up or keyboard.w) and (personaje.y > (celda.height * 2))):
            personaje.y -= celda.height
    
      # To-do: migrar a una funcion
      # To-do: porgramar victoria (eliminar a todos los enemigos) y derrota (personaje.salud <= 0)
    
    
      """ #################>>> COLISIONES CON ENEMIGOS <<<################# """
        
      colision = personaje.collidelist(lista_enemigos)
    
      if (colision != -1):
          # Si hubo colisión con un enemigo:
          personaje.pos = pos_previa
          
          enemigo_atacado = lista_enemigos[colision]
          enemigo_atacado.salud -= personaje.ataque
          personaje.salud -= enemigo_atacado.ataque
    
          if (enemigo_atacado.salud <= 0):
    
              """ 1º Chequeamos si tiene bonus: """
              if enemigo_atacado.bonus == 1:
                # Spawnear curacion
                nvo_bonus = Actor("heart", enemigo_atacado.pos)
                lista_bonus.append(nvo_bonus)
    
              elif enemigo_atacado.bonus == 2:
                # Spawnear bonus de ataque
                nvo_bonus = Actor("sword", enemigo_atacado.pos)
                lista_bonus.append(nvo_bonus)
    
              """ 2º Lo eliminamos """
              # Método #1:
              # lista_enemigos.pop(colision)
              # Método #2:
              lista_enemigos.remove(enemigo_atacado)
              # To-do: agregar pila de huesitos en la casilla donde derrote al esqueleto
              
      else: # Si NO hay colisión con enemigo:
          """ >>> COLISIONES CON BONUS <<< """
          for bonus in lista_bonus:
              if personaje.colliderect(bonus):
                  # Si hubo colisión contra un bonus:
                  if (bonus.image == "heart"):
                      personaje.salud += 15
                  elif (bonus.image == "sword"):
                      personaje.ataque += 5
                  lista_bonus.remove(bonus)
              
  comprobar_fin_de_juego()