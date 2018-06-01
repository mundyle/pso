
#importing random to generate the random numbers
import random 

#creating a list to store lists (columns) for access later
data = []

#for testing purposes, will be the parameters for the function PSO. 
X_p1 = 0.001  #- arrays / vector
X_p2 = 0.999  #- arrays  / vector 
VP1_m_1 = 0.002 #arrays / vector 
VP2_m_1 = -VP1_m_1 #arrays / vector 
URF = 0.1
X_s = 0.001 []
psi = 1
phi_p = 2
phi_s = 2


#for loop to add in 14 lists into the first list to create 14 columns for the 14 variables
for x in range(14):
	
	data.append([])


#setting the initial values for X1 and X2
X1 = 0 + 0.001 
X2 = 1 - X1 

#for testing purposes: appending all the initial values/parameters 
data[0].append(X1)
data[1].append(X2)
data[2].append(X_p1)
data[3].append(X_p2)
data[4].append(X_s)
data[7].append(VP1_m_1)
data[9].append(VP2_m_1)
data[13].append(URF)

#calculates the particle 1 position at current spot
def Xs(Xi,VP,URF):
	Xs_m = Xi + (VP * URF)
	return Xs_m

#calculates the velocity of particle
def VP(psi, VP_m_1, phi_p, rp, X_p, X, phi_s, rs, X_s):
	VP = (psi * VP_m_1) + (phi_p * rp * (X_p - X)) + (phi_s * rs * (X_s - X))
	return VP


popsize = 2;
iteration = 5; #for now, need to figure out the stopping factor


#This is for the iteration (should do everything within this loop before it moves onto the next iteration.
for z in range(iteration):

	#columns for each iteration
	# y[0] = particle
	# y_p[1] = best local estimate of the particles
	# y_s[2] = best position of the swarm
	# r_p[3] = first random # assigned to particles
	# r_s[4] = second random # assigned to swarm
	# Vp_m_1[5] = velocity of previous iteration
	# Vi_m[6] = current velocity of particle
	# Xm[7] = new updated current position of particle
	# URF[8] = the under relaxation factor
	# g_re[9] = the gibbs energy of reference
	# g_id[10] = the gibbs of ideal
	# g_ex[11] = gibbs external
	# G[12] = total gibb's energy
	# Pi[13] = Pi value, the difference between G and the tangent


	#this moves onto the next particle.
	for y in range(popsize):

		# This has a range of 14 because there will be 14 variables that need to be calculated per particle.
		# This is where all the calculations will be done. (longest part of the loop)
		for x in range(popsize):














			if(x == 0):
				data[x,y,z]= Xs()
			#generates random numbers for every iteration for random value of particle and random particle for the swarm
				 = random.uniform(0,1)
				data[5].append(rp)

				rs = random.uniform(0,1)
				data[6].append(rs)


				data[8].append(VP)

			#Sets the previous VP1 as the currently calculated VP1 for the next iteration. Appends this to the appropriate column.
				VP1_m_1 = VP1

				data[7].append(VP1_m_1)


			#the calculations of VP2 then append this value into the appropriate column -- VECTOR
				VP2 = (psi * VP2_m_1) + (phi_p * rp * (X_p2 - X2)) + (phi_s * rs * (X_s - X2))

				data[10].append(VP2)


			#Sets the previous VP1 as the currently calculated VP1 for the next iteration. Appends this to the appropriate column.
				VP2_m_1 = VP2

				data[9].append(VP2_m_1)




			#Calculates X1_m and appends to the appropriate column
				#X1_m = X1 + (VP1 * URF)
				Xs(X1,VP1,URF)
				data[11].append(X1_m)

			#Sets X1 (the previous value) as the current calculated one for next iteration and appends to appropriate column
				X1 = X1_m
				data[0].append(X1)

			#Calculates X2_m and appends to the appropriate column
				X2_m = X2 + (VP2 * URF)
				data[12].append(X2_m)

			#Sets X2 (the previous value) as the current calculated one for next iteration and appends to appropriate column
				X2 = X2_m
				data[1].append(X2)

				#data[x][y][z]


print data




