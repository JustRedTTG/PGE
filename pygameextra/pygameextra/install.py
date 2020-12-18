"""Pygame Extra's installer"""
import requests
import pygame, pygame.display
from os import system, path, mkdir
address = "https://redstonehair.000webhostapp.com/pygame%20extra/1.6.5.2/files/"
scriptpathf = str(path.realpath(__file__)).replace("install.py",'')
def download(link):
    global scriptpathf
    """download(link) -> None
    A function used by the installer to download and save content
    """
    c = requests.get(address+link,timeout=5)
    open(str(path.realpath(__file__)).replace("install.py",'')+link, "wb").write(c.content)
    
def install(scriptpath, progress=0, __version__="1.6.5.2"):
    """install(progress, scriptpath, version) -> None
    Installs Pygame Extra's additional resources
    """
    dis = pygame.display.set_mode((500,100))
    pygame.display.set_caption("Pygame Extra Installation")
    install = True
    try:
        import requests
    except:
        print("[ IMPORT ERROR ]"+
        " Please get the 'requests' library and try to run the installation again!")
        print("Quiting Instalation of " + __version__)
        pygame.quit()
        exit()
    if not path.exists(path.realpath(path.join(scriptpath, "files"))):
        mkdir(path.realpath(path.join(scriptpath, "files")))
    if not path.exists(path.realpath(path.join(scriptpath, "build"))):
        mkdir(path.realpath(path.join(scriptpath, "build")))
    if not path.exists(path.realpath(path.join(scriptpath, "build/scripts-3.8"))):
        mkdir(path.realpath(path.join(scriptpath, "build/scripts-3.8")))
    if not path.exists(path.realpath(path.join(scriptpath, "examples"))):
        mkdir(path.realpath(path.join(scriptpath, "examples")))
    if not path.exists(path.realpath(path.join(scriptpath, "examples/pong"))):
        mkdir(path.realpath(path.join(scriptpath, "examples/pong")))
    if not path.exists(path.realpath(path.join(scriptpath, "examples/tester"))):
        mkdir(path.realpath(path.join(scriptpath, "examples/tester")))
    if not path.exists(path.realpath(path.join(scriptpath, "dist"))):
        mkdir(path.realpath(path.join(scriptpath, "dist")))
    if not path.exists(path.realpath(path.join(scriptpath, "pygameextra_pong.egg-info"))):
        mkdir(path.realpath(path.join(scriptpath, "pygameextra_pong.egg-info")))
    if not path.exists(path.realpath(path.join(scriptpath, "pygameextra_tester.egg-info"))):
        mkdir(path.realpath(path.join(scriptpath, "pygameextra_tester.egg-info")))
    try:
        requests.get("http://www.google.com")
        internet = True
    except:
        internet = False
        #
    while install:
        for eventx in pygame.event.get():
            if eventx.type == pygame.QUIT:
                print("Quiting Instalation of "+__version__+", please complete the instalation in order to use PGE!")
                pygame.quit()
                exit()
        dis.fill((255,255,255))
        if internet:
            if progress < 10:
                download("/files/version.info")
                progress += 10
            elif progress < 20:
                download("dist/pygameextra_pong-0.0.0-py3.8.egg")
                progress += 10
            elif progress < 30:
                download("dist/pygameextra_tester-0.0.0-py3.8.egg")
                progress += 5
            elif progress < 35:
                download("examples/pong/pygameextra-pong")
                progress += 5
            elif progress < 40:
                download("examples/tester/pygameextra-tester")
                progress += 5
            elif progress < 45:
                download("examples/pong/font.ttf")
                progress += 1
            elif progress < 46:
                download("examples/tester/Xbutton.png")
                progress += 1
            elif progress < 47:
                download("examples/tester/Ybutton.png")
                progress += 1
            elif progress < 48:
                download("examples/tester/columns.png")
                progress += 1
            elif progress < 49:
                download("examples/tester/rows.png")
                progress += 1
            elif progress < 50:
                download("examples/tester/mario_01.png")
                progress += 1
            elif progress < 51:
                download("files/slider.png")
                progress += 1
            elif progress < 52:
                download("pygameextra_pong.egg-info/PKG-INFO")
                progress += 1
            elif progress < 53:
                download("pygameextra_pong.egg-info/SOURCES.txt")
                progress += 1
            elif progress < 54:
                download("pygameextra_pong.egg-info/dependency_links.txt")
                progress += 1
            elif progress < 55:
                download("pygameextra_pong.egg-info/top_level.txt")
                progress += 1
            elif progress < 56:
                download("pygameextra_tester.egg-info/PKG-INFO")
                progress += 1
            elif progress < 57:
                download("pygameextra_tester.egg-info/SOURCES.txt")
                progress += 1
            elif progress < 58:
                download("pygameextra_tester.egg-info/dependency_links.txt")
                progress += 1
            elif progress < 59:
                download("pygameextra_tester.egg-info/top_level.txt")
                progress += 1
            elif progress < 60:
                download("examples/pong/pygameextra-pong")
                progress += 1
            elif progress < 61:
                download("examples/tester/pygameextra-tester")
                progress += 1
            else:
                progress += 10
        else:
            progress = 100
        pygame.draw.rect(dis, (0,233,0), (0, 40, progress*5, 20) , 0)
        pygame.display.set_caption("Pygame Extra Installation - "+str(progress)+"%")

        pygame.display.flip()
        if progress >= 100:
            install = False
            open(scriptpath + "files/install.info", "w").write("installed")
        else:
            open(scriptpath + "files/install.info", "w").write("in " + str(progress))
        pygame.time.Clock().tick(160)
