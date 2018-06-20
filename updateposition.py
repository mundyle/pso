import random
import math

#These are the initial terms needed for PSO 

psi = 1 # Inertia weight to prevent velocities becoming too large
phi_s = 2 # Scaling co-efficient on the social component
phi_p= 2 # Scaling co-efficient on the cognitive component

dimension = 1 # Size of the problem/ # of solution phases
iterations = 4
num_particles= 2*dimension


	#Creating the class for the particles in the swarm 

class Particle:

	#each particle will have a velocity, position and best_position
	velocity = []
	position = []
	pBest = []

	#The constructor for each particle 
	#Each particle will have 3 different properties: position, velocity and personal best (pBest)
	def __init__(self):

		#This for loop, it creates random particles with random positions 
		for i in range(dimension):

			#Initiating a random starting position for a particle
			#random.random() is a random number between 0 and 1
			#The random number is then appended into the array, position
			#So the particle/object will have a position vector/array property
			self.position.append(0.01)

			#Initiating a random velocity for a particle
			#Another random number is created, then appended into the velocity array
			#So the particle/object will have a velocity/vector array property
			self.velocity.append(0.002)

			#Initiating best position, as the current position at that dimension
			#This basically copies the position arrayinto the pBest array
			#The particle/obkect will also have a pBest propery shown as an array/vector. 
			self.pBest.append(self.position[i])

			print self.pBest
			print self.position
			print self.velocity
			print

		return



	#This is the method to update the position for each particle. 
	#Takes in the particle, so there is no other arguments needed. 
	def updatePosition(self):

		#Loops through the dimension of each particle 
		for i in range(1,dimension):

			#Start off with URF/Alpha as 1
			URF = 1

			if (self.position[i-1] + (self.velocity[i]*URF) <= 0 ):

				URF = (10**(-5) - self.position[i-1])/self.velocity[i]

				#This updates the position of the particle 
				self.position[i] = self.position[i] + (self.velocity[i] * URF)

				

				#if that value is not less than or equal to 1 
			else:

				#Temporary variable to store the value of the summaton of the position values 
				summation = 0 

				#The summation of the positions are calculated 
				for l in range(len(self.position)):

					#This will get the value from each position of the list position and then add it onto the variable summation
					summation = self.position[l] + summation 

					#Once calculated, URF is equal to 1/summation 
					URF = 1/summation 

					#This updates the position of the particle 
					self.position[l] = self.position[l] + (self.velocity[l] * URF)

		print self.position

		return


	#This is the method used to update the velocity of each particle. 
	#Takes in the object, and the global best of the swarm 
	def updateVelocity(self, gBest):

		for i in range(dimension):

			#creates the random numbers between 1 and 0 for the calculations
			rs = random.uniform(0,1)
			rp = random.uniform(0,1)

			#This creates the attraction portion of the velocity equation 
			#Takes in the constant phi_p initialized above
			#Takes the best position of the whole SWARM, then subtracting the position of the particle 
			social = phi_s * rs * (gBest[i] - self.position[i])


			#Cognitive part is for the particle itself. 
			#It takes the constants phi_p, rs and its personal best, and it's current position 
			cognitive = phi_p * rp * (self.pBest[i] - self.position[i])

			#The equation for calculating the current velocity of the particle 
			self.velocity[i] = (psi * self.velocity[i]) + social + cognitive

		return 




#This is the new class Particle Swarm Optimizer 
class ParticleSwarmOptimizer:

	solution = []

	#This array called Swarm, it is used to hold particle objects created in the Particle class. 
	swarm = []


	#This is the constructor for the class
	#It loops through the number of particles in the swarm 
	#__init__ is for the initialization of the object being created. 
	def __init__(self):

		for h in range(num_particles):

			#creates an object called particle, and it has the properties of the class Particle. 
			particle = Particle()
			# print particle.pBest
			# print particle.velocity
			# print particle.position
			# print

			#This appends that object called particle into the array called swarm, under the passed in particle object. 
			self.swarm.append(particle)
		

		return 


	#This method takes in the particle object, with no other arguments/parameters
	def optimizeCase1(self):


		for i in range(iterations):
			print "iteration", i 
			print

			#Let the first particle arbitrarily be the global best. 
			gBest = self.swarm[0]

			#Looping through the particles in the swarm
			for j in range(num_particles):

				#Returns the pBest from the particle at position swarm[j]
				pBest = self.swarm[j].pBest 

				#if the personal best pi value is less than or equal to the global best pi value, then set the global best to that personal best
				if self.calculatePiCase1(pBest) >= self.calculatePiCase1(gBest.pBest):
					gBest = pBest

			#Once the gbest is found, then set the list Solution the same as gBest. 
			#gBest is a array/vector, same size as the dimension. 
			solution = gBest


#Once that loop is finished, it moves onto this loop, where it updates the position of each particle, before the end of the iteration


			#update position of each particle 
			for k in range(num_particles):

				#takes in the object, and in every particle in the swarm and uses the method updateVelocity, using the global best
				#Does this for updating the position as well, along with the constraints
				# print self.swarm[k].velocity

				self.swarm[k].updateVelocity(gBest)

				self.swarm[k].updatePosition()

				# print self.swarm[k].velocity

			#Update the personal best positions of the swarm 
			for l in range(num_particles):

				#retrieves the pBest of the swarm. 
				pBest = self.swarm[l].pBest

				#if the object's heuristic values for each particle in the swarm is less than or equal to the values for the object's personal best
				if self.calculatePiCase1(self.swarm[l].position) <= self.calculatePiCase1(pBest):

					#if the pbest of the swarm is less than or equal to the pbest of the object, then you update the position for that pbest
					self.swarm[l].pBest = self.swarm[l].position

			# print solution

		return solution 


	def optimizeCase2(self):


		for i in range(iterations):
			print "iteration", i 

			#Let the first particle arbitrarily be the global best. 
			gBest = self.swarm[0]

			#Looping through the particles in the swarm
			for j in range(num_particles):

				#Returns the pBest from the particle at position swarm[j]
				pBest = self.swarm[j].pBest 

				#if the personal best pi value is less than or equal to the global best pi value, then set the global best to that personal best
				if self.calculatePiCase2(self.swarm[j].pBest) >= self.calculatePiCase2(gBest.pBest):
					gBest = pBest

			#Once the gbest is found, then set the list Solution the same as gBest. 
			#gBest is a array/vector, same size as the dimension. 
			solution = gBest


#Once that loop is finished, it moves onto this loop, where it updates the position of each particle, before the end of the iteration


			#update position of each particle 
			for k in range(num_particles):

				#takes in the object, and in every particle in the swarm and uses the method updateVelocity, using the global best
				#Does this for updating the position as well, along with the constraints
				self.swarm[k].updateVelocity(gBest)

				self.swarm[k].updatePosition()



			#Update the personal best positions of the swarm 
			for l in range(num_particles):

				#retrieves the pBest of the swarm. 
				pBest = self.swarm[l].pBest

				#if the object's heuristic values for each particle in the swarm is less than or equal to the values for the object's personal best
				if self.calculatePiCase2(self.swarm[l].position) <= self.calculatePiCase2(pBest):

					#if the pbest of the swarm is less than or equal to the pbest of the object, then you update the position for that pbest
					self.swarm[l].pBest = self.swarm[l].position



		return solution 


#This function takes in the object, and the solution, which is basically gBest.
#Should take in the database values A and B, temperature and g_ex constants (const1 and const2)
#array argument is for what array you will be using to calculate pi. either pbest or gbest or self.swarm.[l]
#WHAT IF THERE IS MORE THAN 2 PARTICLES? HOW CAN I INPUT A 3RD
	def calculatePiCase1(self, array):

		molefraction = []

		#loops through each dimension/species and calculates the mole fraction 
		#len(array) should be the same as the dimension. 
		for i in range(len(array)):

			calcMolFrac = 1 - array[i]

			molefraction.append(calcMolFrac)

		print
		print 'array'
		print array
		print 'molefraction'
		print molefraction

		# #to calculate g_ref
		# for i in range(len(array)):

		g_ref = array[0]*300 + molefraction[0]*0

		print
		print 'gref'
		print g_ref


		#to calculate g_id
		

		summation_for_gid = (array[0] * math.log(array[0])) + (molefraction[0]*math.log(molefraction[0]))

		#once the summation is calculated, g_id = R*T the summation_for_gid

		g_id = 8.314 * 1000 * summation_for_gid
		print
		print 'gid'
		print g_id



		#to calculate g_ex 
		# summation_of_g_ex = 0 
		# for i in range(len(array)):

		g_ex = (array[0]*molefraction[0])*21000 + (array[0])*(molefraction[0]**2)*7000

		# summation_of_g_ex = g_ex + summation_of_g_ex
		print 
		print 'gex'
		print g_ex


		#to calculate the total of G
		G = g_ref + g_id + g_ex
		print
		print 'G'
		print G


		#to calculate Pi 
		#Where do you get m and b? 

		Pi = 0
		for i in range(len(array)):

			Pivalue = G - ((-251.7) * array[0] + (-259.3))

			Pi = Pivalue + Pi

		print
		print 'Pi'
		print Pi

		return 



	# def calculatePiCase2(self, array):

	# 	molefraction = []

	# 	#loops through each dimension/species and calculates the mole fraction 
	# 	#len(array) should be the same as the dimension. 
	# 	for i in range(len(array)):

	# 		calcMolFrac = 1 - array[i]

	# 		molefraction.append(calcMolFrac)



	# 	#to calculate g_ref
	# 	for i in range(len(array)):

	# 		g_ref = 



	# 	#to calculate g_id
	# 	summation_for_gid = 0 

	# 	for i in range(len(array)):

	# 		summation_for_gid = array[i] * math.log(molefraction[i])

	# 		#once the summation is calculated, g_id = R*T the summation_for_gid

	# 		g_id = 8.314 * 1000 * summation_for_gid




	# 	#to calculate g_ex 
	# 	summation_of_g_ex = 0 
	# 	for i in range(len(array)):

	# 		g_ex = array[i]*molefraction[i]*21000 + (array[i]**2)*molefraction[i]*7000

	# 		summation_of_g_ex = g_ex + summation_of_g_ex



	# 	#to calculate the total of G
	# 	G = g_ref + g_id + g_ex



	# 	#to calculate Pi 
	# 	#Where do you get m and b? 

	# 	Pi = 0
	# 	for i in range(len(array)):

	# 		Pivalue = G - ((____) * array[i] + (____))

	# 		Pi = Pivalue + Pi




	# 	return 




#Case 1 - Approach C


psi = 1 
phi_s = 2 
phi_p= 2 

dimension = 1
iterations = 4
num_particles = dimension


obj = ParticleSwarmOptimizer()

#add stopping factor later, (while loop)
obj.optimizeCase1()





# #Case 1 - Approach D

# psi = 1 
# phi_s = 2 
# phi_p= 2 

# #the number of particle changes
# dimension = 1 
# iterations = 2
# num_particles= 2*dimension


# obj = ParticleSwarmOptimizer()
# obj.optimizeCase1()






#Case 2- Approach C 






