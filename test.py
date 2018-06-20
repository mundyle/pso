import random

psi = 0.729844 # Inertia weight to prevent velocities becoming too large
phi_s = 1.496180 # Scaling co-efficient on the social component
phi_p= 1.496180 # Scaling co-efficient on the cognitive component

dimension = 3 # Size of the problem
iterations = 3000
num_particles= 30


class Particle:

	#each particle will have a velocity, position and best_position
	velocity = []
	position = []
	pBest = []

	#The constructor for each particle 
	def __init__(self):

		#This for loop, it creates random particles with random positions 
		for i in range(dimension):

			#Initiating a random starting position for a particle
			#random.random() is a random number between 0 and 1
			#This passes the object in, which is the particle, and appends a random number as the starting position to the array Position
			self.position.append(random.random())

			#Initiating a random velocity for a particle
			#Passes through the object/particle in, appends a random number for starting velocity between 0 and 1 to the array Velocity
			self.velocity.append(0.01 * random.random())

			#Initiating best position, as the current position at that dimension
			#Passes through the object/particle, appends the positions of the particle into the pBest array
			#Basically copies the position list into the pBest
			self.pBest.append(self.position[i])

		print "Position"
		print self.position
		print
		print "Velocity"
		print self.velocity
		print
		print "pBest" 
		print self.pBest 

		return 

	def updatePosition(self):

		for i in range(dimension):
			self.position[i] = self.position[i] + self.velocity[i]

		
		print self.position

	# def updateVelocity(self, gBest):

	# 	for i in range(dimension):

	# 		#creates the random numbers between 1 and 0 for the calculations
	# 		rs = random.random()
	# 		rp = random.random()

	# 		#This creates the attraction portion of the velocity equation 
	# 		#Takes in the constant phi_p initialized above
	# 		#Takes the best position of the whole SWARM, then subtracting the position of the particle 
	# 		social = phi_p * rp * (gBest[i] - self.position[i])

	# 		cognitive = phi_s * rs * (self.pBest[i] - self.position[i])

	# 		self.velocity[i] = (psi * self.velocity[i]) + social + cognitive

	# 	print self.velocity

	# 	return 


particle = Particle()
particle.updatePosition()



