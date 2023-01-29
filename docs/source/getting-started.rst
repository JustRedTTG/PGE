Getting Started
===============

Let's get started and learn how to use the tools of simplicity and make quick and cool games / applications.

Simple Loop
-----------

Let's get started by making a simple game loop, this loop will run our game code, on every frame, let's see how you'd make that in Pygame Extra.

.. code-block:: python

    import pygameextra as pe
    pe.init() # Do not forget to do this!
    pe.display.make((500, 500), 'My Game')
    while True:
        for pe.event.c in pe.event.get():
            pe.event.quitCheckAuto()
        print("Game Code")

Running this will make a 500 x 500 display called "My Game" and close once the "X" (close) is clicked.

.. image:: _static/docs01.png
    :align: center

As you can see we still have nothing on screen, but we can see the message "Game Code" shows up every frame!

Filling the background
----------------------

After making our basic game loop, let's fill the background with white on every frame!
For that we simply use the method: 

.. code-block:: python

  pygameextra.fill.full(color)

Here we have two options we can either manually set the color or use "``pygameextra.colors``".

.. code-block:: python

    import pygameextra as pe
    pe.init()
    pe.display.make((500, 500), 'My Game')
    while True:
        for pe.event.c in pe.event.get():
            pe.event.quitCheckAuto()
        pe.fill.full(pe.colors.white)
        pe.display.update()
    
.. image:: _static/docs02.png
    :align: left
    
As you can see white is filling the entire screen. This is the basic things you need to know when starting to use Pygame Extra.
Note: you have to update the display for all your rendering to show up on the screen!

Maximum Frames Per Second
-------------------------

When making a game / program it's important to have a stable frame-rate, we can set the max frames per second while updating the display:

.. code-block:: python
    
    pe.display.update(max_fps)
    
This will limit the game / program to a maximum frame-rate, we can't tell the game what the minimum frame-rate has to be, that depends on the user's machine.
