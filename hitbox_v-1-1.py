####################
# Hitbox library by Pierce Jones
# v.2.0
####################
try:
    from graphics import *
except:
    import graphics

def checkCollision(obj1, obj2):
    """Returns True if collision is found and False if not"""
    if obj1.testCollision_CircleVsCircle(obj1, obj2):
        return True
    else:
        if obj1.testCollision_CircleVsRectangle(obj2):
            return True
        elif obj2.testCollision_CircleVsRectangle(obj1):
            return True
        else:
            if obj1.testCollision_CircleVsPoint(obj1, obj2.getCenter()):
                return True
            elif obj2.testCollision_CircleVsPoint(obj2, obj1.getCenter()):
                return True
            else:
                return False
