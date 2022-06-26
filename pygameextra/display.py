"""PYGAME EXTRA Display script
This script manages all display functions"""

import pygame
from pygameextra.modified import Surface

# Display MODES
DISPLAY_MODE_NORMAL = 0
DISPLAY_MODE_RESIZABLE = 1
DISPLAY_MODE_FULLSCREEN = 2
DISPLAY_MODE_HIDDEN = 3
DISPLAY_FLAG_MAP = {
    DISPLAY_MODE_NORMAL : 0,
    DISPLAY_MODE_RESIZABLE : pygame.RESIZABLE,
    DISPLAY_MODE_FULLSCREEN : pygame.FULLSCREEN,
    DISPLAY_MODE_HIDDEN : pygame.HIDDEN
}
# Display Others...
DISPLAY_DEFAULT_TITLE = "pygameextra window"
display_refrence = Surface

# Functions
def set_caption(title=DISPLAY_DEFAULT_TITLE): pygame.display.set_caption(title)
def set_icon(icon:Surface):
    surface = icon.surface
    if type(surface) == Surface: surface = surface.surface

    pygame.display.set_icon(surface)


def context(display:Surface):
    global display_refrence
    display_refrence = display

def make(size:tuple=(0, 0), title:str=DISPLAY_DEFAULT_TITLE, mode:int=DISPLAY_MODE_NORMAL):
    """Creates a window that the user can work with
    make(size, title, mode = 0) -> None

    Parameters:
        size -- A tuple (Width, Height), determains the size of the window
        title -- A string
    """
    flags = [] # Initiate a flags list
    final_flags = 0 # Initiate a final flags variable
    flags.append(DISPLAY_FLAG_MAP[mode])

    for item in flags: # Go through all the flags
        final_flags = final_flags | item # Combine all the flags into the final flags variable
    dis = pygame.display.set_mode(size, final_flags) # Create the display surface
    dis = Surface(surface=dis, layer=-1)

    set_caption(title)
    set_icon(Surface(surface=pygame.image.fromstring(b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00`\xb4\xff=^\xb4\xff\xffY\xb3\xf9(\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\\\xad\xf5\x19^\xb3\xfe\xfb^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xfe\xf3U\xbf\xff\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x80\xbf\xff\x04]\xb4\xfe\xe8^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb3\xfd\xd9\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00^\xb3\xfe\xc5^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xfe\xb0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00^\xb3\xfe\xf4^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb3\xff\x80\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00^\xb3\xfe\xf4^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xffL\x9e\xe5\xff/{\xbd\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff]\xb4\xffR\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00^\xb3\xfe\xf4^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xffT\xa8\xf1\xff/{\xbd\xff/{\xbd\xff/{\xbd\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xffY\xb3\xf9(\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00^\xb3\xfe\xf4^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xffZ\xaf\xf9\xff0|\xbe\xff/{\xbd\xff/{\xbd\xff/{\xbd\xff/{\xbd\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xfe\xf3U\xbf\xff\x0c\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00^\xb3\xfe\xf4^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff/{\xbd\xff/{\xbd\xff/{\xbd\xff/{\xbd\xff/{\xbd\xff/{\xbd\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff\\\xb0\xfa\xff_\xb3\xfd\x94\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00^\xb3\xfe\xf4^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff/{\xbd\xff/{\xbd\xff/{\xbd\xff/{\xbd\xff/{\xbd\xff/{\xbd\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff]\xb3\xfe\xffM\x98\xda\xffL\x96\xd7\xff_\xb3\xfd\x94\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00^\xb3\xfe\xf4^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff/{\xbd\xff/{\xbd\xff/{\xbd\xff/{\xbd\xff/{\xbd\xff/{\xbd\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xffO\x9c\xde\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xff_\xb3\xfd\x94\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00^\xb3\xfd\xf9^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff/{\xbd\xff/{\xbd\xff/{\xbd\xff/{\xbd\xff/{\xbd\xff/{\xbe\xff^\xb4\xff\xffS\xa1\xe5\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xff_\xb3\xfd\x94\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00]\xb2\xfd{^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff/{\xbd\xff/{\xbd\xff/{\xbd\xff/{\xbd\xffR\xa5\xed\xffj\xb9\xff\xffZ\xae\xf7\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xff_\xb3\xfd\x94\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00^\xb5\xffL^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff/{\xbd\xff/{\xbd\xffI\x9a\xe1\xfff\xb7\xff\xffx\xc0\xff\xffx\xc0\xff\xffZ\xae\xf7\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xff_\xb3\xfd\x94\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00_\xb6\xff#^\xb3\xfe\xfe^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xffA\x90\xd5\xffa\xb5\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffZ\xae\xf7\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xff_\xb3\xfd\x94\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00]\xb2\xfe\xb7^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xffv\xbf\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffZ\xae\xf7\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xffS\xa2\xe7\xff_\xb5\xfd\x83\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00]\xb4\xfe\xbf^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff\x8d\xca\xff\xff^\xb4\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffZ\xae\xf7\xffL\x96\xd7\xffL\x96\xd7\xffL\x96\xd7\xffP\x9d\xe1\xff^\xb3\xfe\xf1]\xa2\xff\x0b\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00]\xb4\xfe\xbf^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff\x84\xc5\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff^\xb4\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffZ\xae\xf7\xffL\x96\xd7\xffN\x99\xdb\xff]\xb3\xfd\xfeZ\xb3\xff%\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00]\xb4\xfe\xbf^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xffy\xc1\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff^\xb4\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xff[\xaf\xf8\xff\\\xb2\xfc\xff^\xb5\xffL\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00]\xb4\xfe\xbf^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff^\xb4\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffd\xb7\xff\xff]\xb2\xfd{\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00]\xb4\xfe\xbf^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff^\xb4\xff\xffx\xc0\xff\xffx\xc0\xff\xffx\xc0\xff\xffh\xb9\xff\xff]\xb4\xfd\xa7\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00]\xb4\xfe\xbf^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff^\xb4\xff\xffx\xc0\xff\xffm\xbb\xff\xff]\xb3\xfe\xd2\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00]\xb4\xfe\xbf^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff^\xb4\xff\xff]\xb4\xfe\xefU\xaa\xff\t\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00b\xb1\xff\r^\xb3\xfe\xf4^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x91\xcb\xff\xff_\xb4\xfe\xfec\xb8\xff$\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00Y\xb3\xf9(^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff\x96\xce\xff\xff\x96\xce\xff\xff\x95\xcd\xff\xffc\xb6\xff\xff^\xb2\xffI\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\\\xb3\xffP^\xb4\xff\xff^\xb4\xff\xff^\xb4\xff\xff\x96\xce\xff\xffk\xba\xff\xff_\xb4\xfft\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00_\xb3\xff|^\xb4\xff\xff\\\xb2\xfd\xa3\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00', (32, 32), 'RGBA')))

    context(dis)
    return dis

def update(area=None):
    if not area: pygame.display.flip()
    else : pygame.display.update(area)

def blit(object, pos=(0, 0), area=None):
    display_refrence.stamp(object, pos, area)