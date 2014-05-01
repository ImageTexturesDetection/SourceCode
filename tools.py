#!/usr/bin/python2.7
# import Image
# import numpy as np
import cv2
import sys
import pickle
import os.path
# import cv
import random
from lbp import Lbp


class GetOutOfLoop( Exception ):
	pass



class Tools:

	distance=3
	pat_size = 30
	tresh=sys.argv[2]
	# hist_pattern=Lbp.create_hist(200,450,30)

	fname=sys.argv[1]+"d"+str(distance)

	img = cv2.imread(sys.argv[1], 0)
	white = cv2.imread(sys.argv[1])
	temp = cv2.imread(sys.argv[1])
	height, width, depth = white.shape

#	white = white[0:((height/distance)*distance),0:((width/distance)*distance)]
#	height, width, depth = white.shape
	biggest = min(height, width)
	height = biggest
	width = biggest
	color=[0,0,0]	

	all_hist=[]

	@classmethod
	def create_white(self):
		self.white = cv2.imread(sys.argv[1])
		(y,x)=(self.width, self.height)
		i = 0
		j = 0
		# self.white[:,:] = [255,0,0]
		while(i < x):
			j=0
			while(j< y):
				# print self.white[i,j]
				# self.white.itemset((i,j), 255)
				self.white[i,j]=[255,255,255]
				j+=1
			i+=1
		
		
		

	@classmethod
	def hist_comp(self,hist1,hist2):
		t1=0
		for i in range(257):
			t1+=min(hist1.get(i,0) , hist2.get(i,0))
		#print t1
		return (True if t1>=float(self.tresh) else False)

	@classmethod
	def colorize(self,elem):
		x0=elem[0]
		y0=elem[1]
		(i,j)=(x0,y0)
	
		while(i< x0 + elem[2]):
			j=y0
			while(j< y0 + elem[2]):
				# if self.is_white(i,j):
				self.white[i,j]=self.color
				j+=1
			i+=1
	
	@classmethod
	def divide(self,x0,y0,long):
		if long==-1:
			long=int(self.biggest*0.8)
			# long=int(self.pat_size*2)
			
		
		# generate as_many_windows_as_possible
		xT = 0
		yT = 0
		# nb3=((self.height/self.distance)*self.distance)/long
		# nb=((self.width/self.distance)*self.distance)/long
		
		nb3=self.height/long
		nb=self.width/long

		while nb3 !=0:
			nb2=nb
			xT=x0
			while nb2 !=0:
				self.all_hist.append(Lbp().create_hist(xT,yT,long))	
				print "creeyit un histo"
				xT+=long
				nb2-=1
			yT+=long;
			nb3-=1	
		
		if (long-self.distance) >= self.distance*4:
			self.divide(0,0,long-self.distance)

		f=open(self.fname,'w')
		pickle.dump(self.all_hist,f)
		f.close()

	@classmethod
	def is_white(self,i,j):
		return ((self.white[i,j,0]==255)and(self.white[i,j,1]==255)and(self.white[i,j,2]==255))

	@classmethod
	def check_squar(self,i,j):
		a=i
		while (a < i+self.pat_size-1):
			b=j
			while (b < j+self.pat_size-1):
				if not(self.is_white(a,b)):
					return False				
				b+=1
			a+=1
	
		return True

	@classmethod
	def search_pattern(self):

		i = 0
		# print "aaaaaaaaaaaaaaaaaaaaaaa"
		
		try:
			while(i < self.width-self.pat_size-1):
				j=0
				while(j< self.height-self.pat_size-1):
					
					# print self.white[i,j]
					if self.is_white(i,j):
						if(self.check_squar(i,j)):
							raise GetOutOfLoop			
					j+=1				
				i+=1
			return False

		except GetOutOfLoop:
			self.hist_pattern=Lbp.create_hist(i,j,self.pat_size)
			self.color = [random.randint(0,254),random.randint(0,254),random.randint(0,254)]
			self.colorize([i,j,self.pat_size])
			print(i,j)
			return True



	@classmethod
	def search(self):
		# print (self.width, self.height)
		if not(os.path.isfile(self.fname)):
			self.divide(0,0,-1)
		else:
			f=open(self.fname)
			self.all_hist=pickle.load(f)
			f.close()
		
		self.create_white()

		self.temp = self.white.copy()
		while(self.search_pattern()):
			
			for elem in self.all_hist:
				if(self.hist_comp(elem[3],self.hist_pattern[3]) and elem[2]>10):
					self.colorize(elem)
					# self.all_hist.remove(elem)
					# cv2.imshow('whit'+sys.argv[1],self.white)
			
			cv2.imshow('white',self.white)

			self.tresh=sys.argv[2]
			print 'press "y" if you like it, or press "n" to change the treshold value.'

			key = cv2.waitKey(0)
			while (key != ord('y')):	# wait for 'y' key to save and continue
				if key == ord('n'):      				# wait for 'n' key to change treshold value
					print "please enter the new treshold value : "
					self.tresh=raw_input()
					self.white = self.temp.copy()
					break
				else:
					key = cv2.waitKey(0)
				pass
			self.temp = self.white.copy()
			# cv2.destroyAllWindows()
			# self.tresh=raw_input();

		# cv2.imshow('image',self.img)
		# cv2.imshow('whit'+sys.argv[1],self.white)
		print "press q to quit"
		while (cv2.waitKey(0) != ord('q')):
			pass
		cv2.destroyAllWindows()
	
