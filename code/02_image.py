#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Demo for presenting image stimuli with Psychopy
Psychopy Tutorial by Monica Li, 10-18-2016
"""

# set up current folder path
parent_dir = "/Users/mli/Desktop/psychopy-tutorial/"

# load Psychopy modules for visual stimuli and clock
from psychopy import visual, core

# set up the window where the stimuli will be present on
win = visual.Window(size = [800,500],
                    color = "white",
                    fullscr = False,
                    units = "pix")

# set up the image stimulus you want to present
happy_img = visual.ImageStim(win, pos = [0,0],
                    size = [500,500],
                    image = parent_dir + "stim/happy.jpg")

# "draw" the stimulus to "the back of" the window
happy_img.draw()

# present the stimulus
win.flip()

# the stimulus will be presented for 5 seconds
core.wait(5)

### close everything
win.close()
core.quit()
