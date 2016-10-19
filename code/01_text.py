#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Demo for presenting text stimuli with Psychopy
Psychopy Tutorial by Monica Li, 10-18-2016
"""

# load Psychopy modules for visual stimuli and clock
from psychopy import visual, core

# set up the window where the stimuli will be present on
win = visual.Window(size = [800,500],
                    color = "white",
                    fullscr = False,
                    units = "pix")

# set up the text stimulus you want to present
hello_txt = visual.TextStim(win, text = "Hello World!",
                        pos = [0,0],
                        color = "black",
                        height = 50,
                        font = "Arial")

# "draw" the stimulus to "the back of" the window
hello_txt.draw()

# present the stimulus
win.flip()

# the stimulus will be presented for 5 seconds
core.wait(5)

### close everything
win.close()
core.quit()
