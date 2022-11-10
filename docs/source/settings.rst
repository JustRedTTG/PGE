Settings
========

Pygame Extra has some settings up it's sleeve, let's take a closer look at all the different settings and what they affect.

Changing Settings
-----------------

It's very easy to change settings, you simply use the following:

.. code-block:: python

    pe.Settings.setting = newValue
That is pretty much it!

update_auto
-----------
Default value: False

This settings controls whether things like buttons and sliders, even text, automatically update the screen when they are done drawing.
It is not Recommended

update_onButton
---------------
Default value: False

This setting is pretty understandable, if True it updates the screen on button press

button_delay
------------
Default value: 100 (ms)

This setting is a variable buttons use to delay some time after a click, this prevents one click being register like more than one, this setting does not matter if the button_lock settings are set to True

button_lock
-----------
This setting class has two separate settings

* rect
* image

Both default at value: True

These settings are used by buttons to know if the button should lock up after a click aka wait for release
