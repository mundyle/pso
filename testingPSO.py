
#importing random to generate the random numbers
import random 

#creating a list to store lists (columns) for access later
data = []

#for testing purposes, will be the parameters for the function PSO... from older code, don't need to look at this at the moment
# X_p1 = 0.001  #- arrays / vector
# X_p2 = 0.999  #- arrays  / vector 
# VP1_m_1 = 0.002 #arrays / vector 
# VP2_m_1 = -VP1_m_1 #arrays / vector 
# URF = 0.1
# X_s = 0.001 []
# psi = 1
# phi_p = 2
# phi_s = 2


#calculates the particle i position at current position
def X_update(Xi,VP,URF):
	X_m = Xi + (VP * URF)
	return 

#calculates the velocity of particle i 
#X_p is the best position vector for the particle and X_s = the best position vector for the swarm. 
def Vp(X1, X2, psi = 1, VP_m_1 = 0.002,  phi_p = 2, X_p1, X_p2, phi_s = 2, X_s):

	rs = random.uniform(0,1)
	rp = random.uniform(0,1)

	VP = (psi * VP_m_1) + (phi_p * rp * (X_p - X)) + (phi_s * rs * (X_s - X))


	return VP(X_p1, X_p2,VP,)


popsize = 2;
iteration = 5; #for now, need to figure out the stopping factor

def PSO(popsize = 2, iteration = 5, x1, x2, URF):

	#This is for the iteration (should do everything within this loop before it moves onto the next iteration.
	for b in range(iteration):

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
		for a in range(popsize):

			# This has a range of 19 because there will be 19 variables that need to be calculated per particle.
			# This is where all the calculations will be done. (longest part of the loop)
			Xi=0;
			VP=

			for c in range(19):

				
				if(b == 0):
					
					X1 = x1 + 0.001
					X2 = 1 - X1 
					data[0][a][0].append(X1)
					data[1][a][0].append(X2)
					

					rp = random.uniform(0,1)
					data[5][a][0].append(rp)

					rs = random.uniform(0,1)
					data[6][a][0].append(rs)



					VP1 = (psi * VP1_m_1) + (phi_p * rp * (X_p - X1)) + (phi_s * rs * (X_s - X1)
					data[8][a][0].append(VP1)

					VP1_m_1 = VP1
					data[7][a][0].append(VP1_m_1)



					VP2 = (psi * VP2_m_1) + (phi_p * rp * (X_p - X2)) + (phi_s * rs * (X_s - X2)
					data[3][a][0].append(VP2)

					VP2_m_1 = VP2 
					data[9][a][0].append(VP2)



					X1_m = X1 + (VP1*URF)
					data[11][a][0].append(X1_m)

					X1 = X1_m
					data[0][a][1].append(X1_m)					



					X2_m = X2 + (VP1*URF)
					data[12][a][1].append(X2_m)

					X2 = X2_m
					data[1][a][1].append(X2_m)


				else:

					rp = random.uniform(0,1)
					data[5][a][b].append(rp)

					rs = random.uniform(0,1)
					data[6][a][b].append(rs)



					VP1 = (psi * VP1_m_1) + (phi_p * rp * (X_p - X1)) + (phi_s * rs * (X_s - X1)
					data[2][a][b].append(VP1)

					VP1_m_1 = VP1
					data[7][a][b].append(VP1_m_1)



					VP2 = (psi * VP2_m_1) + (phi_p * rp * (X_p - X2)) + (phi_s * rs * (X_s - X2)
					data[3][a][b].append(VP2)

					VP2_m_1 = VP2 
					data[9][a][b].append(VP2)



					X1_m = X1 + (VP1*URF)
					data[11][a][b].append(X1_m)

					X1 = X1_m
					data[0][a][1+b].append(X1_m)					



					X2_m = X2 + (VP1*URF)
					data[12][a][b].append(X2_m)

					X2 = X2_m
					data[1][a][1+b].append(X2_m)


					#need to update Xp1 and xp2 






		
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




