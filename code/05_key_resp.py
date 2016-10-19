#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Demo for presenting text stimuli and receiving keyboard responses with Psychopy
Psychopy Tutorial by Monica Li, 10-18-2016
"""

# load Psychopy modules for visual stimuli, clock, and keypresses & mouse clicks
from psychopy import visual, core, event

# set up the window where the stimuli will be present on
win = visual.Window(size = [800,500],
                    color = "white",
                    fullscr = False,
                    units = "pix")

# set up the text stimuli you want to present
hello_txt = visual.TextStim(win, text = "Hello World!",
                        pos = [0,0],
                        color = "black",
                        height = 50,
                        font = "Arial")
space_txt = visual.TextStim(win, text = "Please press space or ESC to proceed.",
                        pos = [0,-200],
                        color = "black",
                        height = 20,
                        font = "Arial")
                        
# "draw" the stimuli to "the back of" the window
hello_txt.draw()
space_txt.draw()

# present the stimulus
win.flip()

# present the stimulus up to 5 seconds, screen goes blank if keypress received
# but won't proceed until the allocated time period is used up
t0 = core.getTime()
while core.getTime()-t0 <= 5:
    resp_key = event.getKeys(keyList=["space","escape"])
    if resp_key != []:
        win.flip()
        
# # present the stimulus infinitely until a keypress is received
# resp_key = event.waitKeys()
# win.flip()

### close everything
win.close()
core.quit()
