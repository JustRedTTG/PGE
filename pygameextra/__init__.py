from os import environ, system
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import pygame.display
pygame.init()
pygame.display.init()
displaya = None
system("clear")
print("Pygame Extra 1.6.X is installed correctly!")
class Settings:
  update_auto = True
  update_onButton = False
  button_delay = 100
class display:
  def update():
    pygame.display.update()
  def set(dis):
    global displaya
    displaya = dis
  
  def make(size, caption):
    dis = pygame.display.set_mode(size)
    pygame.display.set_caption(caption)
    display.set(dis)
    return dis

  class blit:
    def rect(ob, rect):
      displaya.blit(ob, rect)
    def object(ob):
      displaya.blit(ob[0],ob[1])
class color:
  red = (255, 0, 0)
  green = (0, 255, 0)
  darkblue = (0, 0, 255)
  yellow = (255, 255, 0)
  lightblue = (0, 255, 255)
  pink = (255, 0, 255)
  white = (255, 255, 255)
  black = (0, 0, 0)
  lightgray = (200, 200, 200)
  gray = (100, 100, 100)
  darkgray = (50, 50, 50)

class draw:
  def line(color, pos, w, update=True):
    pygame.draw.line(displaya, color, (pos[0], pos[1]), (pos[2], pos[3]), w)
    if update:
      if Settings.update_auto:
        display.update()

  def rect(color, rect, w, update=True):
    pygame.draw.rect(displaya, color, rect, w)
    if update:
      if Settings.update_auto:
        display.update()

  def circle(color, pos, size, w):
    pygame.draw.circle(displaya, color, pos, size, w)
    if Settings.update_auto:
      display.update()

class fill:
  def full(color):
    displaya.fill(color)
    if Settings.update_auto:
      display.update()
class text:
  def auto(text, font, fontsize, pos, colors):
    color = colors[0]
    background = colors[1]
    font = pygame.font.Font(font, fontsize)
    texto = font.render(text, True, color, background)
    textRect = texto.get_rect()
    textRect.center = pos
    displaya.blit(texto, textRect)
    display.update()

  def make(atext, afont, afontsize, apos, acolors):
    acolor = acolors[0]
    abackground = acolors[1]
    class Text:
      def setup(self):
        self.text = atext
        self.font = afont
        self.fontsize = afontsize
        self.pos = apos
        self.color = acolor
        self.background = abackground
        self.fonto = None
        self.texto = None
        self.textRect = None
        return self
      def init(self):
        self.fonto = pygame.font.Font(self.font, self.fontsize)
        self.texto = self.fonto.render(self.text, True, self.color, self.background)
        self.textRect = self.texto.get_rect()
        self.textRect.center = self.pos

    ob = Text.setup(Text)
    ob.init(ob)
    return ob

  class quick:
    def make(texts, fontsize, pos):
      return text.make(texts,'freesansbold.ttf',fontsize,pos,((0,0,0),None))
    def small(texts, pos):
      return text.quick.make(texts, 20, pos)
    def medium(texts, pos):
      return text.quick.make(texts, 30, pos)
    def large(texts, pos):
      return text.quick.make(texts, 40, pos)
  def display(Text):
    displaya.blit(Text.texto, Text.textRect)
    if Settings.update_auto:
      display.update()
NoneText = text.quick.small('',(0,0)) #makes a quick button text
class time:
  def sleep(time):
    pygame.time.delay(time)
  def tick(tickrate=120):
    pygame.time.Clock().tick(tickrate)
def quit():
  pygame.quit()
def button(rect,ic,ac,Text=NoneText,action=None,data=None,tmp=True):
  if Text == None:
    global NoneText
    Text = NoneText
  else:
    Textq = Text
    Textq.pos = math.center(rect)
    Textq.init(Textq)
  pygame.event.get()
  mouse = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
  if rect[0]+rect[2] > mouse[0] > rect[0] and rect[1]+rect[3] > mouse[1] > rect[1]:
    draw.rect(ac, rect, 0, False)
    if click[0] == 1 and action != None:
      if data != None:
        action(data)
      else:
        action()
      if Settings.update_onButton:
        display.update()
      pygame.time.delay(Settings.button_delay)
  else:
    draw.rect(ic, rect, 0, False)
  displaya.blit(Textq.texto, Textq.textRect)
  if Settings.update_auto:
    display.update()
def button_image(rect,ic,ac,Text=NoneText,action=None,data=None,tmp=True):
  if Text == None:
    global NoneText
    Text = NoneText
  ic[1] = ic[0].get_rect(center = math.center(rect))
  ac[1] = ac[0].get_rect(center = math.center(rect))
  pygame.event.get()
  mouse = pygame.mouse.get_pos()
  click = pygame.mouse.get_pressed()
  if rect[0]+rect[2] > mouse[0] > rect[0] and rect[1]+rect[3] > mouse[1] > rect[1]:
    displaya.blit(ac[0],ac[1])
    if click[0] == 1 and action != None:
      if data != None:
        action(data)
      else:
        action()
      if Settings.update_onButton:
        display.update()
      pygame.time.delay(Settings.button_delay)
  else:
    displaya.blit(ic[0],ic[1])
  displaya.blit(Text.texto, Text.textRect)
  if Settings.update_auto:
    display.update()
class event:

  def quitcheck():
    tmp = False
    for event in pygame.event.get():
      if event.type == pygame.QUIT:
        tmp = True
    return tmp

class math:
  def center(rect):
    return ( (rect[0]+(rect[2]/2)), (rect[1]+(rect[3]/2)) )
  def perspective(point_a, point_b, length):
    a = pygame.math.Vector2(point_a)
    b = pygame.math.Vector2(point_b)
    dir = b - a
    dir.normalize_ip()
    dir *= length
    dest = a + dir
    return dest
class image:
  def load(file, size, position=(0,0)):
    image = [None] * 2
    image[0] = pygame.image.load(file).convert_alpha()
    image[0] = pygame.transform.scale(image[0],size)
    image[1] = image[0].get_rect(center = (position[0] + size[0] / 2, position[1] + size[1] / 2))
    return image
class sprite:
  def make(imagef, size, position=(0,0), rotation=90):
    class Sprite:
      def setup(self):
        self.image = image.load(imagef, size, position)
        self.image[0] = pygame.transform.rotozoom(self.image[0],rotation,1)
        self.rotation = rotation
        self.position = position
        self.rect = size
        self.size = 1
        self.new = self.image
        self.refresh = True
        return self
      def init_rotation(self):
        sprite_r = [None] * 2
        sprite_r[0] = pygame.Surface(self.image[0].get_size(),pygame.SRCALPHA)
        if self.rotation != 0:
          sprite_r[0] = pygame.transform.rotozoom(self.image[0],self.rotation,self.size)
        else:
          sprite_r[0] = self.image[0]
        sprite_r[1] = sprite_r[0].get_rect(center = self.image[1].center)
        self.new = sprite_r
        return self.new
      def init_position(self):
        sprite_r = [None] * 2
        sprite_r[0] = self.image
        sprite_r[1] = sprite_r[0].get_rect(center = (list(self.position)[0] + list(self.rect)[0] / 2, list(self.position)[1] + list(self.rect)[1] / 2))
        self.new = sprite_r
        return self.new
      def init(self):
        sprite_r = [None] * 2
        #sprite_r[0] = pygame.Surface(self.image[0].get_size(),pygame.SRCALPHA)
        if self.rotation != 0:
          sprite_r[0] = pygame.transform.rotozoom(self.image[0],self.rotation,self.size)
        else:
          sprite_r[0] = self.image[0]
        sprite_r[1] = sprite_r[0].get_rect(center = (list(self.position)[0] + list(self.rect)[0] / 2, list(self.position)[1] + list(self.rect)[1] / 2))
        self.new = sprite_r
        return self.new
    return Sprite.setup(Sprite)
