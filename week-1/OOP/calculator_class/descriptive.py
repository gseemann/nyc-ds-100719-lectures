#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 10 16:11:46 2019

@author: gabrielseemann
"""

import math

class Calculator:
    
    def __init__(self, data):
        self.data = data
        self.__reinit__()
        
    def __reinit__(self):
        self.length = self.__getLength__()
        self.mean = self. __getMean__()
        self.median = self.__getMedian__()
        self.variance = self.__getVariance__()
        self.stand_dev = self.__getStand_Dev__()
        
        
    def __getLength__(self):
        return len(self.data)
        
    def __getMean__(self):
        return sum(self.data)/self.length
        
    def __getMedian__(self):
        self.data.sort()
        if self.length%2:
            return self.data[self.length//2]
        else:
            return (self.data[self.length//2]+self.data[self.length-1])/2
        
    def __getVariance__(self):
        xnum = 0
        for i in self.data:
            xnum+=(i-self.mean)**2
        return xnum/(self.length -1)
    
        
    def __getStand_Dev__(self):
        return math.sqrt(self.variance)
    
    def add_data(self, new_data):
        self.data.extend(new_data)
        self.__reinit__()
    
    def remove_data(self, remove):
        for i in remove:
            if i in self.data:
                self.data.remove(i)
        self.__reinit__()
        
    
                
        
    
    
    