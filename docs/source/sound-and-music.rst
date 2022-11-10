Sound
=====

Let's get started with Pygame Extra's sound class.

Loading
-------

To load a sound from file we simple use:

.. code-block:: python

    pe.sound.load(file)

Let's say we have a "boom.mp3" file in our script folder, to load it we simply do:

.. code-block:: python

    boom = pe.sound.load("boom.mp3")
    
Now when we need to play the sound we just provide the "boom" variable

Playing
-------

To play a sound we simply use:

.. code-block:: python

    pe.sound.play(soundOBJ)
    
Let's play our "boom" sound:

.. code-block:: python

    pe.sound.play(boom)
    
There we go!

Music
=====

Let's get started with Pygame Extra's music class.

Loading
-------

To load a music file we simple use:

.. code-block:: python

    pe.music.load(file)

Let's say we have a "boss.mp3" file in our script folder, to load it we simply do:

.. code-block:: python

    pe.music.load("boss.mp3")
    
Now let's play the music!

Playing
-------

To play the music we simply use:

.. code-block:: python

    pe.music.play(amount)
    
Say we want to play it once:

.. code-block:: python

    pe.music.play(1)
    
How about if we want to play it infinitely?

No problem!

.. code-block:: python

    pe.music.play(0)

If we do this, we'll have to pause or stop it!

Pause / Unpause
---------------

To pause the currently playing music we simply do:

.. code-block:: python

    pe.music.pause()
    
To unpause the currently playing music we simply do:

.. code-block:: python

    pe.music.unpause()

How about if we want to stop the music?

Stopping and Fading
--------------------

To stop the music we simply do:

.. code-block:: python

    pe.music.stop()
    
If we want the music to stop with a added fade we use:

.. code-block:: python

    pe.music.fade(time)
    
Say we want to fade and stop the music after 3 seconds, we do:

.. code-block:: python

    pe.music.fade(3000)

The fade function is in milliseconds, so for 3 seconds we use "3000".

Volume
------

It's important to control the volume of the music, let's see how.

Getting
+++++++

There are 2 ways to get the volume

The more accurate way is by using:

.. code-block:: python

    pe.music.get_v()
    
This will return the volume of the mixer.

The more inaccurate way is to directly use the volume variable:

.. code-block:: python

    pe.music.volume()

Setting
+++++++

Now to set the volume:

.. code-block:: python

    pe.music.set_v(new_volume)
    
This is basically it!

Position
--------

The position of the music track might be necessary in some cases, for example in music players

Getting
+++++++

To get the position of the music is at we simply do:

.. code-block:: python

    pe.music.get_t()
    
This will get the current position of the music track.

Setting
+++++++

To set the position of the music track we simply do:

.. code-block:: python

    pe.music.set_t(new_time)
    
This is basically it!