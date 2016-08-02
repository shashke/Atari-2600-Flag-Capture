# config.py
# Settings
import pygame

RESOURCE_DIR = "res/"

SIZE = WIDTH, HEIGHT = 1280, 720

PADDLE_SIZE = PADDLE_WIDTH, PADDLE_HEIGHT = 20, 100

PLAYER1_CONTROLS = {
    "up": pygame.K_w,
    "down": pygame.K_s
}

PLAYER2_CONTROLS = {
    "up": pygame.K_UP,
    "down": pygame.K_DOWN
}