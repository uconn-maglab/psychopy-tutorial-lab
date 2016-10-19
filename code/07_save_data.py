#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Demo for presenting text stimuli and receiving keyboard responses with Psychopy
Psychopy Tutorial by Monica Li, 10-18-2016
"""
### SETUP ###
# load Psychopy modules for visual stimuli, clock, and keypresses & mouse clicks
from psychopy import visual, core, event, sound
# load module for list randomization
import random
# load numpy for storing and saving data
import numpy as np
# set up current folder path
parent_dir = "/Users/mli/Desktop/psychopy-tutorial/"

### STIMULI ###
# set up the window where the stimuli will be present on
win = visual.Window(size = [800,500],
                    color = "white",
                    fullscr = False,
                    units = "pix")

# set up the image stimuli you want to present
happy_img = visual.ImageStim(win, pos = [0,0],
                    size = [200,200],
                    image = parent_dir + "stim/happy.jpg")
sad_img = visual.ImageStim(win, pos = [0,0],
                    size = [200,200],
                    image = parent_dir + "stim/sad.jpg")

# set up the audio stimulus you want to play
### use pyo for the audio library
### IMPORTANT: change the audio driver to "portaudio" in psychopy preferences/general
laugh_wav = sound.SoundPyo(parent_dir + "stim/baby_laugh.wav",
                            start = 0, stop = -1)
cry_wav = sound.SoundPyo(parent_dir + "stim/baby_cry.wav",
                            start = 0, stop = -1)

# set up the text stimuli you want to present for the response feedback
right_txt = visual.TextStim(win, text = "Correct",
                        pos = [0,0],
                        color = "black",
                        height = 50,
                        font = "Arial")
wrong_txt = visual.TextStim(win, text = "Incorrect",
                        pos = [0,0],
                        color = "red",
                        height = 50,
                        font = "Arial")
slow_txt = visual.TextStim(win, text = "Too Slow",
                        pos = [0,0],
                        color = "red",
                        height = 50,
                        font = "Arial")

### LISTS AND RANDOMIZATION ###
# put stimuli into dictionaries for easy reference
V_STIM = {"happy": happy_img, "sad": sad_img}
A_STIM = {"laugh": laugh_wav, "cry": cry_wav}
# trial lists with the condition of each trial and its corresponding stimuli
COND = ["congruent", "congruent", "incongruent", "incongruent"]
V_STIM_LIST = ["happy","sad","happy","sad"]
A_STIM_LIST = ["laugh","cry","cry","laugh"]
# create a randomized number list
list_order = range(4) # a list of numbers, [0,1,2,3]
random.shuffle(list_order) # randomize the list above

# header for data log
data = np.hstack(("COND", "V_STIM", "A_STIM", "KEY", "RESP", "ACC", "RT"))

### EXPERIMENTAL PRESENTATION ###
for index in list_order:
    # draw and present the visual stimulus of a given trial
    V_STIM[V_STIM_LIST[index]].draw(); win.flip()
    # play the audio stimulus of the same trial
    A_STIM[A_STIM_LIST[index]].play()
    # start timing
    t0 = core.getTime()
    # present the stimulus up to 5 seconds, screen goes blank if keypress received
    while core.getTime()-t0 <= 5:
        KEY = event.getKeys(keyList=["right","left"])
        if KEY != []:
            t1 = core.getTime()
            win.flip()
            break
    # map keypress to meaningful response type
    if KEY == []:
        KEY = "None"
        RESP = "None"
    elif KEY == ["right"]:
        RESP = "congruent"
    elif KEY == ["left"]:
        RESP = "incongruent"
    # determine the accuracy of the response, calculate reaction time, and give feedback
    if RESP == "None":
        ACC = 0; RT = 9999
        slow_txt.draw(); win.flip(); core.wait(1)
    elif RESP == COND[index]:
        ACC = 1; RT = t1-t0
        right_txt.draw(); win.flip(); core.wait(1)
    elif RESP != COND[index]:
        ACC = 0; RT = t1-t0
        wrong_txt.draw(); win.flip(); core.wait(1)
    # store data into the numpy array
    data = np.vstack((data, np.hstack((COND[index],
                                       V_STIM_LIST[index],
                                       A_STIM_LIST[index],
                                       KEY,
                                       RESP,
                                       ACC,
                                       "%.3f" %RT)))) # round the RT (in seconds) to the third decimal place

### SAVE DATA ###
np.savetxt(parent_dir + "data/MyData.txt",
            data, fmt='%s', delimiter='\t', newline='\n',
            header='', footer='', comments='# ')

# close everything
win.close()
core.quit()
