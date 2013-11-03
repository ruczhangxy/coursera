from vec import Vec
from mat import Mat
from matutil import *
import math

## Task 1
def identity(labels = {'x','y','u'}):
    '''
    In case you have never seen this notation for a parameter before,
    the way it works is that identity() now defaults to having labels 
    equal to {'x','y','u'}.  So you should write your procedure as if 
    it were defined 'def identity(labels):'.  However, if you want the labels of 
    your identity matrix to be {'x','y','u'}, you can just call 
    identity().  Additionally, if you want {'r','g','b'}, or another set, to be the
    labels of your matrix, you can call identity({'r','g','b'}).  
    '''
    return Mat((labels, labels),{(x,x):1 for x in labels})

## Task 2
def translation(x,y):
    '''
    Input:  An x and y value by which to translate an image.
    Output:  Corresponding 3x3 translation matrix.
    '''
    labels = {'x','y','u'}
    return Mat((labels, labels),{('x','x'):1, ('y','y'):1, ('u','u'):1, ('x','u'):x, ('y', 'u'):y})

## Task 3
def scale(a, b):
    '''
    Input:  Scaling parameters for the x and y direction.
    Output:  Corresponding 3x3 scaling matrix.
    '''
    labels = {'x','y','u'}
    return Mat((labels, labels),{('x', 'x'):a, ('y','y'):b, ('u','u'):1})

## Task 4
def rotation(angle):
    '''
    Input:  An angle in radians to rotate an image.
    Output:  Corresponding 3x3 rotation matrix.
    Note that the math module is imported.
    '''
    labels = {'x','y','u'}
    return Mat((labels, labels),{('x', 'x'):math.cos(angle), ('x', 'y'):-math.sin(angle), ('y','x'):math.sin(angle), ('y','y'):math.cos(angle), ('u','u'):1})

## Task 5
def rotate_about(x,y,angle):
    '''
    Input:  An x and y coordinate to rotate about, and an angle
    in radians to rotate about.
    Output:  Corresponding 3x3 rotation matrix.
    It might be helpful to use procedures you already wrote.
    '''
    m1 = translation(-x,-y)
    m2 = rotation(angle)
    m3 = translation(x,y)

    return m3*m2*m1

## Task 6
def reflect_y():
    '''
    Input:  None.
    Output:  3x3 Y-reflection matrix.
    '''
    return scale(-1,1)

## Task 7
def reflect_x():
    '''
    Inpute:  None.
    Output:  3x3 X-reflection matrix.
    '''
    return scale(1,-1)
    
## Task 8    
def scale_color(scale_r,scale_g,scale_b):
    '''
    Input:  3 scaling parameters for the colors of the image.
    Output:  Corresponding 3x3 color scaling matrix.
    '''
    labels = {'r', 'g', 'b'}
    return Mat((labels, labels), {('r','r'):scale_r,('g','g'):scale_g,('b','b'):scale_b} )

## Task 9
def grayscale():
    '''
    Input: None
    Output: 3x3 greyscale matrix.
    '''
    labels = {'r', 'g', 'b'}
    row_dict = {}
    row_dict['r'] = Vec(labels, {'r':77/256, 'g':151/256, 'b':28/256})
    row_dict['g'] = Vec(labels, {'r':77/256, 'g':151/256, 'b':28/256})
    row_dict['b'] = Vec(labels, {'r':77/256, 'g':151/256, 'b':28/256})
    return rowdict2mat(row_dict)

## Task 10
def reflect_about(p1,p2):
    '''
    Input: 2 points that define a line to reflect about.
    Output:  Corresponding 3x3 reflect about matrix.
    '''
    pass


