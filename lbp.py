#!/usr/bin/python2.7
# import Image
# import numpy as np
import cv2
import sys
import pickle
import os.path
# import cv
import random


class Lbp:
	
	values=[0,255]
	img = cv2.imread(sys.argv[1], 0)
	calc_val=True

	@classmethod
	def generate_val(self):
		
		valeur_bin=[[0,0,0,0,0,0,0,1],[0,0,0,0,0,0,1,1],[0,0,0,0,0,1,1,1],[0,0,0,0,1,1,1,1],
					[0,0,0,1,1,1,1,1],[0,0,1,1,1,1,1,1],[0,1,1,1,1,1,1,1]]

		for elem in valeur_bin:
			for j in range(8):
				val=0
				for i in range(8):
					val+=elem[i]*pow(2,i)
				self.values.append(val)
				elem.append(elem.pop(0)) #rotation

		self.values = sorted(self.values)

	@classmethod
	def thresholded(self, center, pixels):
	    out = []
	    for a in pixels:
	        if a >= center:
	            out.append(1)
	        else:
	            out.append(0)
	    return out
	@classmethod
	def get_pixel_else_0(self, x, y):
	    try:
	    	return self.img[x,y]
	    except IndexError:
	        return 0

	@classmethod
	def value(self,x,y):

		center        = self.get_pixel_else_0(x,y)
		top_left      = self.get_pixel_else_0(x-1, y-1)
		top_up        = self.get_pixel_else_0(x, y-1)
		top_right     = self.get_pixel_else_0(x+1, y-1)
		right         = self.get_pixel_else_0(x+1, y )
		left          = self.get_pixel_else_0(x-1, y )
		bottom_left   = self.get_pixel_else_0(x-1, y+1)
		bottom_right  = self.get_pixel_else_0(x+1, y+1)
		bottom_down   = self.get_pixel_else_0(x,   y+1 )

		values = self.thresholded(center, [top_left, top_up, top_right, right, bottom_right, bottom_down, bottom_left, left])

		weights = [1, 2, 4, 8, 16, 32, 64, 128]
		res = 0
		for a in range(0, len(values)):
		    res += weights[a] * values[a]

		return res

	@classmethod	
	def create_hist(self,x0,y0,long):
		if self.calc_val :
			self.generate_val()
			self.calc_val=False
		hist={}
		somme = 0
		
		for elem in self.values:
			hist[elem]=0
		hist[256]=0
		
		for x in range(x0,x0+long+1):
			for y in range(y0,y0+long+1):
				v=self.value(x,y)
				
				if v in hist:
					hist[v]+=1
				else:
					hist[256]+=1
		
		for elem in hist:
			somme+=hist[elem]

		if somme != 0:
			for elem in hist:
				hist[elem]/=float(somme)
		return [x0,y0,long,hist]

# **********************************************************

