# Getting Started

Let's get started with Pygame Extra!

> This is the beginner-friendly legacy documentation for Pygame Extra.
>
> Skip ahead to <a href="Contexts.md">Contexts</a>

## Installation
{default-state="collapsed" collapsible="true"}

To install Pygame Extra, you can use pip:

```bash
pip install pygameextra
```

Current supported python version is **3.11**, but it should work with any version supported by pygame.

## Initialization

> pe is the common alias for Pygame Extra and is used throughout the documentation.

To start using Pygame Extra, you need to initialize it:
```python
import pygameextra as pe
pe.init()
```

### Creating a display

Pygame Extra simplifies making a window or display.
```python
pe.display.make((500, 500), "My Window")
```

### Running the game loop

Pygame Extra simplifies the game loop.

By using the legacy pygame loop you need to handle events yourself,
this can be done using `pe.event`, you'll want to typically use `pe.event.quitCheckAuto()` to handle the quit event. or `pe.event.quitCheck()` and `pe.pQuit()` if you want to handle the quit event yourself.

```python
import pygameextra as pe
pe.init()

pe.display.make((500, 500), "My Window")

while True:
    for pe.event.c in pe.event.get():
        pe.event.quitCheckAuto()
    pe.display.update()
```

You can use `pe.fill.full(color)` to refresh the screen with a color.
Likewise, you can use the pygame extended `pe.colors` module to get colors.

```python
pe.fill.full(pe.colors.white)
```

## Simple shapes

Pygame Extra proxies pygame draw functions automatically for you!
With some additions, you can use transparency in your color freely!

### Rect 

The rect only requires a color and the rect itself, notice that the width is left as 0 if not set,
which means the shape will be filled.

<img src="pe.draw.rect(1).png" width="50" height="50" style="inline"/>

```python
pe.draw.rect((*pe.colors.red, 150), (0, 0, 100, 100), w=5)
```
<img src="pe.draw.rect(2).png" width="50" height="50" style="inline"/>

```python
pe.draw.rect((*pe.colors.red, 150), (0, 0, 100, 100))
```

You can also make any of the 4 edges round

> Using the edge_rounding parameter will make all edges the same rounding value
> You can also change the roundness of each edge individually
> ```python
> edge_rounding: int = -1
> edge_rounding_topright: int = -1
> edge_rounding_topleft: int = -1
> edge_rounding_bottomright: int = -1
> edge_rounding_bottomleft: int = -1
> ```
> Leaving the value to -1 which is the default will make the edge not rounded
> Notice that if you pass edge_rounding it will override the individual edge roundings
> if they have -1 set as their value, this can be avoided by setting it to 0


<img src="pe.draw.rect(3).png" width="50" height="50" style="inline"/>

```python
pe.draw.rect((*pe.colors.red, 150), (0, 0, 100, 100), w=5, edge_rounding=15)
```
<img src="pe.draw.rect(4).png" width="50" height="50" style="inline"/>

```python
pe.draw.rect((*pe.colors.red, 150), (0, 0, 100, 100), edge_rounding=15)
```

### Circle

Notice that while the circle takes in a width like the rect,
it has an additional required parameter, radius.

<img src="pe.draw.circle(1).png" width="50" height="50" style="inline"/>

```python
pe.draw.circle((*pe.colors.red, 150), (100, 100), radius=50, w=5)
```

<img src="pe.draw.circle(2).png" width="50" height="50" style="inline"/>

```python
pe.draw.circle((*pe.colors.red, 150), (100, 100), radius=50)
```