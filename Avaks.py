import pygame, sys
# from province import *
# from quiz import Question
import pygame.freetype

pygame.init()

# ***************************   Basic layout **********************************************
size = width, height = 1920, 1020
screen = pygame.display.set_mode(size)
black = 0, 0, 0
white = (255, 255, 255)
currentScreen = 'Title'
imagePath = "C:/Users/Anna/Pictures/Avaks/" 
GAME_FONT = pygame.freetype.Font(imagePath + 'Secret Winter.ttf', 70)
score = 0

# *************************** Coordinates ***************************************************
# province button coordinates 
provCoordinates = {'Alberta': (553, 616)} # add the rest later 

# province location coordinates 
subProvCoordinates = {'Banff National Park': (776,691)} # add the rest later 
# , 'Jasper National Park': (), 'Abraham Lake': ()

# title screen button locations (top left coordinates)
titleScreenButtons = {'Start': (798, 164), 'Instructions': (674, 414),'Exit':(803, 66)}

# coordinate location for quiz question and options 
questionCoordinates = {'Question':(112, 96),'score':(1734, 96)}


# *************************** Importing images *************************************************
# format -> image = pygame.image.load(imagePath + 'imagename.png')

Title = pygame.image.load(imagePath + 'Title.png')
Instructions = pygame.image.load(imagePath + 'Instructions.png')
mapscreen = pygame.image.load(imagePath + 'MapScreen.png')


# Provinces 
AlbertaProv = pygame.image.load(imagePath + 'Alberta.png')

# sublocations 
BanffNationalPark = pygame.image.load(imagePath + 'Banff National Park.png')
# JasperNationalPark = pygame.image.load(imagePath + 'JapserNationalPark.png')
# AbrahamLake = pygame.image.load(imagePath + 'Abraham Lake')

# Title buttons 
StartButton = pygame.image.load(imagePath + 'Start.png')
InstructionButton = pygame.image.load(imagePath + 'instructionsButton.png')
ExitButton = pygame.image.load(imagePath + 'Exit.png')

# ************************** screens ***********************************************************
screens = {'Map':1,'Alberta':3}

# **************************   screen name && icon  **********************************************
pygame.display.set_caption("Avaks")
# icon = pygame.image.load(imagePath + 'imageName.png')
# pygame.display.set_icon(icon)

# ***************************** class **************************************************************
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt,
        self.answer = answer

# **************************** summon screens **********************************************************
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

# *************************** selection Methods *******************************************************
        
def selectProv(pos):
    """ Determines which province was selected, then sets current screen to equal that province."""
    global currentScreen
    # format -> if (image import (scroll up to find it)).get_rect(topleft = (provCoordinates['Provincename'])).collidepoint(pos)
        # currentScreen = 'ProvinceName'
    if AlbertaProv.get_rect(topleft = (provCoordinates['Alberta'])).collidepoint(pos):
        currentScreen = 'Alberta'



def selectSubProvAlberta(pos):
    """ Determines which tourist attraction was selected, then changes it to that quiz page"""
    global currentScreen
    if BanffNationalPark.get_rect(topleft = (subProvCoordinates['Banff National Park'])).collidepoint(pos):
        currentScreen = 'Banff National Park'
    # elif JasperNationalPark.get_rect(topleft = (subProvCoordinates['Jasper National Park'])).collidepoint(pos):
    #     currentScreen = 'Jasper National Park'
    # elif AbrahamLake.get_rect(topleft = (subProvCoordinates['Abraham Lake'])).collidepoint(pos):
    #     currentScreen = 'Abraham Lake'


# ************************** Title screen Methods ******************************************

def startButton(pos):
    """Determines if the start button was clicked. if it was, start the map screen """
    global currentScreen
    if StartButton.get_rect(topleft = (titleScreenButtons['Start'])).collidepoint(pos):
        currentScreen = 'Map'

def instructionButton(pos):
    """Determines if the instruction button was clicked. if it was, take us to the instruction screen"""
    global currentScreen
    if InstructionButton.get_rect(topleft = (titleScreenButtons['Instructions'])).collidepoint(pos):
        currentScreen = 'Instructions'

def exitButton(pos):
    """Determines if the exit button was clicked. if so, exit the game"""
    global running 
    if ExitButton.get_rect(topleft = (titleScreenButtons['Exit'])).collidepoint(pos):
        running = False 

def titleButtons(pos):
    """Determine where player has clicked on the screen"""
    # check if mouse click was in start button
    startButton(pos)
    # check if mouse click was on instruction
    instructionButton(pos)
    # check if mouse click was in exit button
    exitButton(pos)
    


# ************************** Quiz running thing *************************************************
    
def run(questions):
    global score 
    for question in questions:
        for privateEvent in pygame.event.get():
            if privateEvent.type == pygame.KEYDOWN:
                if privateEvent.key == question.answer:
                    score += 1
    return score 


def runQuizOne(questions):
    """ Display questions for question 1"""
    if screen == 'Quiz':
        GAME_FONT.render_to(screen, (questionCoordinates['Question']), questionBanff[0], white)
        showScore(questions)
        for privateEvent in pygame.event.get():
            if privateEvent.type == pygame.KEYDOWN:
                runQuizTwo(questions)

def runQuizTwo(questions):
    """ Display questions for question 2"""
    if screen == 'Quiz':
        GAME_FONT.render_to(screen, (questionCoordinates['Question']), questionBanff[1], white)
        showScore(questions)
        for privateEvent in pygame.event.get():
            if privateEvent.type == pygame.KEYDOWN:
                runQuizThree(questions)
                
def runQuizThree(questions):
    """ Display questions for question 3"""
    if screen == 'Quiz':
        GAME_FONT.render_to(screen, (questionCoordinates['Question']), questionBanff[2], white)
        showScore(questions)
        for privateEvent in pygame.event.get():
            if privateEvent.type == pygame.KEYDOWN:
                runQuizFour(questions)

def runQuizFour(questions):
    """Display question for question 4"""
    global currentScreen 
    if screen == 'Quiz':
        GAME_FONT.render_to(screen, (questionCoordinates['Question']), questionBanff[3], white)
        showScore(questions)
        for privateEvent in pygame.event.get():
            if privateEvent.type == pygame.KEYDOWN:
                currentScreen = 'Map'
                # call the info paragraph 
                

def showScore(questions):
    """Display the score"""
    run(questions)
    GAME_FONT.render_to(screen, (questionCoordinates['score']), str(score), white)



# ************************** Quiz lists *************************************************
# all keys for quiz answers 
A = pygame.K_a
B = pygame.K_b
C = pygame.K_c
D = pygame.K_d

# Banff info 
questionBanff = [
        "What is the elevation of Banff in feet?\na)4,678 feet\nb)4,537 feet\nc)4,902 feet\nd)3,564 feet\n\n",
        "What year was Banff established in?\n(a)1885\n(b)1969\n(c)1869\n(d)1872\n\n",
        "What is Banff most known for?\n(a)Lakes \n(b)Scenery\n(c)Mountains\n(d)All of the above\n\n",
        "What are popular locations in Banff?\n(a) Lake louise \n(b)Sunshine Village Ski Resort \n(c)Icefields Parkway \n (d)all of the above\n\n"
         ]

questionsBanff =[
    Question(questionBanff[0], A),
    Question(questionBanff[1], C),
    Question(questionBanff[2], D),
    Question(questionBanff[3], A)
] 
    
# **************************  main running thing **************************************************
if __name__ == "__main__":
    running = True 
    while running:
        # allows us to use quit button 
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False 
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False 

        # If we are on the title screen, show the title screen and do nothing until player presses a button 
        if currentScreen == 'Title':
            title()                
            for event in pygame.event.get():                                            
                if event.type == pygame.MOUSEBUTTONDOWN:                                    
                    pos = pygame.mouse.get_pos()                                                   
                    titleButtons(pos)
                     
        # If we are on the Instructions screen, we can go back to the title by pressing TAB
        if currentScreen == 'Instructions':
            instructions()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_TAB:
                        currentScreen = 'Title'
        
        # If we are on the Map page, we do nothing until player either ESC or presses a province. 
        if currentScreen == 'Map':
            map()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    selectProv(pos)

        # If we are on the Alberta page, we do nothing until player either ESC or presses a scenic place. 
        if currentScreen == 'Alberta':
            Alberta()
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()
                    selectSubProvAlberta(pos)
        
        if currentScreen == 'Banff National Park':
            screen.blit(BanffNationalPark, (0,0))
            currentScreen = 'Quiz'
            runQuizOne(questionBanff)

        
        # Update the display (screen)
        pygame.display.flip()