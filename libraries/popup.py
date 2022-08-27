import pygameextra as pe
from libraries.roundrect import rect as roundrect
taken = None
taken_size = ()

font = pe.pygame.font.SysFont('freesans', 20)
class popup:
    def __init__(self, size: tuple, title: str = "Popup", position: tuple = None):
        global taken, taken_size
        taken = pe.display_a
        taken_size = pe.display.get.size()
        self.screen = pe.pygame.Surface(size,pe.pygame.SRCALPHA)
        pe.display.set(self.screen)
        self.size = size
        sizediv = (self.size[0] / 2, self.size[1] / 2)
        takendiv = (taken_size[0] / 2, taken_size[1] / 2)
        pos = (takendiv[0] - sizediv[0] + 20 * int(len(title) / 2.8), takendiv[1] - sizediv[1] + 12)
        if position != None:
            pos = list(position)
            pos[0] += 20 * int(len(title) / 2.8)
            pos[1] += 12
        if title != '':
            self.title = font.render(title, False, (0, 0, 0))
        else:
            self.title = None
        self.pos = (takendiv[0] - sizediv[0], takendiv[1] - sizediv[1])
        if position != None:
            self.pos = position
        pe.mouse.off = (self.pos[0] * -1, self.pos[1] * -1)

def close(popto):
    pop = popto.screen
    if popto.title != None:
        w, h = popto.title.get_size()
        pos = list(popto.pos)
        pos[0] += popto.size[0] / 2
        pos[0] -= w / 2
        roundrect((255, 255, 255, 100), (-5 + popto.size[0] / 2 - w / 2,-100,w + 10,100 + h + 2))
    pe.display.set(taken)
    pe.display.blit.rect(pop, popto.pos)
    if popto.title != None:
        pe.display.blit.rect(popto.title,pos)
