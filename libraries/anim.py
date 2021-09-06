# Setup
import pygameextra as pe
factor = 1

class animation:
    def __init__(self, start: tuple, end: tuple, speed: float = 1):
        self.canvas = None
        self.speed = speed
        self.start = start
        self.end = end
        self.position = start
        self.finish = False
        self.progress = 0


class canvas:
    def __init__(self):
        self.objects = []
        self.speed = 1
        self.enable = True

    def add(self, anim: animation):
        anim.canvas = self
        self.objects.append(anim)

def animate(group: canvas):
    i = 0
    if not group.enable:
        return
    while i < len(group.objects):
        if not group.objects[i].finish:
            # Gather speed
            speed = group.objects[i].speed * group.speed * factor

            # Move Object
            group.objects[i].position = pe.math.lerp(group.objects[i].position,group.objects[i].end, speed)
            group.objects[i].position = (group.objects[i].position[0], group.objects[i].position[1])

            # Calculate progress
            end = pe.math.dist(group.objects[i].start, group.objects[i].end)
            current = pe.math.dist(group.objects[i].start, group.objects[i].position)
            try:
                group.objects[i].progress = (current / end) * 100
            except:
                group.objects[i].progress = 100
            group.objects[i].progress = int(group.objects[i].progress)

            # Check if goal reached
            if group.objects[i].position == group.objects[i].end or group.objects[i].progress >= 100:
                group.objects[i].finish = True

        i += 1
