Drawing
=======

Pygame Extra has simple drawing functions, most are simply redirecting to pygame itself and don't really change in complexity

Line
----
.. image:: _static/docs13.png
    :align: right

Let's look at the syntax of drawing a line

.. code-block:: python

    pe.draw.line(color, pos, w, update=True, layer=0)
Now let's take a closer look at the syntax

* color - the line color
* pos - the position of the line aka ``(StartX,StartY,EndX,EndY)``
* w - the line width
* update(optional) - setting this to false will disable the automatic screen update
* layer - the layer on witch to put the line

Rect
----
.. image:: _static/docs14.png
    :align: right

Let's look at the syntax of drawing a rect aka a rectangle

.. code-block:: python

    pe.draw.rect(color, rect, w, update=True, layer=0)
Now let's take a closer look at the syntax

* color - the rect / rect line color
* rect - the rect itself aka ``(StartX,StartY,SizeX,SizeY)``
* w (no fill) - setting this to be larger than 0 will make a line rect without fill
* w (with fill) - setting this to 0 will make the rect filled
* update(optional) - setting this to false will disable the automatic screen update
* layer - the layer on witch to put the rect

Circle
------
.. image:: _static/docs15.png
    :align: right

Let's look at the syntax of drawing a circle

.. code-block:: python

    pe.draw.circle(color, pos, size, w, update=True, layer=0)
Now let's take a closer look at the syntax

* color - the circle color
* pos - the center position of the circle
* size - the size / radius of the circle
* w (no fill) - setting this to be larger than 0 will make a line circle
* w (with fill) - setting this to 0 will make a filled circle
* update(optional) - setting this to false will disable the automatic screen update
* layer - the layer on witch to put the circle

Ellipse
-------
.. image:: _static/docs18.png
    :align: right

Let's look at the syntax of drawing a ellipse

.. code-block:: python

    pe.draw.ellipse(color, rect, update=True, layer=0)
Now let's take a closer look at the syntax

* color - the ellipse color
* rect - the rect of the ellipse
* update(optional) - setting this to false will disable the automatic screen update
* layer - the layer on witch to put the ellipse