# importar libreria
import pygame
# inicializando pygame
pygame.init()

# configuración de la ventana
screen = pygame.display.set_mode([800, 600])

# variables importantes
# running = si es true el juego esta corriendo, si no se cierra
running = True
#backgroundImage = ruta del fondo
backgroundImage = pygame.image.load('imgs/bg.png').convert()

# mientras running es verdadero el juego se muestra
while running:
  # busca constantemente los eventos (pygame.event)
  for event in pygame.event.get():
    # el tipo de evento: QUIT, cuando se apriete la X
    if event.type == pygame.QUIT:
      running = False
      print(f'Running value: {running}')
  # fondo (en colores) de la pantalla
  #screen.fill((190, 193, 54))
  # fondo imagen
  screen.blit(backgroundImage, [0, 0])

  # actualiza la 'screen'
  pygame.display.flip()
