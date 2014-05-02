#!/usr/bin/python2.7

import cv2
import sys
# import os.path
import os
import random

class GetOutOfLoop( Exception ):
	pass

class Tools:

	pat_size = 80
	tresh=sys.argv[2]
	pattnb = 1
	pattname = 'patterns/pattern'+str(pattnb)+'.png'
	# hist_pattern=Lbp.create_hist(200,450,30)

	img = cv2.imread(sys.argv[1], 0)
	white = cv2.imread(sys.argv[1])
	temp = cv2.imread(sys.argv[1])
	height, width, depth = white.shape

#	white = white[0:((height/distance)*distance),0:((width/distance)*distance)]
#	height, width, depth = white.shape
	biggest = min(height, width)
	# height = biggest
	# width = biggest
	color=[0,0,0]	

	@classmethod
	def create_white(self):
		self.white = cv2.imread(sys.argv[1])
		(x,y)=(self.height, self.width)
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
	def is_white(self,i,j):
		return ((self.white[i,j,0]==255)and(self.white[i,j,1]==255)and(self.white[i,j,2]==255))

	@classmethod
	def check_squar(self,i,j):
		a=i
		# while (a < i+self.pat_size):
		while (a < i+60):
			b=j
			# while (b < j+self.pat_size):
			while (b < j+60):
				if not(self.is_white(a,b)):
					return False				
				b+=1
			a+=1
	
		return True

	@classmethod
	def search_pattern(self):
		self.white = cv2.imread('white.png')
		i = 0

		try:
			while(i < self.height-self.pat_size-1):
				j=0
				while(j< self.width-self.pat_size-1):
					if self.is_white(i,j):
						if(self.check_squar(i,j)):
							raise GetOutOfLoop			
					j+=1				
				i+=1
			return False

		except GetOutOfLoop:

			self.pattname = 'patterns/pattern'+str(self.pattnb)+'.png'

			cv2.imwrite(self.pattname, self.img[i:i+self.pat_size,j:j+self.pat_size])

			self.color = [random.randint(0,254),random.randint(0,254),random.randint(0,254)]
			# self.colorize([i,j,self.pat_size])

			
			# os.system('matlab -nodesktop -nosplash -r "colorize(\'points.png\',\''+pattname+'\','+self.tresh+','+color+')"')
			
			# os.system("matlab -nodesktop -nosplash -r \"colorize('"+sys.argv[1]+"','"+pattname+"',"+self.tresh+","+self.color+")\"")
			print(i,j)
			return True



	@classmethod
	def search(self):

		if not os.path.exists('data'):
  			os.makedirs('data')
  		if not os.path.exists('patterns'):
  			os.makedirs('patterns')

		# self.create_white()
		self.white[:,:] = [255,255,255]

		cv2.imwrite('white.png', self.white)

		# if not (os.path.isfile('data/'+sys.argv[1]+'.mat')):
		# 	os.system("matlab -nodesktop -nosplash -r \"divide('"+sys.argv[1]+"')\"")
		os.system("matlab -nodesktop -nosplash -r \"divide('"+sys.argv[1]+"')\"")

		self.temp = self.white.copy()
		while(self.search_pattern()):
			self.temp = self.white.copy()
			# print self.pattname
			os.system("matlab -nodesktop -nosplash -r \"colorize('"+sys.argv[1]+"','"+self.pattname+"',"+self.tresh+","+str(self.color)+")\"")
			# print self.pattname
			self.white = cv2.imread('white.png')
			cv2.imshow('white',self.white)
			

			self.tresh=sys.argv[2]
			print 'press "y" if you like it, or press "n" to change the treshold value.'

			key = cv2.waitKey(0)
			while (key != ord('y')):	# wait for 'y' key to save and continue
				if key == ord('n'):      				# wait for 'n' key to change treshold value
					print "please enter the new treshold value : "
					self.tresh=raw_input()
					# self.white = self.temp.copy()
					cv2.imwrite('white.png', self.temp)
					break
				else:
					key = cv2.waitKey(0)
				pass
			if key == ord('y'): 
				self.pattnb+=1
				self.temp = self.white.copy()

		print "press q to quit"
		while (cv2.waitKey(0) != ord('q')):
			pass
		cv2.destroyAllWindows()
	
Tools.search()
