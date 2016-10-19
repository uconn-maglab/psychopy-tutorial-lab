#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Demo for presenting video stimuli with Psychopy
Psychopy Tutorial by Monica Li, 10-18-2016
"""

# set up current folder path
parent_dir = "/Users/mli/Desktop/psychopy-tutorial/"

# load Psychopy modules for visual stimuli, audio stimuli and clock
from psychopy import visual, core, sound

# set up the window where the stimuli will be present on
win = visual.Window(size = [800,500],
                    color = "black",
                    fullscr = False,
                    units = "pix")

# set up the video stimulus
mov = visual.MovieStim3(win, parent_dir + 'stim/baby_laugh.mp4',
                        size = (320, 240),
                        flipVert = False,
                        flipHoriz = False,
                        loop = False)

# play the video clip for 10 seconds, starting at 20 seconds
t0 = core.getTime()
mov.seek(20) # start play at 20 seconds
while core.getTime()-t0 <= 10:
    mov.draw()
    win.flip()

# # play the entire video clip
# while mov.status != visual.FINISHED:
#     mov.draw()
#     win.flip()

### close everything
win.close()
core.quit()
