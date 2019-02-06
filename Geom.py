#  File: Geom.py

#  Description: Assignment4

#  Student Name: Shimin Zhang

#  Student UT EID: sz6939

#  Course Name: CS 313E

#  Unique Number: 51350

#  Date Created: 9/15/2018

#  Date Last Modified: 9/17/2018

import math

class Point(object):
    # constructor
    # x and y are floats
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # get distance
    # other is a Point object
    def dist(self, other):
        return math.hypot(self.x - other.x, self.y - other.y)

    # get a string representation of a Point object
    # takes no arguments
    # returns a string
    def __str__(self):
        return '(' + str(self.x) + ", " + str(self.y) + ")"

    # test for equality
    # other is a Point object
    # returns a Boolean
    def __eq__(self, other):
        tol = 1.0e-16
        return ((abs(self.x - other.x) < tol) and (abs(self.y - other.y) < tol))


class Circle(object):
    # constructor
    # x, y, and radius are floats
    def __init__(self,  x=0, y=0,radius=1,):
        self.radius = radius
        self.center = Point(x, y)

    # compute cirumference
    def circumference(self):
        return 2.0 * math.pi * self.radius

    # compute area
    def area(self):
        return math.pi * self.radius * self.radius

    # determine if point is strictly inside circle
    def point_inside(self, p):
        return (self.center.dist(p) < self.radius)

    # determine if a circle is strictly inside this circle
    def circle_inside(self, c):
        distance = self.center.dist(c.center)
        return (distance + c.radius) < self.radius

    # determine if a circle c intersects this circle (non-zero area of overlap)
    # the only argument c is a Circle object
    # returns a boolean
    def does_intersect(self, c):
        distance = self.center.dist(c.center)
        return distance<(self.radius+c.radius)


    # determine the smallest circle that circumscribes a rectangle
    # the circle goes through all the vertices of the rectangle
    # the only argument, r, is a rectangle object
    def circle_circumscribes(self, r):
        x = r.ul.x + (r.length() / 2)
        y = r.lr.y + (r.width() / 2)
        radius = (r.ul.dist(r.lr)) / 2
        return Circle(x, y, radius)

    # string representation of a circle
    # takes no arguments and returns a string
    def __str__(self):
        return 'Center: ' + str(self.center) + ', Radius: ' + str(self.radius)

    # test for equality of radius
    # the only argument, other, is a circle
    # returns a boolean
    def __eq__(self, other):
        tol = 1.0e-16
        return abs(self.radius-other.radius)<tol


class Rectangle(object):
    # constructor
    def __init__(self, ul_x=0, ul_y=1, lr_x=1, lr_y=0):
        if ((ul_x < lr_x) and (ul_y > lr_y)):
            self.ul = Point(ul_x, ul_y)
            self.lr = Point(lr_x, lr_y)
        else:
            self.ul = Point(0, 1)
            self.lr = Point(1, 0)

    # determine length of Rectangle (distance along the x axis)
    # takes no arguments, returns a float
    def length(self):
        return abs(self.ul.x-self.lr.x)

    # determine width of Rectangle (distance along the y axis)
    # takes no arguments, returns a float
    def width(self):
        return abs(self.ul.y - self.lr.y)

    # determine the perimeter
    # takes no arguments, returns a float
    def perimeter(self):
        return 2*(self.length()+self.width())

    # determine the area
    # takes no arguments, returns a float
    def area(self):
        return self.length() * self.width()

    # determine if a point is strictly inside the Rectangle
    # takes a point object p as an argument, returns a boolean
    def point_inside(self, p):
        return self.ul.x<p.x<self.lr.x and self.lr.y<p.y<self.ul.y

    # determine if another Rectangle is strictly inside this Rectangle
    # takes a rectangle object r as an argument, returns a boolean
    # should return False if self and r are equal
    def rectangle_inside(self, r):
        return self.point_inside(r.ul) and self.point_inside(r.lr)

    # determine if two Rectangles overlap (non-zero area of overlap)
    # takes a rectangle object r as an argument returns a boolean
    def does_intersect(self, other):
        ul_p=other.ul
        ur_p=Point(other.lr.x,other.ul.y)
        ll_p=Point(other.ul.x,other.lr.y)
        lr_p=other.lr

        if self.point_inside(ul_p) or self.point_inside(ur_p) or self.point_inside(ll_p) or self.point_inside(lr_p) or other.point_inside(self.lr):
            return True

    # sides of the rectangle are tangents to circle c
    # takes a circle object c as input and returns a rectangle object
    def rect_circumscribe(self, c):
        ul_x = c.center.x - c.radius
        ul_y = c.center.y + c.radius
        lr_x = c.center.x + c.radius
        lr_y = c.center.y - c.radius
        return Rectangle(ul_x, ul_y, lr_x, lr_y)

    def __str__(self):
        return "Upper Left: (" + str(self.ul.x) + ", " + str(self.ul.y) + "), Lower Right: (" + str(self.lr.x) + ", " + str(self.lr.y) + ") "

     # determine if two rectangles have the same length and width
     # takes a rectangle other as argument and returns a boolean
    def __eq__(self, other):
        tol = 1.0e-16
        return abs(self.width() - other.width()) < tol and abs(self.length() - other.length()) < tol

def main():


# open the file geom.txt
    file=open('./geom.txt','r')

# create Point objects P and Q
    p_line = file.readline().strip().split(" ")
    P= Point(float(p_line[0]), float(p_line[1]))


    q_line = file.readline().strip().split(" ")
    Q = Point(float(q_line[0]), float(q_line[1]))


# print the coordinates of the points P and Q
    print('Coordinates of P: '+str(P))
    print('Coordinates of P: '+str(Q))

# find the distance between the points P and Q
    print('Distance between P and Q: '+str(P.dist(Q)))


# create two Circle objects C and D
    c_line = file.readline().strip().split(" ")
    C= Circle(float(c_line[0]), float(c_line[1]), float(c_line[2]))


    d_line = file.readline().strip().split(" ")
    D = Circle(float(d_line[0]), float(d_line[1]), float(d_line[2]))


# print C and D
    print('Circle C: '+str(C))
    print('Circle D: '+str(D))

# compute the circumference of C
    print('Circumference of C: '+str(C.circumference()))

# compute the area of D
    print('Area of D: '+str(D.area()))

# determine if P is strictly inside C
    if C.point_inside(P):
        print('P is inside C')
    else:
        print('P is not inside C')


# determine if C is strictly inside D
    if C.circle_inside(D):
        print('C is inside D')
    else:
        print('C is not inside D')

# determine if C and D intersect (non zero area of intersection)
    if C.does_intersect(D):
        print('C does intersect D')
    else:
        print('C does not intersect D')

# determine if C and D are equal (have the same radius)
    if C==D:
        print('C is to D')
    else:
        print('C is not equal to D')

# create two rectangle objects G and H
    g_line = file.readline().strip().split(" ")
    G= Rectangle(float(g_line[0]), float(g_line[1]), float(g_line[2]), float(g_line[3]))


    h_line = file.readline().strip().split(" ")
    H = Rectangle(float(h_line[0]), float(h_line[1]), float(h_line[2]),float(h_line[3]))


# print the two rectangles G and H
    print('Rectangle G: '+str(G))
    print('Rectangle H: '+str(H))

# determine the length of G (distance along x axis)
    print('Length of G: '+str(G.length()))

# determine the width of H (distance along y axis)
    print('Width of H: ' + str(H.width()))

# determine the perimeter of G
    print('Perimeter of G:' +str(G.perimeter()))

# determine the area of H
    print('Area of H: ' + str(H.area()))

# determine if point P is strictly inside rectangle G
    if G.point_inside(P):
        print('P is inside G')
    else:
        print('P is not inside G')

# determine if rectangle G is strictly inside rectangle H
    if H.rectangle_inside(G):
        print('G is inside H')
    else:
        print('G is not inside H')

# determine if rectangles G and H overlap (non-zero area of overlap)
    if H.does_intersect(G):
        print('G does overlap H')
    else:
        print('G does not overlap H')

# find the smallest circle thcat circumscribes rectangle G
# goes through the four vertices of the rectangle
    print('Circle that circumscribes G: '+ str(Circle().circle_circumscribes(G)))

# find the smallest rectangle that circumscribes circle D
# all four sides of the rectangle are tangents to the circle
    print('Rectangle that circumscribes D: '+ str(Rectangle().rect_circumscribe(D)))

# determine if the two rectangles have the same length and width
    if (G == H):
        print("Rectangle G is equal to H")
    else:
        print("Rectangle G is not equal to H")

# close the file geom.txt
    file.close()

# This line above main is for grading purposes. It will not affect how
# your code will run while you develop and test it.
# DO NOT REMOVE THE LINE ABOVE MAIN
if __name__ == "__main__":
    main()
