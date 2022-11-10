Mouse events
============

Pygame Extra has a class just for mouse operations!

Let's take a look at what this class offers.

Position
--------

Using mouse.pos() we can get the position of the mouse, in tuple!

Syntax:

.. code-block:: python

    (mouseX,mouseY)

Clicked?
--------

Using mouse.clicked() we can check if the mouse is clicked, now since there's 3 mouse buttons, running this will return a bool list

Say we have our left mouse button pressed

.. code-block:: python

    [True, False, False]

Now, say we have our right mouse button pressed

.. code-block:: python

    [False, False, True]

Basically the syntax here is:

.. code-block:: python

    pe.mouse.clicked()

.. code-block:: python

    [Left, Middle, Right]
