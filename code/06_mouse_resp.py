#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Demo for presenting image stimuli and receiving mouse click responses with Psychopy
Psychopy Tutorial by Monica Li, 10-18-2016
"""

# set up current folder path
parent_dir = "/Users/mli/Desktop/psychopy-tutorial/"

# load Psychopy modules for visual stimuli, clock, and keypresses & mouse clicks
from psychopy import visual, core, event

# set up the window where the stimuli will be present on
win = visual.Window(size = [800,500],
                    color = "white",
                    fullscr = False,
                    units = "pix")

mouse = event.Mouse(visible = True, win = win)

# set up the image stimuli you want to present
happy_img = visual.ImageStim(win, pos = [200,0],
                    size = [200,200],
                    image = parent_dir + "stim/happy.jpg")
sad_img = visual.ImageStim(win, pos = [-200,0],
                    size = [200,200],
                    image = parent_dir + "stim/sad.jpg")


# set mouse position to the center of the screen
mouse.setPos(newPos=[0,0])

# present the stimulus up to 10 seconds, screen goes blank if mouse click is received
# trial ends as soon as mouse click is received
t0 = core.getTime()
while core.getTime()-t0 <= 10:
    happy_img.draw(); sad_img.draw(); win.flip() # keep updating the images
    
    mouse_pos = mouse.getPos() # keep getting the mouse position
    
    # change opacity of the images when the mouse hovers over
    if happy_img.contains(mouse_pos):
        happy_img.setOpacity(0.7)
    else:
        happy_img.setOpacity(1.0)
        
    if sad_img.contains(mouse_pos):
        sad_img.setOpacity(0.7)
    else:
        sad_img.setOpacity(1.0)
    
    # trial ends when one of the images is clicked on
    if mouse.isPressedIn(happy_img) or mouse.isPressedIn(sad_img):
        win.flip()
        break

# close everything
win.close()
core.quit()
