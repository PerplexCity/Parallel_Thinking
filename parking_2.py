#1000 feet long
import random
import numpy
import time

def parking(leaders):
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
			#same logic as first simulator until all the leaders have gone
			#after that, only available spaces are those around leaders (or at boundary)
			if cars <= leaders-1:
				if all(round(spot-i,1) in available for i in [0,10,space]):
					available_car.append(spot)
			else:
				if all(round(spot-i,1) in available for i in [0,10,space]):
					if round(spot+0.1, 1) not in available or round(spot - space - 0.1,1) not in available:
						available_car.append(spot)

		if len(available_car)>0:
			#randomly choose a place to park
			park = random.choice(available_car)
			
			for i in range(int(space*10)):
				#get rid of subsequent available space once car is parked
				available.remove(round(park-0.1*i,1))
			cars += 1
			#print "Car %d, %s feet long, parked between %s feet and %s feet" % (cars, str(carlength), str(park), str(park-space))
		
		else:
			#print "Full at %d cars!" %(cars)
			return cars
			break

#simple averaging function that will run sim ten times on different values of leaders
def average_park(leaders):
	total = 0
	for i in range(10):
		total += parking(leaders)
	print str(leaders) + ", " + str(float(total)/10)



#sims for 1 through 40 leaders
for i in range(1, 41):
	average_park(i)







