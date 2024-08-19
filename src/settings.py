import os

SCALE = 1

TILE_SIZE = 32
HALF_TILE = TILE_SIZE / 2

GRID_WIDTH = 16
GRID_HEIGHT = 9
SCREEN_WIDTH = GRID_WIDTH * TILE_SIZE
SCREEN_HEIGHT = GRID_HEIGHT * TILE_SIZE

ANTI_ALIASING = os.getenv("ANTI_ALIASING", "false").lower() == "true"
DEFAULT_FPS = 120
