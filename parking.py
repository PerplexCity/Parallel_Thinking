#1000 feet long
import random
import numpy
import time

def parking():
	available = []
	#ideally the available space would be continuously defined
	#for our purposes though, we'll create ten thousand hash marks
	for i in range(10000):
		available.append(float(i)/10)
	
	cars = 0

	while True:
		#random normally distributed car length
		carlength = round(numpy.random.normal(15,1),1)
		
		#space required is another two feet (one on each end)
		space = carlength + 2
		available_car = []

		for spot in available:
			#if hash, the hash 10 feet back, and the hash all the way back are all available,
			#then that spot is available
			if all(round(spot-i,1) in available for i in [0,10,space]):
				available_car.append(spot)

		if len(available_car)>0:
			#randomly choose a place to park
			park = random.choice(available_car)
			
			for i in range(int(space*10)):
				#get rid
				available.remove(round(park-0.1*i,1))
			cars += 1
			#print "Car %d, %s feet long, parked between %s feet and %s feet" % (cars, str(carlength), str(park), str(park-space))
		
		else:
			#print "Full at %d cars!" %(cars)
			print cars
			break


for i in range(100):
	parking()






