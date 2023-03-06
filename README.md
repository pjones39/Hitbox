# Hitbox
a hitbox and graphics library for python

---
checkCollision()
---
**this function takes two(2) object parameters and tests if they have collided or not, if so, it return True, if not, it returns False**

e.g.

circle1 = Cricle(Point(100, 100), 20)
square1 = Rectangle(Point(200, 200), Point(300, 300))

if checkCollision(circle1, square1):
    

---
checkWindowCollision()
---
**this function takes two(2) parameters, one the object, the other is the window object it's on. It checks to see if the object has collided
with the window, if so, it returns which axis as a string, if not, it returns False**

e.g. 

window1 = GraphWin('window1', 1000, 650)
circle = Circle (Point(500, 300), 20)
dx = 1
speed = 10

while True:
    if checkWindowCollision(circle, window1) == 'x':
        dx *= -1
        circle.move(dx * speed, 0)
       
---
graphics library
---
Simple object oriented graphics library
The library is designed to make it very easy for novice programmers to
experiment with computer graphics in an object oriented fashion. It is
written by John Zelle with modifications by Scott Nissley for use with 
the book "Python Programming: An Introduction to Computer Science" 
(Franklin, Beedle & Associates).

LICENSE: This is open-source software released under the terms of the
GPL (http://www.gnu.org/licenses/gpl.html).

PLATFORMS: The package is a wrapper around Tkinter and should run on
any platform where Tkinter is available.

INSTALLATION: Put this file somewhere where Python can see it.

OVERVIEW: There are two kinds of objects in the library. The GraphWin
class implements a window where drawing can be done and various
GraphicsObjects are provided that can be drawn into a GraphWin. As a
simple example, here is a complete program to draw a circle of radius
10 centered in a 100x100 window:
--------------------------------------------------------------------
from graphics import *
def main():
    win = GraphWin("My Circle", 100, 100)
    c = Circle(Point(50,50), 10)
    c.draw(win)
    win.getMouse() # Pause to view result
    win.close()    # Close window when done
main()
--------------------------------------------------------------------
GraphWin objects support coordinate transformation through the
setCoords method and mouse and keyboard interaction methods.
The library provides the following graphical objects:
    Point
    Line
    Circle
    Oval
    Rectangle
    Polygon
    Text
    Entry (for text-based input)
    Image
Various attributes of graphical objects can be set such as
outline-color, fill-color and line-width. Graphical objects also
support moving and hiding for animation effects.
The library also provides a very simple class for pixel-based image
manipulation, Pixmap. A pixmap can be loaded from a file and displayed
using an Image object. Both getPixel and setPixel methods are provided
for manipulating the image.

DOCUMENTATION: For complete documentation, see Chapter 4 of "Python
Programming: An Introduction to Computer Science" by John Zelle,
published by Franklin, Beedle & Associates.  Also see
http://mcsp.wartburg.edu/zelle/python for a quick reference
---
Thanks! -Crackle6
