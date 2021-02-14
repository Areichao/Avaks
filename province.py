from Avaks import *
# by printing this function, it opens up the map for to each

def showScreen(active):
    """ Displays the current screen """
    screen.blit(active,(0, 0))

def instructions():
    global currentScreen
    showScreen(Instructions)
    currentScreen = 'Instructions'

def map():
    global currentScreen
    showScreen(mapscreen)
    currentScreen = 'Map'

def title():
    global currentScreen
    showScreen(Title)
    currentScreen = 'Title'

def Alberta():
    """ Sets object Alberta, and shows screen """
    global currentScreen
    showScreen(AlbertaProv)
    currentScreen = 'Alberta'
