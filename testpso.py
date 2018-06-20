import random
 
#These are the initial terms needed for PSO 

psi = 1 # Inertia weight to prevent velocities becoming too large
phi_s = 2 # Scaling co-efficient on the social component
phi_p= 2 # Scaling co-efficient on the cognitive component

dimension = 3 # Size of the problem
iterations = 3
num_particles= 2


class Particle:

	#each particle will have a velocity, position and best_position
	

	#The constructor for each particle 
	#Each particle will have 3 different properties: position, velocity and personal best (pBest)
	def __init__(self):

		swarm = []

		for i in range(num_particles):

			particle = []

			#This for loop, it creates random particles with random positions 
			for i in range(num_particles):

				velocity = []
				position = []
				pBest = []

				for i in range(dimension):

					#Initiating a random starting position for a particle
					#random.random() is a random number between 0 and 1
					#The random number is then appended into the array, position
					#So the particle/object will have a position vector/array property
			
					pos = 1
					position.append(pos)

					#Initiating a random velocity for a particle
					#Another random number is created, then appended into the velocity array
					#So the particle/object will have a velocity/vector array property
					vel = 2
					velocity.append(vel)


					#Initiating best position, as the current position at that dimension
					#This basically copies the position arrayinto the pBest array
					#The particle/obkect will also have a pBest propery shown as an array/vector. 
					pB = 3
					pBest.append(pB)

			particle.append(position)
			particle.append(velocity)
			particle.append(pBest)


			swarm.append(particle)

		
		

	def updatePosition(self):

		
		for i in range(1):
			# print swarm[i]
			print

			for j in range(num_particles):
			 	# print swarm[i][0]
			 	print

			 	for k in range(len(swarm[i][j])):
			 		
			 		URF = 2

			 		k = k*URF


			 		swarm[i][0][k]
			 		# print


		return


# class ParticleSwarmOptimizer:

# 	solution = []

# 	#This method takes in the particle object, with no other arguments/parameters
# 	def optimize(self):

		
# 		for i in range(iterations):
# 			print "iteration", i 

# 			#Let the first particle arbitrarily be the global best. 
# 			gBest = self.swarm[0]

# 			# print 'gBest'
# 			# print gBest
# 			# print

# 			#Looping through the particles in the swarm
# 			for j in range(num_particles):

# 				#Sets pBest 
# 				pBest = self.swarm[j].pBest 

# 				print "pBest"
# 				print pBest
# 				print

# 				# #if the personal best is less than or equal to the global best, then set the global best to that personal best
# 				# if self.calculatePi(pBest) >= self.calculatePi(gBest):
# 				# 	gBest = pBest

# 			#Once the gbest is found, then set the list Solution the same as gBest. 
# 			solution = gBest

# 		return solution


particle = Particle()
particle.updatePosition()
