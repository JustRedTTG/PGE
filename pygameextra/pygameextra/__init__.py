"""Pygame Extra"""
from os import environ, path, mkdir, getcwd
environ['PYGAME_HIDE_SUPPORT_PROMPT'] = '1' # disable pygame's hello message, sorry pygame ;-;
from pygameextra.install import install, requests, pygame, system
import pygameextra.settings as Settings
pe_values, rect, pivot, color = None, None, None, None # Nill variables
NoneText, display_a, display_size, eventsl, scriptpath, slider_image = None, None, None, None, None, None # Nill variables


# layer setup \/
Layer = [None] * 17
for x in range(0,17):
    Layer[x] = [True, (0,0)]
    #
# layer setup /\


# DEVELOPER OPTIONS!
__version__ = "1.6.5.1" # developers, please change this accordingly when developing!
modified = False # developers, please set this to True when developing!
# DEVELOPER OPTIONS!

def preinit():
    """preinit() -> None
    Imports important functions to prepare for init
    """
    global pe_values, rect, pivot, color
    # IMPORTING Pygame Extra sub-modules
    import pygameextra.values as pe_values
    import pygameextra.rect
    rect.pygame = pygame
    rect = rect.rect
    import pygameextra.pivot
    import pygameextra.colors as color

preinit()

def init():
    """init() -> None
    Makes sure Pygame Extra is ready for operation
    """
    global NoneText, display_a, display_size, eventsl, scriptpath, slider_image
    pygame.mixer.pre_init(frequency = 44100, size = 16, channels = 1, buffer = 512)
    pygame.init()
    pygame.display.init()
    display_a = None
    display_size = [0,0]
    eventsl = None
    scriptpath = str(path.realpath(__file__)).replace("__init__.py",'')
    #RESOURCE LOADING# \/
    slider_image = None
    #RESOURCE LOADING# /\
    NoneText = text.quick.small('', (0, 0))  # an empty placeholder text if you don't supply text objects to functions

    if False: # this scraps the old installation of updates
        #check instalation...
        if path.isfile(scriptpath + "files/install.info"):
            infof = open(scriptpath + "files/install.info", "a+")
            infof.seek(0)
            data = infof.read()
            ver = open(path.join(scriptpath, "files/version.info"), "a+")
            ver.seek(0)
            if data == "no install" or ver.read() != requests.get("https://redstonehair.000webhostapp.com/pygame%20extra/"+__version__+"/files/version,info", timeout=5).content.decode('ascii'):
                if Settings.INIT_TEXT:
                    if modified:
                        print("Pygame Extra " + __version__ + " (modified) is installed with missing files")
                        print("We don't supply resources to modified versions, so please contact the modifier for files")
                        pygame.quit()
                        exit()
                    else:
                        print("Pygame Extra " + __version__ + " isn't fully installed yet!")
                        print("Starting Instalation of "+__version__)
                        install(scriptpath=scriptpath,__version__=__version__)
            elif "in " in data:
                if modified:
                    print("Pygame Extra " + __version__ + " (modified) is installed with missing files")
                    print("We don't supply resources to modified versions, so please contact the modifier for files")
                    pygame.quit()
                    exit()
                else:
                    print("Pygame Extra " + __version__ + " isn't fully installed yet!")
                    print("Continuing Instalation of " + __version__)
                    install(progress=int(data.replace("in ", "")), scriptpath=scriptpath, __version__=__version__)
            elif data == "installed":
                if Settings.INIT_TEXT:
                    if modified:
                        print("Pygame Extra " + __version__ + " (modified) is installed!")
                        print("Please note we don't take consequnces of using this modified version, use at your own risk!")
                    else:
                        print("Pygame Extra " + __version__ + " is installed correctly!")
        elif path.exists(scriptpath + "files"):
            open(scriptpath + "files/install.info", "w").write("no install")
        else:
            mkdir(scriptpath + "files")
            open(scriptpath + "files/install.info", "w").write("no install")
            infof = open(scriptpath + "files/install.info", "a+")
            infof.seek(0)
            data = infof.read()
            ver = open(path.join(scriptpath, "files/version"), "a+")
            ver.seek(0)
            if data == "no install" or ver.read() != requests.get(
                    "https://redstonehair.000webhostapp.com/pygame%20extra/"+__version__+"/files/version.txt",
                    timeout=5).content.decode('ascii'):
                if Settings.INIT_TEXT:
                    if modified:
                        print("Pygame Extra " + __version__ + " (modified) is installed with missing files")
                        print("We don't supply resources to modified versions, so please contact the modifier for files")
                        pygame.quit()
                        exit()
                    else:
                        print("Pygame Extra " + __version__ + " isn't fully installed yet!")
                        print("Starting Instalation of " + __version__)
                        install(scriptpath=scriptpath, __version__=__version__)
            elif "in " in data:
                if modified:
                    print("Pygame Extra " + __version__ + " (modified) is installed with missing files")
                    print("We don't supply resources to modified versions, so please contact the modifier for files")
                    pygame.quit()
                    exit()
                else:
                    print("Pygame Extra " + __version__ + " isn't fully installed yet!")
                    print("Continuing Instalation of " + __version__)
                    install(progress=int(data.replace("in ", "")), scriptpath=scriptpath, __version__=__version__)
            elif data == "installed":
                if Settings.INIT_TEXT:
                    if modified:
                        print("Pygame Extra " + __version__ + " (modified) is installed!")
                        print("Please note we don't take consequnces of using this modified version, use at your own risk!")
                    else:
                        print("Pygame Extra " + __version__ + " is installed correctly!")
    else:
        if modified:
            print("Pygame Extra " + __version__+" modified")
        else:
            print("Pygame Extra " + __version__)
    print("Join our discord: " + "https://discord.gg/8CKtZpYrdj")


def error(textS):
    """error(text) -> None
    Used to display an error message that is more user friendly than command-line errors
    """
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
    sl = 0
    while True:
        for x in pygame.event.get():
            if x is not None:
                if x.type == pygame.QUIT:
                    pygame.quit()
                    quit()
        time.sleep(1)
        sl += 1
        if sl >= 10000:
            pygame.quit()
            quit()


class display:
    def update():
        """update() -> None
        Used to update the screen"""
        pygame.display.flip()
    def set(dis):
        """set(Display_Surface) -> None
        Used by display.make to set the current display in use"""
        global display_a
        display_a = dis
    
    def make(size, caption, mode=0, check=False):
        """make(size, caption, mode) -> Display Surface
        Setup the display surface"""
        global display_size
        display_size = size
        if mode == 0:
            dis = pygame.display.set_mode(size)
            pygame.display.set_caption(caption)
            display.set(dis)
        elif mode == 1:
            dis = pygame.display.set_mode(size, pygame.RESIZABLE)
            pygame.display.set_caption(caption)
            display.set(dis)
        elif mode == 2:
            dis = pygame.display.set_mode(size, pygame.FULLSCREEN)
            pygame.display.set_caption(caption)
            display.set(dis)
        if check:
            m = pygame.display.Info()
            ms = (m.current_w,m.current_h)
            if ms[0] and ms[1]>=720:
                pass
            else:
                error("Screen size too small")
                pygame.quit()
                quit()
        return dis
    class get:
        def size():
            """size() -> Tuple
            Get display_a's changed size"""
            x = display_a.get_width()
            y = display_a.get_height()
            return (x, y)
        def Msize():
            """Msize() -> Tuple
            The same as size()"""
            m = pygame.display.Info()
            return (m.current_w,m.current_h)
    class blit:
        def rect(ob, rect):
            """rect(object, rect) -> None
            Blit a object and a rect seperately"""
            display_a.blit(ob, rect)
        def object(ob):
            """object([object, rect]) -> None
            Blit a list with an object and rect"""
            display_a.blit(ob[0],ob[1])


class draw:
    def line(color, pos_a, pos_b, w, update=True, layer=0):
        """line(color, (position_a, position_b), width) -> None
        Draws a line across two points
        """
        pos = (pos_a[0], pos_a[1], pos_b[0], pos_b[1])
        if Layer[layer][0]:
            pygame.draw.line(display_a, color, (pos[0]+Layer[layer][1][0], pos[1]+Layer[layer][1][1]), (pos[2]+Layer[layer][1][0], pos[3]+Layer[layer][1][1]), w)
            if Settings.UPDATE_AUTO and update:
                    display.update()

    def rect(color, rect, w, update=True, layer=0):
        """rect(color, rect, width) -> None
        Draws a rectangle
        """
        if Layer[layer][0]:
            pygame.draw.rect(display_a, color, (rect[0]+Layer[layer][1][0], rect[1]+Layer[layer][1][1], rect[2], rect[3]), w)
            if Settings.UPDATE_AUTO and update:
                    display.update()

    def circle(color, pos, size, w, update=True, layer=0):
        """circle(color, position, radius, width) -> None
        Draws a circle
        """
        if Layer[layer][0]:
            pygame.draw.circle(display_a, color, (pos[0]+Layer[layer][1][0], pos[1]+Layer[layer][1][1]), size, w)
            if Settings.UPDATE_AUTO and update:
                display.update()

    def ellipse(color, rect, update=True, layer=0):
        """ellipse(color, rect) -> None
        Draws a filled circle within a rect
        """
        if Layer[layer][0]:
            pygame.draw.ellipse(display_a,color,(rect[0]+Layer[layer][1][0], rect[1]+Layer[layer][1][1], rect[2], rect[3]))
        if Settings.UPDATE_AUTO and update:
            display.update()


class fill:
    def full(color, update=True, layer=0):
        """fill(color)
        Fills the full screen with a color
        """
        if Layer[layer][0]:
            display_a.fill(color)
            if Settings.UPDATE_AUTO and update:
                display.update()


class text:
    def auto(text, font, fontsize, pos, colors, layer=0):
        """no info :("""
        if Layer[layer][0]:
            color = colors[0]
            background = colors[1]
            font = pygame.font.Font(font, fontsize)
            texto = font.render(text, True, color, background)
            textRect = texto.get_rect()
            textRect.center = pos
            display_a.blit(texto, textRect)
            display.update()

    def make(atext, afont, afontsize, apos, acolors, layer=0):
        """make(text, font, fontsize, position, [color, background]) -> Text Object
        Makes a text object
        """
        acolor = acolors[0]
        abackground = acolors[1]
        class Text:
            def setup(self):
                self.text = atext
                self.font = afont
                self.fontsize = afontsize
                self.pos = (apos[0]+Layer[layer][1][0], apos[1]+Layer[layer][1][0])
                self.original_pos = apos
                self.color = acolor
                self.background = abackground
                self.fonto = None
                self.texto = None
                self.textRect = None
                self.layer = layer
                return self
            def init(self):
                self.pos = (self.original_pos[0]+Layer[self.layer][1][0], self.original_pos[1]+Layer[self.layer][1][0])
                self.fonto = pygame.font.Font(self.font, self.fontsize)
                self.texto = self.fonto.render(self.text, True, self.color, self.background)
                self.textRect = self.texto.get_rect()
                self.textRect.center = self.pos

        ob = Text.setup(Text)
        ob.init(ob)
        return ob

    class quick:
        def make(texts, fontsize, pos, layer=0):
            """make(text, fontsize, position) -> Text Object
            Quickly makes a custom sized text object
            """
            return text.make(texts,'freesansbold.ttf',fontsize,pos,((0,0,0),None), layer=layer)
        def small(texts, pos, layer=0):
            """small(text, position) -> Text Object
            Quickly makes a small text object
            """
            return text.quick.make(texts, 20, pos, layer=layer)
        def medium(texts, pos, layer=0):
            """medium(text, position) -> Text Object
            Quickly makes a medium text object
            """
            return text.quick.make(texts, 30, pos, layer=layer)
        def large(texts, pos, layer=0):
            """large(text, position) -> Text Object
            Quickly makes a large text object
            """
            return text.quick.make(texts, 40, pos, layer=layer)
    def display(Text, update=True):
        """display(Text_Object) -> None
        Displays a text object
        """
        if Layer[Text.layer][0]:
            display_a.blit(Text.texto, Text.textRect)
            if Settings.UPDATE_AUTO and update:
                display.update()


class time:
    def sleep(time):
        """sleep(time) -> None
        Halts the program for the specified time
        """
        pygame.time.delay(time)
    def tick(tickrate=120):
        """tick(tickrate) -> None
        Sets the maximum frames per second
        """
        pygame.time.Clock().tick(tickrate)


def Pquit():
    """Pquit() -> None
    Quits pygame
    """
    pygame.quit()


class button:
    def rect(rect,ic,ac,Text=NoneText,action=None,data=None,tmp=True,update=True,layer=0):
        """rect(rect, color_idle, color_active, Text_Object, action, data -> None
        Draws a rectanular colored button (optionally with text)
        """
        if Layer[layer][0]:
            if Text == None:
                global NoneText
                Text = NoneText
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
                draw.rect(ac, rect, 0, False, layer=layer)
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
                    if Settings.UPDATE_ON_BUTTON:
                        display.update()
                    pygame.time.delay(Settings.BUTTON_DELAY)
                else:
                    pe_values.mouse.in_use = False
            else:
                #pe_values.last.click = False
                draw.rect(ic, rect, 0, False, layer=layer)
            display_a.blit(Textq.texto, Textq.textRect)
            if Settings.UPDATE_AUTO and update:
                display.update()
    def image(rect,ic,ac,action=None,data=None,tmp=True,update=True,layer=0):
        """image(rect, image_idle, image_active, action, data) -> None
        Blits a image button on screen
        """
        if Layer[layer][0]:
            ic.rect = ic.object.get_rect(center = math.center(rect))
            ac.rect = ac.object.get_rect(center = math.center(rect))
            pygame.event.get()
            mouse = pygame.mouse.get_pos()
            click = pygame.mouse.get_pressed()
            if rect[0]+rect[2] > mouse[0] > rect[0] and rect[1]+rect[3] > mouse[1] > rect[1]:
                pe_values.last.mouse = mouse
                if pe_values.last.click and not click[0] == 1:
                    pe_values.last.click = False
                    pe_values.mouse.in_use = False
                ac.display()
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
                    if Settings.UPDATE_ON_BUTTON:
                        display.update()
                    pygame.time.delay(Settings.BUTTON_DELAY)
                else:
                    pe_values.mouse.in_use = False
            else:
                #pe_values.last.click = False
                ic.display()
            if Settings.UPDATE_AUTO and update:
                display.update()


class slider:
    def normal(rect, imageS, minS, maxS, current, back, color, w, enableT=False, colorT=(255,255,255), wT=0, layer=0):
        """normal(rect, image/color, min, max, current, color_background, color1, width1, enable2, color2, width2) -> Int
        Draws a slider without a outsize box. Returns the new current
        """
        if Layer[layer][0]:
            global slider_image
            global image
            global scriptpath
            global error
            saveU = Settings.UPDATE_AUTO
            Settings.UPDATE_AUTO = False
            rectE = False
            if imageS == None:
                if slider_image == None:
                    try:
                        slider_image = image(scriptpath + "files/slider.png",(25,25)).old
                    except:
                        error('Critical Error: file slider.png is missing, please reinstall pygameextra')
                    imageQ = slider_image
                else:
                    imageQ = slider_image
            else:
                if list(imageS) == [imageS[0],imageS[1],imageS[2]]:
                    rectE = True
                    try:
                        slider_image = image(scriptpath + "files/slider.png",(15,25)).old
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
                draw.line(color, (rectTT[0], rectTT[1]), (rectTT[2], rectTT[3]), w, False)
                rectN = rectTT
                rectN[0] = rect[0] + rect[2]
                rectN[1] = rect[1] + rect[3]
                rectN[2] = rectTT[2]
                rectN[3] = rectTT[3]
                draw.line(colorT, (rectN[0], rectN[1]), (rectN[2], rectN[3]), wT, False)
            else:
                draw.line(color, (rectT[0], rectT[1]), (rectT[2], rectT[3]), w, False)
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
            Settings.UPDATE_AUTO = saveU
        return int(current)
    def boxed(rect, imageS, minS, maxS, current, back, lineout, color, enableT=False, colorT=(255,255,255), layer=0):
        """boxed(rect, image/color, min, max, current, color_background, outLine, color1, enable2, color2) -> Int
        Draws a slider with a outsize box. Returns the new current
        """
        if Layer[layer][0]:
            rect = list(rect)
            rect[0] += 5
            rect = tuple(rect)
            global slider_image
            global image
            global scriptpath
            global error
            saveU = Settings.UPDATE_AUTO
            Settings.UPDATE_AUTO = False
            rectE = False
            w = 0
            wT = w
            m = False
            if imageS == None:
                if slider_image == None:
                    try:
                        slider_image = image(scriptpath + "files/slider.png",(25,25)).old
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
                        slider_image = image(scriptpath + "files/slider.png",(15,25)).old
                    except:
                        if path.isfile(scriptpath + "files/slider.png"):
                            slider_image = image(scriptpath + "files/slider.png",(15,25)).old
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
            Settings.UPDATE_AUTO = saveU
        return int(current)


class event:
    c = None
    def get():
        """get() -> List
        Gets and returns the event list
        """
        tmp = pygame.event.get()
        if tmp != None:
            return tmp
    def quitcheck():
        """quitcheck() -> Bool
        Checks if the window was attempted to be closed and returns a bool accordingly
        """
        tmp = False
        if event.c.type == pygame.QUIT:
            tmp = True
        return tmp
    def quitcheckauto():
        """quitcheckauto() -> None
        Checks if the window has been closed and automatically quits the program
        """
        if event.quitcheck():
            pygame.quit()
            quit()
    def keylog():
        """keylog() -> int
        Returns all the button pressed or released
        """
        if event.c.type == pygame.KEYDOWN or event.c.type == pygame.KEYUP:
            return event.c.key
    def key_UP(var):
        """key_UP(key) -> Bool
        Check if a button has been released and returns a bool accordingly
        """
        if event.c.type == pygame.KEYUP:
            if event.c.key == var:
                return True
            else:
                return False
    def key_DOWN(var):
        """key_DOWN(key) -> Bool
        Checks if a key is pressed and returns a bool accordingly
        """
        if event.c.type == pygame.KEYDOWN:
            if event.c.key == var:
                return True
            else:
                return False


class mouse:
    def pos():
        """pos() -> Tuple
        Gets and returns the mouse position on the open window
        """
        return pygame.mouse.get_pos()
    def clicked():
        """clicked() -> List
        Checks and returns a list with bools depending witch button is pressed [Left, Middle, Right]
        """
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
        """center(rect) -> Tuple
        Calculates the center of a rectangle
        """
        return ( (rect[0]+(rect[2]/2)), (rect[1]+(rect[3]/2)) )
    def lerp(point_a, point_b, length):
        a = pygame.math.Vector2(point_a)
        b = pygame.math.Vector2(point_b)
        dir = b - a
        try:
            dir.normalize_ip()
        except:
            pass
        dir *= length
        dest = a + dir
        return dest


class image:
    def display(self, layer=0):
        """Image_Object.display() -> None
        Displays a image object
        """
        if Layer[layer][0]:
            size = self.size
            position = self.position
            self.rect = self.object.get_rect(center=((position[0] + size[0] / 2)+Layer[layer][1][0], (position[1] + size[1] / 2)+Layer[layer][1][1]))
            display.blit.rect(self.object, self.rect)
    def __init__(self, file, size=None, position=(0,0)):
        """image.(file, size, position) -> Image Object
        Makes a image object
        """
        try:
            self.object = pygame.image.load(file).convert_alpha()
            self.Asize = self.object.get_size()
        except:
            print("file: "+str(file)+" doesn't exist")
            error("File doesn't exist 'Image.__init__()'")
        if size != None:
            self.object = pygame.transform.scale(self.object,size)
        self.rect = self.object.get_rect(topleft = (position[0], position[1]))
        self.size = size
        self.position = position
        self.old = [self.object, self.rect, self.size, self.position, self.Asize]


class sheet:
    columns = 0
    rows = 1
    def __init__(self, file, cellsize, type=1, offset=(0, 0)):
        """sheet(file, cellSize, type, Start_offset) -> Sheet Object
        Returns a simple sheet object containing details of a sprite sheet
        """
        self.file = file
        self.cellsize = cellsize
        self.type = type
        self.offset = offset


if True:
        class Sprite:
            def __init__(self, imagef, size, position=(0,0), rotation=0, pivot="center", layer=0):
                """Sprite(file/files/image/images/sheet_object, size, position, rotation, pivot) -> Sprite Object
                Makes and initializes a sprite object
                """
                if isinstance(imagef, list):
                    if isinstance(imagef[0], list):
                        imagef = [imagef]
                else:
                    imagef = [imagef]
                    #
                self.sheet_e = False
                self.frames = len(imagef)
                self.fx = 0
                if isinstance(imagef[0], image):
                    self.image = [None] * len(imagef)
                    i = 0
                    for x in imagef:
                        self.image[i] = imagef[i]
                        if rotation > 0:
                            self.image[i].object = pygame.transform.rotozoom(self.image[i].object, rotation, 1)
                        self.image[i].object = pygame.transform.scale(self.image[i].object, size)
                        sprite_r = self.image[i]
                        sizev = (size[0]/2,size[1]/2)
                        if pivot == "center":
                            sprite_r.rect = sprite_r.object.get_rect(center=(list(position)[0] + Layer[layer][1][0] + sizev[0],list(position)[1] + Layer[layer][1][1] + sizev[1]))
                        elif pivot == "left":
                            sprite_r.rect = sprite_r.object.get_rect(left=(list(position)[0] + Layer[layer][1][0] + sizev[0],list(position)[1] + Layer[layer][1][1] + sizev[1]))
                        elif pivot == "right":
                            sprite_r.rect = sprite_r.object.get_rect(right=(list(position)[0] + Layer[layer][1][0] + sizev[0],list(position)[1] + Layer[layer][1][1] + sizev[1]))
                        elif pivot == "top":
                            sprite_r.rect = sprite_r.object.get_rect(top=(list(position)[0] + Layer[layer][1][0] + sizev[0],list(position)[1] + Layer[layer][1][1] + sizev[1]))
                        elif pivot == "topleft":
                            sprite_r.rect = sprite_r.object.get_rect(topleft=(list(position)[0] + Layer[layer][1][0] + sizev[0],list(position)[1] + Layer[layer][1][1] + sizev[1]))
                        elif pivot == "topright":
                            sprite_r.rect = sprite_r.object.get_rect(topright=(list(position)[0] + Layer[layer][1][0] + sizev[0],list(position)[1] + Layer[layer][1][1] + sizev[1]))
                        elif pivot == "bottom":
                            sprite_r.rect = sprite_r.object.get_rect(bottom=(list(position)[0] + Layer[layer][1][0] + sizev[0],list(position)[1] + Layer[layer][1][1] + sizev[1]))
                        elif pivot == "bottomleft":
                            sprite_r.rect = sprite_r.object.get_rect(bottomleft=(list(position)[0] + Layer[layer][1][0] + sizev[0],list(position)[1] + Layer[layer][1][1] + sizev[1]))
                        elif pivot == "bottomright":
                            sprite_r.rect = sprite_r.object.get_rect(bottomright=(list(position)[0] + Layer[layer][1][0] + sizev[0],list(position)[1] + Layer[layer][1][1] + sizev[1]))
                        self.image[i] = sprite_r
                        i += 1
                elif isinstance(imagef[0], sheet):
                    self.sheet = imagef[0]
                    self.image = image(self.sheet.file, position=position)
                    sd = (int((self.image.Asize[0]/self.sheet.cellsize[0])*size[0]), int((self.image.Asize[1]/self.sheet.cellsize[0])*size[1]))
                    self.frames = 0
                    self.fx = [0,0]
                    self.frames = int(self.image.Asize[0]/self.sheet.cellsize[0])*int(self.image.Asize[1]/self.sheet.cellsize[1])
                    if self.sheet.type == 1:
                        self.fx[0] = int(self.image.Asize[0]/self.sheet.cellsize[0])
                        self.fx[1] = int(self.image.Asize[1]/self.sheet.cellsize[1])-1
                    else:
                        self.fx[0] = int(self.image.Asize[0] / self.sheet.cellsize[0]) - 1
                        self.fx[1] = int(self.image.Asize[1] / self.sheet.cellsize[1])
                    self.image.object = pygame.transform.scale(self.image.object, sd)
                    self.sheet_e = True
                else:
                    self.image = [None] * len(imagef)
                    i = 0
                    for x in imagef:
                        self.image[i] = image(str(x), size, position)
                        if rotation > 0:
                            self.image[i].object = pygame.transform.rotozoom(self.image[i].object,rotation,1)
                        i += 1
                self.pivot = pivot
                self.rotation = rotation * 2
                self.rotationND = rotation
                self.position = position
                self.rect = size
                self.size = 1
                self.new = self.image
                self.refresh = True
                self.layer = layer
                self.frame = 0
                self.step = 0
                self.step_m = 1
                self.pingpong = False
                #return self
            def init_rotation(self):
                """sprite_object.init_rotation() -> Sprite Object
                Initializes only the rotation of the sprite
                """
                i = 0
                if not self.sheet_e:
                    for x in self.image:
                        sprite_r = x
                        sprite_r.object = pygame.Surface(x.object.get_size(),pygame.SRCALPHA)
                        if self.rotation != 0:
                            sprite_r.object = pygame.transform.rotozoom(x.object,self.rotation,self.size)
                        else:
                            sprite_r.object = x.object
                        sprite_r.rect = sprite_r.object.get_rect(center = x.rect.center)
                        self.new[i] = sprite_r
                        i += 1
                return self.new
            def init_position(self):
                """sprite_object.init_position() -> Sprite Object
                Initializes only the position of the sprite
                """
                i = 0
                if self.sheet_e:
                    sprite_r = self.image
                    if self.pivot == "topleft":
                        sprite_r.rect = sprite_r.object.get_rect(topleft=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                        #
                    elif self.pivot == "topright":
                        sprite_r.rect = sprite_r.object.get_rect(topright=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                        #
                    elif self.pivot == "top":
                        sprite_r.rect = sprite_r.object.get_rect(top=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                        #
                    elif self.pivot == "bottomleft":
                        sprite_r.rect = sprite_r.object.get_rect(bottomleft=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                        #
                    elif self.pivot == "bottomright":
                        sprite_r.rect = sprite_r.object.get_rect(bottomleft=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                        #
                    elif self.pivot == "bottom":
                        sprite_r.rect = sprite_r.object.get_rect(bottom=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                        #
                    elif self.pivot == "left":
                        sprite_r.rect = sprite_r.object.get_rect(left=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                        #
                    elif self.pivot == "right":
                        sprite_r.rect = sprite_r.object.get_rect(right=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                        #
                    elif self.pivot == "center":
                        sprite_r.rect = sprite_r.object.get_rect(center=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                        #
                else:
                    for x in self.image:
                        sprite_r = x
                        if self.pivot == "topleft":
                            sprite_r.rect = sprite_r.object.get_rect(topleft=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                            #
                        elif self.pivot == "topright":
                            sprite_r.rect = sprite_r.object.get_rect(topright=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                            #
                        elif self.pivot == "top":
                            sprite_r.rect = sprite_r.object.get_rect(top=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                            #
                        elif self.pivot == "bottomleft":
                            sprite_r.rect = sprite_r.object.get_rect(bottomleft=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                            #
                        elif self.pivot == "bottomright":
                            sprite_r.rect = sprite_r.object.get_rect(bottomleft=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                            #
                        elif self.pivot == "bottom":
                            sprite_r.rect = sprite_r.object.get_rect(bottom=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                            #
                        elif self.pivot == "left":
                            sprite_r.rect = sprite_r.object.get_rect(left=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                            #
                        elif self.pivot == "right":
                            sprite_r.rect = sprite_r.object.get_rect(right=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                            #
                        elif self.pivot == "center":
                            sprite_r.rect = sprite_r.object.get_rect(center=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                            #
                        self.new[i] = sprite_r
                        i += 1
                return self.new
            def init(self):
                """sprite_object.init() -> Sprite Object
                Initializes the entire sprite
                """
                self.rotation = self.rotationND * 2
                if self.sheet_e:
                    sprite_r = self.image
                    if self.rotation != 0:
                        #sprite_r.object = pygame.transform.rotate(self.image, self.rotation)
                        pass
                    else:
                        if self.pivot == "topleft":
                            sprite_r.rect = sprite_r.object.get_rect(topleft = ( list(self.position)[0] + Layer[self.layer][1][0], list(self.position)[1] + Layer[self.layer][1][1]))
                        elif self.pivot == "topright":
                            sprite_r.rect = sprite_r.object.get_rect(topright = ( list(self.position)[0] + Layer[self.layer][1][0], list(self.position)[1] + Layer[self.layer][1][1]))
                        elif self.pivot == "top":
                            sprite_r.rect = sprite_r.object.get_rect(top = ( list(self.position)[0] + Layer[self.layer][1][0], list(self.position)[1] + Layer[self.layer][1][1]))
                        elif self.pivot == "bottomleft":
                            sprite_r.rect = sprite_r.object.get_rect(bottomleft = ( list(self.position)[0] + Layer[self.layer][1][0], list(self.position)[1] + Layer[self.layer][1][1]))
                        elif self.pivot == "bottomright":
                            sprite_r.rect = sprite_r.object.get_rect(bottomleft = ( list(self.position)[0] + Layer[self.layer][1][0], list(self.position)[1] + Layer[self.layer][1][1]))
                        elif self.pivot == "bottom":
                            sprite_r.rect = sprite_r.object.get_rect(bottom = ( list(self.position)[0] + Layer[self.layer][1][0], list(self.position)[1] + Layer[self.layer][1][1]))
                        elif self.pivot == "left":
                            sprite_r.rect = sprite_r.object.get_rect(left = ( list(self.position)[0] + Layer[self.layer][1][0], list(self.position)[1] + Layer[self.layer][1][1]))
                        elif self.pivot == "right":
                            sprite_r.rect = sprite_r.object.get_rect(right = ( list(self.position)[0] + Layer[self.layer][1][0], list(self.position)[1] + Layer[self.layer][1][1]))
                        elif self.pivot == "center":
                            sprite_r.rect = sprite_r.object.get_rect(center = ( list(self.position)[0] + Layer[self.layer][1][0], list(self.position)[1] + Layer[self.layer][1][1]))

                    self.new = sprite_r
                else:
                    i = 0
                    for x in self.image:
                        sprite_r = x
                        #sprite_r[0] = pygame.Surface(self.image[0].get_size(),pygame.SRCALPHA)
                        if self.rotation != 0 or True:
                            sprite_r.object = pygame.transform.rotozoom(self.image[i].object,self.rotation,self.size)
                        else:
                            sprite_r.object = x.object
                        if self.pivot == "topleft":
                            sprite_r.rect = sprite_r.object.get_rect(topleft=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                        elif self.pivot == "topright":
                            sprite_r.rect = sprite_r.object.get_rect(topright=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                        elif self.pivot == "top":
                            sprite_r.rect = sprite_r.object.get_rect(top=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                        elif self.pivot == "bottomleft":
                            sprite_r.rect = sprite_r.object.get_rect(bottomleft=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                        elif self.pivot == "bottomright":
                            sprite_r.rect = sprite_r.object.get_rect(bottomleft=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                        elif self.pivot == "bottom":
                            sprite_r.rect = sprite_r.object.get_rect(bottom=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                        elif self.pivot == "left":
                            sprite_r.rect = sprite_r.object.get_rect(left=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                        elif self.pivot == "right":
                            sprite_r.rect = sprite_r.object.get_rect(right=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                        elif self.pivot == "center":
                            sprite_r.rect = sprite_r.object.get_rect(center=(list(self.position)[0] + Layer[self.layer][1][0],list(self.position)[1] + Layer[self.layer][1][1]))
                        self.new[i] = sprite_r
                        i += 1
                return self.new
            def display(self):
                """sprite_object.display() -> None
                displays the sprite object on the screen
                """
                if Layer[self.layer][0]:
                    if int(self.frame) >= self.frames:
                        if self.pingpong:
                            self.step_m *= -1
                        else:
                            self.frame = 1
                    if int(self.frame) < 2 and self.pingpong and "-" in str(self.step_m):
                        self.step_m *= -1
                    if self.step > 0:
                        self.frame += self.step * self.step_m
                    else:
                        self.frame = 1
                    if self.sheet_e:
                        x = 0
                        y = 0
                        if self.sheet.type == 1:
                            for i in range(int(self.frame-1)):
                                x += 1
                                if x > self.fx[0]-1:
                                    x = 0
                                    y += 1
                            x *= self.rect[0]
                            y *= self.rect[1]
                            area = (x+self.sheet.offset[0], y+self.sheet.offset[1], self.rect[0], self.rect[1])
                        else:
                            for i in range(int(self.frame-1)):
                                y += 1
                                if y > self.fx[1]-1:
                                    y = 0
                                    x += 1
                            x *= self.rect[0]
                            y *= self.rect[1]
                            area = (x+self.sheet.offset[0], y+self.sheet.offset[1], self.rect[0], self.rect[1])
                        display_a.blit(self.new.object, self.new.rect, area=area)
                    else:
                        display_a.blit(self.new[int(self.frame) - 1].object, self.new[int(self.frame) - 1].rect)


class E_intro:
    def intro(anim,back,t):
        """intro(sleep, color_background, color_text) -> None
        Plays the "PGE" sequence
        """
        global display_size
        fvv = Settings.UPDATE_AUTO
        Settings.UPDATE_AUTO = True
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
            Settings.UPDATE_AUTO = fvv
        else:
            print('======================================')
            print('resolution too small to display intro!')
            print('Try again with at least (300,150)')
            print('=================================')
    def run(tA=100,tB=100,tC=1000):
        """run(sleep_first, delay, finish_delay) -> None
        Plays the full original "PGE" animation
        """
        E_intro.intro(tA,color.white,color.red) # Plays first intro
        time.sleep(tB)
        Settings.UPDATE_AUTO = False # Disables auto update
        E_intro.intro(0,color.black,(0,100,255)) # Plays second intro
        display.update() # updates
        time.sleep(tC)
        Settings.UPDATE_AUTO = True # Enables auto update


class sound:
    def load(file):
        """load(file) -> Sound Object
        Loads a sound file and returns the object
        """
        return pygame.mixer.Sound(file)
    def play(soundOBJ):
        """play(sound_object) -> None
        Plays a sound object
        """
        soundOBJ.play()


class music:
    volume = 100
    def load(file):
        """load(file) -> None
        Loads a track to the buffer
        """
        pygame.mixer.music.load(file)
        
    def play(i=1):
        """play(times) -> None
        Plays the buffer for an amount of times, 0 is infinity
        """
        pygame.mixer.music.play(i-1)
        
    def unload():
        """unload() -> None
        Removes the track from buffer
        """
        pygame.mixer.music.unload()
        
    def restart():
        """restart() -> None
        Rewinds to the start of the track
        """
        pygame.mixer.music.pause()
        pygame.mixer.music.rewind()
        pygame.mixer.music.play(0)

    def stop():
        """stop() -> None
        Stops the buffer playback
        """
        pygame.mixer.music.stop()
        
    def pause():
        """pause() -> None
        Pauses the buffer playback
        """
        pygame.mixer.music.pause()
        
    def unpause():
        """unpause() -> None
        Un-Pauses the buffer playback
        """
        pygame.mixer.music.unpause()
        
    def fade(time):
        """fade(time) -> None
        Fades the playback for a given time and stops
        """
        pygame.mixer.music.fadeout(time)
    
    def set_v(new_v):
        """set_v(new) -> None
        Sets a new playback volume
        """
        pygame.mixer.music.set_volume(new_v)
        music.volume = new_v

    def get_v():
        """get_v() -> Float
        Gets the current playback volume
        """
        music.volume = pygame.mixer.music.get_volume()
        return music.volume

    def set_t(new_t):
        """set_v(new) -> None
        Changes the playback's position
        """
        pygame.mixer.music.set_pos(new_t)

    def get_t():
        """get_t() -> Float
        Get's the current playback position
        """
        return pygame.mixer.music.get_pos()
