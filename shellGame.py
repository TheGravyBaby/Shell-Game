from graphics import * 
from math import *
import random 

win = GraphWin("Shell Game", 500,500)


def inside(point, rectangle):                              

    ll = rectangle.getP1()  # assume p1 is ll (lower left)
    ur = rectangle.getP2()  # assume p2 is ur (upper right)

    return ll.getX() < point.getX() < ur.getX() and ll.getY() < point.getY() < ur.getY()    #mathematical function for finding box dimensions

def insideCircle(point, circle):                              

    centerPoint = circle.getCenter()
    radius = circle.getRadius()

    return (centerPoint.getX() - radius) < point.getX() < (centerPoint.getX() + radius) and (centerPoint.getY() - radius) < point.getY() < (centerPoint.getY() + radius)

def setupPage():

    winText = Text(Point(250, 350), "YOU WIN")
    loseText = Text(Point(250, 400), "YOU LOSE")

    radius = 50
    cupsRotated = False

    c1 = Circle(Point(100,250),radius)
    c2 = Circle(Point(250,250),radius)
    c3 = Circle(Point(400,250),radius)
    c1.setFill('gray')
    c2.setFill('green')
    c3.setFill('gray')

    c1.draw(win)
    c2.draw(win)
    c3.draw(win)

    startButton = Rectangle(Point(25, 25), Point(175, 75))
    startButton.setFill('lightgreen')
    startButton.draw(win)

    startButtonText = Text(Point(100, 50), "Start")
    startButtonText.draw(win)

    infoText = Text(Point(350, 50), "Hit the start button, \n and then try to follow the green cup. \n Click the cup at the end to see if you win!")
    infoText.draw(win)

    while True:
        clickPoint = win.getMouse()                               #check for mouse clicks and get location of click

        if inside(clickPoint, startButton):
            c2.setFill('grey')
            time.sleep(1)
            
            for i in range(5):
                rando = random.randint(1,3)                       #give us a random number             
                if rando == 1:
                    swapCups(c1, c2)
                if rando == 2:
                    swapCups(c1, c3)
                if rando == 3:
                    swapCups(c2, c3)
            cupsRotated = True

        if cupsRotated:
            winClick = win.getMouse()

            if insideCircle(winClick, c2):
                print("You win")
                c2.setFill('green')
                winText.draw(win)
                time.sleep(2)
                win.close()

            else:
                print("You lose")
                c2.setFill('green')
                loseText.draw(win)
                time.sleep(2)
                win.close()

#swap any two cups in any position 
def swapCups(cup1, cup2):
    cup1XStart = cup1.getCenter().getX()        #constants so they dont change during our math 
    cup2XStart = cup2.getCenter().getX()

    cup1.move((cup2XStart - cup1XStart)/2, 75) 
    time.sleep(.1)
    cup2.move((cup1XStart - cup2XStart)/2, -75) 
    time.sleep(.1)
    cup1.move((cup2XStart - cup1XStart)/2, -75)
    time.sleep(.1)
    cup2.move((cup1XStart - cup2XStart)/2, 75) 
    time.sleep(.75)

setupPage()