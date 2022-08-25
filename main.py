from tkinter import Image
import PySimpleGUI as gui      
from time import sleep
import threading
from PIL import Image

layout = [      
    [gui.Graph(canvas_size=(900, 900), graph_bottom_left=(0,0), graph_top_right=(900, 900), background_color='white', key='graph')],      
]      

window = gui.Window('DVD Screensaver Demo', layout, finalize=True)       
graph = window['graph']

imgWidth, imgHeight = Image.open("res/dvdvideo.png").size
imgHeight = imgHeight

xPos, yPos = 0, imgHeight

dvdVideo = graph.draw_image("res/dvdvideo.png", location=(xPos, yPos))

print(imgWidth, imgHeight)

def test():
    global xPos, yPos
    xVel, yVel = 0, 1
    
    while True:
        graph.MoveFigure(dvdVideo, xVel, yVel)
        xPos += xVel
        yPos += yVel

        # check for collision
        if yPos >= 900:
            yVel = -1
        elif yPos <= imgHeight:
            yVel = 1

        if xPos >= (900 - imgWidth):
            xVel = -1
        elif xPos <= 0:
            xVel = 1

        sleep(.005)

threading.Thread(target=lambda: test()).start()

event, values = window.read()    