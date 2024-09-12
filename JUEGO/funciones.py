import pygame

# Función para mostrar el menú principal
def mostrar_menu(pantalla):
    fuente = pygame.font.Font(None, 74)
    texto = fuente.render("Presiona una tecla ", True, (200, 200, 200))
    pantalla.blit(texto, (50, 250))
    pygame.display.flip()

    esperando = True
    while esperando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                pygame.quit()
            if evento.type == pygame.KEYDOWN:
                esperando = False

# Función para mostrar la puntuación en pantalla
def mostrar_puntuacion(pantalla, puntuacion):
    fuente = pygame.font.Font(None, 36)
    texto = fuente.render(f"Puntuación: {puntuacion}", True, (255, 255, 255))
    pantalla.blit(texto, (10, 10))

# Función para mostrar el mensaje de "game over"
def game_over(pantalla):
    fuente = pygame.font.Font(None, 74)
    texto = fuente.render("GAME OVER", True, (255, 0, 0))
    pantalla.blit(texto, (250, 250))
    pygame.display.flip()

    pygame.time.wait(2000)
