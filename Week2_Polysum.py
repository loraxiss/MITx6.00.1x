# -*- coding: utf-8 -*-
import math

def polysum(n, s):
    '''
    n: number of sides of a regular polygon

    s: length of the sides of the same regular polygon
    
    returns: the sum of the area and the square of the perimeter of a regular polygon rounded to 4 decimal places
    '''
    #calculate are of the polygon:     (0.25∗n∗s**2)/(tan(π/n))
    area = (0.25 * n * s**2) / (math.tan(math.pi / n))
    
    #calculate perimeter of the polygon: n*s
    perim = n*s
    
    #return the sum of the area and the square of the perimeter to 4 decimal places
    return(round(area + perim**2,4))
