import pygame
import random
from funciones import mostrar_menu, mostrar_puntuacion, game_over

# Inicializar Pygame
pygame.init()

# Dimensiones de la pantalla
ANCHO = 800
ALTO = 600

# Colores
NEGRO = (0, 0, 0)
BLANCO = (255, 255, 255)

# Crear la pantalla
pantalla = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Shooter")

# Cargar imágenes
# Redimensionar las imágenes para ajustarlas al juego
jugador_img = pygame.transform.scale(pygame.image.load("assets/player.png"), (80, 80))  # Tamaño de 50x50 píxeles
enemigo_img = pygame.transform.scale(pygame.image.load("assets/enemy.png"), (50, 50))   # Tamaño de 40x40 píxeles
bala_img = pygame.transform.scale(pygame.image.load("assets/bullet.png"), (10, 20))     # Tamaño de 10x20 píxeles


# Jugador
jugador_x = ANCHO // 2 - 32
jugador_y = ALTO - 100
jugador_vel = 5

# Balas
bala_vel = -10
balas = []

# Enemigos
enemigos = []
enemigo_vel = 3
for i in range(5):
    enemigos.append([random.randint(0, ANCHO - 64), random.randint(-100, -40)])

# Puntuación
puntuacion = 0

# Reloj para FPS
reloj = pygame.time.Clock()

# Función principal del juego
def juego():
    global jugador_x, jugador_y, puntuacion

    # Loop principal del juego
    corriendo = True
    while corriendo:
        pantalla.fill(NEGRO)

        # Verificar eventos
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                corriendo = False

       # Controles del jugador
        teclas = pygame.key.get_pressed()
        if teclas[pygame.K_LEFT] and jugador_x > 0:
            jugador_x -= jugador_vel
        if teclas[pygame.K_RIGHT] and jugador_x < ANCHO - 50:
            jugador_x += jugador_vel
        if teclas[pygame.K_SPACE]:
            balas.append([jugador_x + 20, jugador_y])  # Ajusta la posición de la bala

        # Movimiento de las balas
        for bala in balas:
            bala[1] += bala_vel
            if bala[1] < 0:
                balas.remove(bala)

        # Movimiento de los enemigos
        for enemigo in enemigos:
            enemigo[1] += enemigo_vel
            if enemigo[1] > ALTO:
                enemigo[0] = random.randint(0, ANCHO - 64)
                enemigo[1] = random.randint(-100, -40)

        # Detectar colisión entre enemigo y jugador
            jugador_rect = pygame.Rect(jugador_x, jugador_y, 50, 50)  # Ajusta el tamaño del jugador
            enemigo_rect = pygame.Rect(enemigo[0], enemigo[1], 40, 40)  # Ajusta el tamaño del enemigo

            if jugador_rect.colliderect(enemigo_rect):
                game_over(pantalla)  # Mostrar "Game Over" cuando el jugador colisione con un enemigo
                corriendo = False  # Termina el juego después del "Game Over"

        # Detectar colisión entre balas y enemigos
        for bala in balas:
            for enemigo in enemigos:
                bala_rect = pygame.Rect(bala[0], bala[1], 10, 20)  # Ajusta el tamaño de la bala
                enemigo_rect = pygame.Rect(enemigo[0], enemigo[1], 40, 40)

                if bala_rect.colliderect(enemigo_rect):
                    balas.remove(bala)
                    enemigos.remove(enemigo)
                    enemigos.append([random.randint(0, ANCHO - 40), random.randint(-100, -40)])
                    puntuacion += 10


        # Dibujar el jugador
        pantalla.blit(jugador_img, (jugador_x, jugador_y))

        # Dibujar las balas
        for bala in balas:
            pantalla.blit(bala_img, (bala[0], bala[1]))

        # Dibujar enemigos
        for enemigo in enemigos:
            pantalla.blit(enemigo_img, (enemigo[0], enemigo[1]))

        # Mostrar puntuación
        mostrar_puntuacion(pantalla, puntuacion)

        # Actualizar la pantalla
        pygame.display.flip()

        # FPS
        reloj.tick(60)

    pygame.quit()

if __name__ == "__main__":
    mostrar_menu(pantalla)
    juego()
