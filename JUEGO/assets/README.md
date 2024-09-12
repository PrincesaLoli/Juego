# Shooter en Pygame

## Descripción
Este es un juego de disparos 2D simple desarrollado en Python utilizando la librería **Pygame**. El jugador controla una nave que debe disparar a los enemigos que se aproximan desde la parte superior de la pantalla. El objetivo es obtener la mayor puntuación posible.

## Requisitos
- Python 3.x
- Pygame (puedes instalarlo con `pip install pygame`)

## Funcionalidades
- Control de una nave espacial usando las teclas de flecha izquierda y derecha.
- Disparar balas con la barra espaciadora.
- Menú principal que inicia el juego cuando se presiona cualquier tecla.
- Enemigos que se generan aleatoriamente y se mueven hacia abajo.
- Puntuación basada en el número de enemigos destruidos.
- Mensaje de "Game Over" al perder

## Estructura del Proyecto
- `main.py`: Archivo principal que contiene la lógica del juego y el ciclo principal.
- `funciones.py`: Contiene funciones auxiliares como el menú, mostrar puntuación y el mensaje de "Game Over".
- `assets/`: Carpeta que contiene las imágenes utilizadas en el juego (por ejemplo, `player.png`, `enemy.png`).

## Controles
- Flecha izquierda: Mover la nave a la izquierda.
- Flecha derecha: Mover la nave a la derecha.
- Barra espaciadora
