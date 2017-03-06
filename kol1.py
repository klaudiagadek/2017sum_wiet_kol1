import random
def flight_simulator():
	angle = random.randint(1,360) 
	print str(angle) + "-> Current state"
	print str(correct_angle(angle))  + "-> State after correction"
	

def correct_angle(angle):
	max_angle=90
	if angle > max_angle:
		return angle%max_angle
	else:
		return angle

if __name__ =="__main__":
	while True:
		flight_simulator()


