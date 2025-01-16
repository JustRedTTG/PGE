import os
from abc import ABC
from typing import Union

import pygame
import pygame_shaders

from pygameextra import GameContext, display, Surface, event
import moderngl


class ErrorFix:
    Error = moderngl.Error


setattr(moderngl, 'error', ErrorFix)


class ShaderBackedSurface(Surface):
    def __init__(self):
        super().__init__(display.get_size())
        self._default_shader = pygame_shaders.DefaultScreenShader(self.surface)

    def render(self):
        self._default_shader.render()

    def resize(self, size: tuple):
        if size == self.size:
            return
        super().resize(size)
        self._default_shader.target_surface = self.surface
        self._default_shader.render_rect.size = size
        self._default_shader.window_size = size
        self._default_shader.screen_texture = pygame_shaders.Texture(pygame.Surface(size),
                                                                     self._default_shader.ctx)
        self._default_shader.framebuffer = self._default_shader.ctx.simple_framebuffer(size=size,
                                                                                       components=4)
        self._default_shader.scope = self._default_shader.ctx.scope(self._default_shader.framebuffer)

    def stamp(self, source: Union['Surface', pygame.Surface], position: tuple = (0, 0), area: tuple = None,
              special_flags: int = 0):
        super().stamp(source, position, area, special_flags | pygame.BLEND_RGBA_ADD)

    @property
    def ctx(self):
        return self._default_shader.ctx


class ShaderGameContext(GameContext, ABC):
    surface: ShaderBackedSurface

    def __init__(self):
        for flag in (pygame.OPENGL, pygame.DOUBLEBUF, pygame.HWSURFACE):
            if flag not in self.FLAGS:
                self.FLAGS.append(flag)
        super().__init__()
        self.window = display.display_reference
        self.surface = ShaderBackedSurface()
        display.context(self.surface)

    def handle_event(self, e: event.Event):
        super().handle_event(e)
        if e.type == pygame.WINDOWRESIZED:
            self.surface.resize((e.x, e.y))

    def update(self):
        self.surface.render()
        display.update(self.FPS)

    def end_loop(self):
        self.surface.render()
        super().end_loop()
