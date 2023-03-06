####################
# Hitbox library by Pierce Jones
# v.1.0
####################
try:
    from graphics import *
except:
    import graphics
from math import *

def checkCollision(circ1, circ2):
    """Returns True if collision is found and False if not"""
    c1 = circ1.getCenter()
    c2 = circ2.getCenter()
    r1 = circ1.getRadius()
    r2 = circ2.getRadius()
    dist = sqrt((c1.getY() - c2.getY())**2 + (c1.getX() - c2.getX())**2)
    if dist <= r1 + r2:
        return True
    else:
        return False
