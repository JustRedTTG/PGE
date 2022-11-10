Layers
======

Don't think of layer as a mean of layering objects, think of them as maps, you can Enable and Disable layers and set their offset, let's see how that's done!

**Note**: there's only 16 layers available to use in Pygame Extra

**Note**: the default layer is 0, and it's recommended to keep it Enabled

Toggling layers
---------------

It's very easy to toggle layers, to do so:

.. code-block:: python

    pe.layers[0-16][0] = bool

If you disable a layer all drawing functions that target that layer will be stopped!

Here are all the PGE functions that use layers:

.. code-block:: python

    pe.fill.full(layer=0)
    pe.draw.line(layer=0)
    pe.draw.rect(layer=0)
    pe.draw.circle(layer=0)
    pe.draw.ellipse(layer=0)
    pe.Sprite(layer=0)
    pe.text.make(layer=0)
    pe.image.display(layer=0)
    pe.button.rect(layer=0)
    pe.button.image(layer=0)
    pe.slider.normal(layer=0)
    pe.slider.boxed(layer=0)