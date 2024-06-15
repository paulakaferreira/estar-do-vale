import os
from typing import Any

import pygame
from pygame.surface import Surface

from .settings import HEIGHT_RATIO, WIDTH_RATIO


def import_folder(path) -> list[Surface]:  # type: ignore
    sprite_list = []
    for folder_name, sub_folder, contents in os.walk(path):
        # TODO: this assumes sprites are ordered alphabetically, which is not true for numbered sprites beyond 9
        for content in sorted(contents):
            full_path = path + "/" + content
            # imports the image as a surface
            content_surf = pygame.image.load(full_path).convert_alpha()
            sprite_list.append(content_surf)
    return sprite_list


def handle_resize_event(event) -> tuple[float, float]:  # type: ignore
    # Imports from .settings: WIDTH_RATIO, HEIGHT_RATIO

    new_width = event.size[0]
    new_height = event.size[1]

    if (new_width / WIDTH_RATIO) != (new_height / HEIGHT_RATIO):
        # Uses height to set new screen width:
        new_width = new_height * (WIDTH_RATIO / HEIGHT_RATIO)

    new_size = (new_width, new_height)

    return new_size


def handle_sprite_position(self) -> Any:  # type: ignore
    sorted_sprites: Any = pygame.sprite.Group()
    for sprite in sorted(self.level.all_interactables.sprites(), key=lambda sprite: sprite.pos.y):
        sorted_sprites.add(sprite)
    return sorted_sprites


def blit_centered(surface: Surface, image: Surface) -> None:
    surface_width, surface_height = surface.get_size()
    image_width, image_height = image.get_size()

    x = (surface_width - image_width) // 2
    y = (surface_height - image_height) // 2

    surface.blit(image, (x, y))  # draw the background


def ratio_to_lefttop(ratio: tuple[float, float], width_height: tuple[float, float]) -> tuple[float, float]:
    surface = pygame.display.get_surface()
    surface_width, surface_height = surface.get_size()
    image_width, image_height = width_height

    x = (surface_width - image_width) * ratio[0]
    y = (surface_height - image_height) * ratio[1]

    return (x, y)
