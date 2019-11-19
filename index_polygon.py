#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 18 09:57:27 2019

@author: valteresj
"""

import numpy as np

def point_in_poly(x,y,poly):
    n = len(poly)
    n_points=len(x)
    flag_inside=[]
    for j in range(n_points):
        p1x,p1y = poly[0]
        inside = False
        for i in range(n+1):
            p2x,p2y = poly[i % n]
            if y[j] > min(p1y,p2y):
                if y[j] <= max(p1y,p2y):
                    if x[j] <= max(p1x,p2x):
                        if p1y != p2y:
                            xints = (y[j]-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                        if p1x == p2x or x[j] <= xints:
                            inside = not inside
            p1x,p1y = p2x,p2y
        flag_inside.append(inside)

    return flag_inside

class IPI(object):
    def __init__(self,polygon):
        self.polygon=polygon
    
    def index_in_polygon_image(self):
        x_min=min([i[0]for i in self.polygon])
        y_min=min([i[1]for i in self.polygon])
        x_max=max([i[0]for i in self.polygon])
        y_max=max([i[1]for i in self.polygon])
        
        x_seq=list(range(x_min,x_max+1))
        y_seq=list(range(y_min,y_max+1))
        
        x_save=[]
        y_save=[]
        for index,i in enumerate(y_seq):
            y_points=[i]*len(x_seq)
            flag=point_in_poly(x_seq,y_points,self.polygon)
            index_inside=np.where(np.array(flag)==True)[0]
            if len(index_inside)>0:
                x_save.extend(list(np.array(x_seq)[index_inside]))
                y_save.extend(list(np.array(y_points)[index_inside]))
        return x_save,y_save