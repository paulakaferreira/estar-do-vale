import os

SCALE = 1

TILE_SIZE = 32
HALF_TILE = TILE_SIZE / 2

GRID_COLS = 16
GRID_ROWS = 9
SCREEN_WIDTH = GRID_COLS * TILE_SIZE
SCREEN_HEIGHT = GRID_ROWS * TILE_SIZE

ANTI_ALIASING = os.getenv("ANTI_ALIASING", "false").lower() == "true"
