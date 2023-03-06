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
    try:
        if obj1.testCollision_CircleVsCircle(obj1, obj2):
            return True
        else:
            return False
    except:
        try:
            if obj1.testCollision_CircleVsRectangle(obj2):
                return True
            elif obj2.testCollision_CircleVsRectangle(obj1):
                return True
            else:
                return False
        except:
            try:
                if obj1.testCollision_CircleVsPoint(obj1, obj2.getCenter()):
                    return True
                elif obj2.testCollision_CircleVsPoint(obj2, obj1.getCenter()):
                    return True
                else:
                    return False
            except:
                return False

def checkWindowCollision(obj, win):
    """Returns False if no collision, returns the axis walls as a string E.g. 'x' or 'y' if collision is found"""
    xmax = win.getWidth()
    ymax = win.getHeight()
    try:        # It's a circle
        center = obj.getCenter()
        radius = obj.getRadius()
        if center.getX() - radius <= 0 or center.getX() + radius >= xmax:
            return True, 'x'
        elif center.getY() - radius <= 0 or center.getY() + radius >= ymax:
            return True, 'y'
        else:
            return False
    except:
        try:        # It's a polygon
            points = obj.getPoints()
            xmin = win.getWidth()
            ymin = win.getHeight()
            xmax = 0
            ymax = 0
            for point in points:
                if point.getX() < xmin:
                    xmin = point.getX()
                elif point.getY() < ymin:
                    ymin = point.getY()
                elif point.getX() > xmax:
                    xmax = point.getX()
                elif point.getY() > ymax:
                    ymax = point.getY()
            if xmax >= win.getWidth():
                return True, 'x'
            elif ymax >= win.getHeight():
                return True, 'y'
            elif  xmin <= 0:
                return True, 'x'
            elif ymin <= 0:
                return True, 'y'
            else:
                return False
        except:    # It's a rectangle
            temp_polygon = Polygon(obj.getP1(), obj.getP2())
            points = temp_polygon.getPoints()
            xmin = win.getWidth()
            ymin = win.getHeight()
            xmax = 0
            ymax = 0
            for point in points:
                if point.getX() < xmin:
                    xmin = point.getX()
                elif point.getY() < ymin:
                    ymin = point.getY()
                elif point.getX() > xmax:
                    xmax = point.getX()
                elif point.getY() > ymax:
                    ymax = point.getY()
            if xmax >= win.getWidth():
                return True, 'x'
            elif ymax >= win.getHeight():
                return True, 'y'
            elif  xmin <= 0:
                return True, 'x'
            elif ymin <= 0:
                return True, 'y'
            else:
                return False
