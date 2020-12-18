from os import environ, system, path
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1'
import pygame
import pygame.display
pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512)
pygame.init()
pygame.display.init()
displaya = None
display_size = [0,0]
eventsl = None
system("clear")
print("Pygame Extra 1.6.4 is installed correctly!")
scriptpath = str(__file__).replace("__init__.py",'')
#RESOURCE LOADING# \/
slider_image = None
#RESOURCE LOADING# /\
#Emergency call functions# \/
def error(textS):
  pygame.quit()
  print(textS)
  pygame.init()
  pygame.display.init()
  global display
  global fill
  global time
  global text
  display.make((500, 100),"CRITICAL ERROR!")
  fill.full((255,255,255))
  text.display(text.quick.make(textS,15,(250,50)))
  display.update()
  time.sleep(10000)
  pygame.quit()
  quit()
#Emergency call functions# /\
class Settings:
  update_auto = True
  update_onButton = False
  button_delay = 100
  class button_lock:
    rect = True
    image = True
class pe_values:
  class mouse:
    in_use = False
  class last:
    mouse = (0,0)
    click = False
  class slider:
    start = (-10,-10)
    rect = (-10,-10,-10,-10)
    click = False
    drag = False
class display:
  def update():
    pygame.display.update()
  def set(dis):
    global displaya
    displaya = dis
  
  def make(size, caption):
    global display_size
    display_size[0] = size[0]
    display_size[1] = size[1]
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

  def ellipse(color, rect):
    pygame.draw.ellipse(displaya,color,rect)
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
NoneText = text.quick.small('',(0,0))
class time:
  def sleep(time):
    pygame.time.delay(time)
  def tick(tickrate=120):
    pygame.time.Clock().tick(tickrate)
def Pquit():
  pygame.quit()
  
class button:
  def rect(rect,ic,ac,Text=NoneText,action=None,data=None,tmp=True):
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
      pe_values.last.mouse = mouse
      if pe_values.last.click and not click[0] == 1:
        pe_values.last.click = False
        pe_values.mouse.in_use = False
      draw.rect(ac, rect, 0, False)
      if click[0] == 1 and action != None:
        mouse = pe_values.last.mouse
        click = pe_values.last.click
        if data != None:
          if (pe_values.mouse.in_use == False and rect[0]+rect[2] > mouse[0] > rect[0] and rect[1]+rect[3] > mouse[1] > rect[1] and not click) or not Settings.button_lock.rect:
            action(data)
            pe_values.last.click = True
            pe_values.last.mouse = pygame.mouse.get_pos()
        else:
          if (pe_values.mouse.in_use == False and rect[0]+rect[2] > mouse[0] > rect[0] and rect[1]+rect[3] > mouse[1] > rect[1] and not click) or not Settings.button_lock.rect:
            action()
            pe_values.last.click = True
            pe_values.last.mouse = pygame.mouse.get_pos()
        if Settings.update_onButton:
          display.update()
        pygame.time.delay(Settings.button_delay)
      else:
        pe_values.mouse.in_use = False
    else:
      #pe_values.last.click = False
      draw.rect(ic, rect, 0, False)
    displaya.blit(Textq.texto, Textq.textRect)
    if Settings.update_auto:
      display.update()
  def image(rect,ic,ac,action=None,data=None,tmp=True):
    ic[1] = ic[0].get_rect(center = math.center(rect))
    ac[1] = ac[0].get_rect(center = math.center(rect))
    pygame.event.get()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if rect[0]+rect[2] > mouse[0] > rect[0] and rect[1]+rect[3] > mouse[1] > rect[1]:
      pe_values.last.mouse = mouse
      if pe_values.last.click and not click[0] == 1:
        pe_values.last.click = False
        pe_values.mouse.in_use = False
      display.blit.object(ac)
      if click[0] == 1 and action != None:
        mouse = pe_values.last.mouse
        click = pe_values.last.click
        if data != None:
          if (pe_values.mouse.in_use == False and rect[0]+rect[2] > mouse[0] > rect[0] and rect[1]+rect[3] > mouse[1] > rect[1] and not click) or not Settings.button_lock.image:
            action(data)
            pe_values.last.click = True
            pe_values.last.mouse = pygame.mouse.get_pos()
        else:
          if (pe_values.mouse.in_use == False and rect[0]+rect[2] > mouse[0] > rect[0] and rect[1]+rect[3] > mouse[1] > rect[1] and not click) or not Settings.button_lock.image:
            action()
            pe_values.last.click = True
            pe_values.last.mouse = pygame.mouse.get_pos()
        if Settings.update_onButton:
          display.update()
        pygame.time.delay(Settings.button_delay)
      else:
        pe_values.mouse.in_use = False
    else:
      #pe_values.last.click = False
      display.blit.object(ic)
    if Settings.update_auto:
      display.update()
class slider:
  def normal(rect, imageS, minS, maxS, current, back, color, w, enableT=False, colorT=(255,255,255), wT=0):
    global slider_image
    global image
    global scriptpath
    global error
    saveU = Settings.update_auto
    Settings.update_auto = False
    rectE = False
    if imageS == None:
      if slider_image == None:
        try:
          slider_image = image.load(scriptpath + "files/slider.png",(25,25))
        except:
          error('Critical Error: file slider.png is missing, please reinstall pygameextra')
        imageQ = slider_image
      else:
        imageQ = slider_image
    else:
      if list(imageS) == [imageS[0],imageS[1],imageS[2]]:
        rectE = True
        try:
          slider_image = image.load(scriptpath + "files/slider.png",(15,25))
        except:
          error('Critical Error: file slider.png is missing, please reinstall pygameextra')
        imageQ = list(slider_image)
        imageQ[2] = list(imageQ[2])
        imageQ[2][1] = rect[3]
        imageQ[2] = tuple(imageQ[2])
      else:
        imageQ = imageS
    rectQ = list(rect)
    rectH = rectQ
    rectQ[2] = rectH[0] + rectH[2]
    rectQ[3] = rectH[1] + rectH[3]
    rectT = tuple(rectQ)
    #calculate \/
    pos = rect[0] + ((rect[2] / maxS) * current)
    #calculate /\
    rectIMAGE = rectQ
    imageIMAGE = imageQ
    rectV = [None] * 4
    rectV = rectQ
    rectV[1] = rectQ[3] - (imageQ[2][1] / 2)
    rectV[2] = (rectV[2] - rectV[0]) + imageIMAGE[2][0]
    rectV[0] -= (imageIMAGE[2][0] / 2)
    rectV[2] += 10
    rectV[0] += -5
    rectV = [rectV[0],rectV[1],rectV[2],rectV[3]]
    imageIMAGE[1] = imageIMAGE[0].get_rect(center = (pos, rectIMAGE[3]))
    if enableT:
      rectTT = list(rectT)
      rectTT[2] = pos
      rectTT[3] = rectIMAGE[3]
    if rectE:
      rectRECT = (pos - (rect[4] / 2), rectIMAGE[3] - (rect[3] / 2), (pos + (rect[4] / 2)) - (pos - (rect[4] / 2)), (rectIMAGE[3] + (rect[3] / 2)) - (rectIMAGE[3] - (rect[3] / 2)))
    pygame.event.get()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    rectB = [None] * 4
    #calculate \/
    rectB[0] = pos - (imageQ[2][0] / 2)
    rectB[1] = rectQ[3] - (imageQ[2][1] / 2)
    rectB[2] = imageQ[2][0]
    rectB[3] = imageQ[2][1]
    #calculate /\
    if rectB[0]+rectB[2] > mouse[0] > rectB[0] and rectB[1]+rectB[3] > mouse[1] > rectB[1]:
      state = True
    else:
      state = False
    rectV[3] = imageQ[2][1]
    #DRAW \/
    draw.rect(back, rectV,0,False)
    if enableT:
      rectTT[1] = rectTT[3]
      draw.line(color,tuple(rectTT),w,False)
      rectN = rectTT
      rectN[0] = rect[0] + rect[2]
      rectN[1] = rect[1] + rect[3]
      rectN[2] = rectTT[2]
      rectN[3] = rectTT[3]
      draw.line(colorT,tuple(rectN),wT,False)
    else:
      draw.line(color,rectT,w,False)
    if not rectE:
      display.blit.object(imageIMAGE)
    else:
      draw.rect(imageS,rectRECT,0)

    #DRAW /\
    if state:
      if click[0] == 1:
        pe_values.slider.click = True
        pe_values.slider.drag = True
        pe_values.slider.rect = rect
        pe_values.slider.start = mouse
      else:
        pe_values.slider.click = False
    if pe_values.slider.drag:
      if click[0] == 1 and pe_values.slider.click:
        if rect == pe_values.slider.rect:
          mX = mouse[0]
          mY = mouse[1]
          a = rect[0]
          b = rect[2]
          c = a + b
          #calculate \/
          if mX < a:
            mXc = a
          elif mX > c:
            mXc = c
          else:
            mXc = mX
          p = (mXc - a) / (b / maxS)
          current = p
          #calculate /\
      else:
        pe_values.slider.click = False
        pe_values.slider.drag = False
    Settings.update_auto = saveU
    return int(current)
  def boxed(rect, imageS, minS, maxS, current, back, lineout, color, enableT=False, colorT=(255,255,255)):
    rect = list(rect)
    rect[0] += 5
    rect = tuple(rect)
    global slider_image
    global image
    global scriptpath
    global error
    saveU = Settings.update_auto
    Settings.update_auto = False
    rectE = False
    w = 0
    wT = w
    m = False
    if imageS == None:
      if slider_image == None:
        try:
          slider_image = image.load(scriptpath + "files/slider.png",(25,25))
          w = 25
          wT = 25
        except:
          error('Critical Error: file slider.png is missing, please reinstall pygameextra')
        imageQ = slider_image
      else:
        imageQ = slider_image
    else:
      if list(imageS) == [imageS[0],imageS[1],imageS[2]]:
        rectE = True
        m = True
        try:
          slider_image = image.load(scriptpath + "files/slider.png",(15,25))
        except:
          if path.isfile(scriptpath + "files/slider.png"):
            slider_image = image.load(scriptpath + "files/slider.png",(15,25))
          else:
            error('Critical Error: file slider.png is missing, please reinstall pygameextra')
        imageQ = list(slider_image)
        imageQ[2] = list(imageQ[2])
        imageQ[2][1] = rect[3]
        imageQ[2] = tuple(imageQ[2])
      else:
        imageQ = imageS
    rectQ = list(rect)
    rectH = rectQ
    rectQ[2] = rectH[0] + rectH[2]
    rectQ[3] = rectH[1] + rectH[3]
    rectT = tuple(rectQ)
    #calculate \/
    pos = rect[0] + ((rect[2] / maxS) * current)
    #calculate /\
    rectIMAGE = rectQ
    imageIMAGE = imageQ
    rectV = [None] * 4
    rectV = rectQ
    rectV[1] = rectQ[3] - (imageQ[2][1] / 2)
    rectV[2] = (rectV[2] - rectV[0]) + imageIMAGE[2][0]
    rectV[0] -= (imageIMAGE[2][0] / 2)
    rectV = [rectV[0],rectV[1],rectV[2],rectV[3]]
    rectOP = rectV
    rectV[2] += 10
    rectV[0] += -5
    imageIMAGE[1] = imageIMAGE[0].get_rect(center = (pos, rectIMAGE[3]))
    if enableT:
      rectTT = list(rectT)
      rectTT[2] = pos
      rectTT[3] = rectIMAGE[3]
    if rectE:
      rectRECT = (pos - (rect[4] / 2), rectIMAGE[3] - (rect[3] / 2), (pos + (rect[4] / 2)) - (pos - (rect[4] / 2)), (rectIMAGE[3] + (rect[3] / 2)) - (rectIMAGE[3] - (rect[3] / 2)))
    pygame.event.get()
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    rectB = [None] * 4
    #calculate \/
    rectB[0] = pos - (imageQ[2][0] / 2)
    rectB[1] = rectQ[3] - (imageQ[2][1] / 2)
    rectB[2] = imageQ[2][0]
    rectB[3] = imageQ[2][1]
    #calculate /\
    if rectB[0]+rectB[2] > mouse[0] > rectB[0] and rectB[1]+rectB[3] > mouse[1] > rectB[1]:
      state = True
    else:
      state = False
    rectV[3] = imageQ[2][1] 
    #DRAW \/

    draw.rect(back, rectV,0,False)
    if not m:
      if enableT:
        draw.line(color,tuple(rectTT),w,False)
        rectN = rectTT
        rectN[0] = rect[0] + rect[2]
        rectN[1] = rect[1] + rect[3]
        rectN[2] = rectTT[2]
        rectN[3] = rectTT[3]
        draw.line(colorT,tuple(rectN),wT,False)
      else:
        draw.line(color,rectT,w,False)
    else:
      if enableT:
        rectOPT = list(rectOP)
        rectOPT[2] = pos - rectOPT[0]
        draw.rect(color,tuple(rectOPT),0,False)
        rectN = list(rectOP)
        rectN[0] = list(rectOPT)[0] + list(rectOPT)[2]
        rectN[2] = rect[2] - pos + rect[0] + 11
        draw.rect(colorT,tuple(rectN),0,False)
      else:
        draw.line(color,rectT,w,False)
    
    if not rectE:
      display.blit.object(imageIMAGE)
    else:
      draw.rect(imageS,rectRECT,0)
    draw.rect(lineout, rectV,1,False)
    #DRAW /\
    if state:
      if click[0] == 1:
        pe_values.slider.click = True
        pe_values.slider.drag = True
        pe_values.slider.rect = rect
        pe_values.slider.start = mouse
        pe_values.mouse.in_use = True
      else:
        pe_values.slider.click = False
    if pe_values.slider.drag:
      if click[0] == 1 and pe_values.slider.click:
        if rect == pe_values.slider.rect:
          pe_values.mouse.in_use = True
          mX = mouse[0]
          mY = mouse[1]
          a = rect[0]
          b = rect[2]
          c = a + b
          #calculate \/
          if mX < a:
            mXc = a
          elif mX > c:
            mXc = c
          else:
            mXc = mX
          p = (mXc - a) / (b / maxS)
          current = p
          #calculate /\
      else:
        pe_values.slider.click = False
        pe_values.slider.drag = False
        pe_values.mouse.in_use = False
    Settings.update_auto = saveU
    return int(current)
class event:
  c = None
  def get():
    tmp = pygame.event.get()
    if tmp != None:
      return tmp
  def quitcheck():
    tmp = False
    if event.c.type == pygame.QUIT:
      tmp = True
    return tmp
  def quitcheckauto():
    if event.quitcheck():
      pygame.quit()
      quit()
  def keylog():
    if event.c.type == pygame.KEYDOWN or event.c.type == pygame.KEYUP:
      return event.c.key
  def key_UP(var):
    if event.c.type == pygame.KEYUP:
      if event.c.key == var:
        return True
      else:
        return False
  def key_DOWN(var):
    if event.c.type == pygame.KEYDOWN:
      if event.c.key == var:
        return True
      else:
        return False
class mouse:
  def pos():
    #
    return pygame.mouse.get_pos()
  def clicked():
    r = [False] * 3
    m = pygame.mouse.get_pressed()
    if m[0] == 1:
      r[0] = True
    if m[1] == 1:
      r[1] = True
    if m[2] == 1:
      r[2] = True
    return r
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
  def display(image):
    display.blit.object(image)
  def load(file, size, position=(0,0)):
    image = [None] * 3
    image[0] = pygame.image.load(file).convert_alpha()
    image[0] = pygame.transform.scale(image[0],size)
    image[1] = image[0].get_rect(center = (position[0] + size[0] / 2, position[1] + size[1] / 2))
    image[2] = size
    return image
class sprite:
  def make(imagef, size, position=(0,0), rotation=0):
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
  def display(sprite):
    display.blit.object(sprite.new)
def rect(a,b,c,d):
  return pygame.Rect(a,b,c,d)
  #
class E_intro:
  def intro(anim,back,t):
    global display_size
    if display_size[0] >= 300 and display_size[1] >= 150:
      fx = (display_size[0] / 2) - 150
      fy = (display_size[1] / 2) - 50
      #INTRO \/
      fill.full(back)
      if anim != 0:
        time.sleep(anim)
      # P \/
      draw.rect(t,(0+fx,0+fy,25,125),0)
      if anim != 0:
        time.sleep(anim)
      draw.rect(t,(0+fx,0+fy,75,25),0)
      if anim != 0:
        time.sleep(anim)
      draw.rect(t,(50+fx,0+fy,25,75),0)
      if anim != 0:
        time.sleep(anim)
      draw.rect(t,(0+fx,50+fy,75,25),0)
      # P /\
      fx += 100             
      # G \/
      draw.rect(t,(0+fx,0+fy,75,25),0)
      if anim != 0:
        time.sleep(anim)
      draw.rect(back,(0+fx,50+fy,75,25),0)
      if anim != 0:
        time.sleep(anim)
      draw.rect(t,(0+fx,0+fy,25,125),0)
      if anim != 0:
        time.sleep(anim)
      draw.rect(t,(0+fx,100+fy,75,25),0)
      if anim != 0:
        time.sleep(anim)
      draw.rect(t,(50+fx,50+fy,25,75),0)
      # G /\
      fx += 100
      # E \/
      draw.rect(t,(0+fx,0+fy,75,25),0)
      if anim != 0:
        time.sleep(anim)
      draw.rect(t,(0+fx,50+fy,75,25),0)
      if anim != 0:
        time.sleep(anim)
      draw.rect(t,(0+fx,0+fy,25,125),0)
      if anim != 0:
        time.sleep(anim)
      draw.rect(t,(0+fx,100+fy,75,25),0)
      # E /\
      #INTRO /\

    else:
      print('======================================')
      print('resolution too small to display intro!')
      print('Try again with at least (300,150)')
      print('=================================')
  def run(tA=100,tB=100,tC=1000):
    E_intro.intro(tA,color.white,color.red) # Plays first intro
    time.sleep(tB)
    Settings.update_auto = False # Disables auto update
    E_intro.intro(0,color.black,(0,100,255)) # Plays second intro
    display.update() # updates
    time.sleep(tC)
    Settings.update_auto = True # Enables auto update
class sound:
  def load(file):
    return pygame.mixer.Sound(file)
  def play(soundOBJ):
    soundOBJ.play()
class music:
  volume = 100
  def load(file):
    pygame.mixer.music.load(file)
    
  def play(i=1):
    pygame.mixer.music.play(i-1)
    
  def unload():
    pygame.mixer.music.unload()
    
  def restart():
    pygame.mixer.music.rewind()
  
  def stop():
    pygame.mixer.music.stop()
    
  def pause():
    pygame.mixer.music.pause()
    
  def unpause():
    pygame.mixer.music.unpause()
    
  def fade(time):
    pygame.mixer.music.fadeout(time)
  
  def set_v(new_v):
    pygame.mixer.music.set_volume(new_v)
    music.volume = new_v
  def get_v():
    music.volume = pygame.mixer.music.get_volume()
    return music.volume
  def set_t(new_t):
    pygame.mixer.music.set_pos(new_t)
    
  def get_t():
    return pygame.mixer.music.get_pos()
  #