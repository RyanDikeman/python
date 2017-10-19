from graphics import *

def main():
    win = GraphWin('FACE', 400, 400) # give title and dimensions
    win.yUp() # make right side up coordinates!

    head = Circle(Point(40,100), 25) # set center and radius
    head.setFill("#ff7f22")
    head.draw(win)

    eye1 = Circle(Point(30, 105), 5)
    eye1.setFill('#00ff00')
    eye1.draw(win)

    eye2 = Line(Point(45, 105), Point(55, 105)) # set endpoints
    eye2.setWidth(3)
    eye2.draw(win)

    mouth = Oval(Point(30, 90), Point(50, 85)) # set corners of bounding box
    mouth.setFill("#ff7f00")
    mouth.draw(win)

    aline = Line(Point(0, 0), Point(200, 200)) # set endpoints
    aline.setWidth(3)
    aline.draw(win)



    label = Text(Point(100, 120), 'SMILE')
    label.draw(win)

    message = Text(Point(win.getWidth()/2, 20), 'Click anywhere to quit.')
    message.draw(win)
    win.getMouse()
    win.close()

main()
