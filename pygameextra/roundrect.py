import pygameextra as pe
def rect(color,rect,g=6):
    ok = False
    back,sur,blitrect,alpha=None,None,None,None
    if len(color)>3:
        blitrect=(rect[0],rect[1])
        back=pe.display_a
        sur=pe.pygame.Surface((rect[2],rect[3]),pe.pygame.SRCALPHA)
        pe.display_a=sur
        rect=(0,0,rect[2],rect[3])
        alpha=color[3]
        color=(color[0],color[1],color[2])
        ok=True

    s=min(rect[2]/g,rect[3]/g)
    #corners
    pe.draw.ellipse(color,(rect[0],rect[1],s,s))
    pe.draw.ellipse(color,(rect[0]+rect[2]-s,rect[1],s,s))
    pe.draw.ellipse(color,(rect[0],rect[1]+rect[3]-s,s,s))
    pe.draw.ellipse(color,(rect[0]+rect[2]-s,rect[1]+rect[3]-s,s,s))
    #fill
    pe.draw.rect(color,(rect[0]+s/2,rect[1],rect[2]-s,rect[3]-s),0)
    pe.draw.rect(color,(rect[0]+s/2,rect[1]+s,rect[2]-s,rect[3]-s),0)
    #fill
    pe.draw.rect(color,(rect[0],rect[1]+s/2,rect[2]-s,rect[3]-s),0)
    pe.draw.rect(color,(rect[0]+s,rect[1]+s/2,rect[2]-s,rect[3]-s),0)
    if ok:
        pe.display_a=back
        sur.set_alpha(alpha)
        pe.display.blit.rect(sur,blitrect)