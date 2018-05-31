#This is the code for calculating Pi
#This will eventually be a function to be used, but for testing purposes, I will add def later. 

from decimal import Decimal
import math

#def piCalc(g_A, g_B, temp):

#Creating a list for the data to be stored 

data = []

#For testing purposes
g_A = 0 
g_B = 300 
temp = 1000

#Creating the necessary lists within data to store variables 

for x in range(7):
	
	data.append([])

#Defining initial value of mole fractions of X and Y

X = 0 
Y = 1 

#Calculations for every mole fraction possible and appending them into the list 

while (X < 1 and Y > 0):

	#Getting the mole fractions of X and Y
	X = X + 0.01
	X = round(X,2)
	data[0].append(X)

	Y = 1-X 
	Y = round(Y,2)
	data[1].append(Y)

	g_ref = (X * g_B) + (Y * g_A)
	g_ref = round(g_ref,2)
	data[2].append(g_ref)

	# print Y
	# print math.log(Y)
	# print X
	# print math.log(X)
	
	# print 

	# g_id = 8.314 * temp * (X * (2.3025 * math.log(X)) + (Y * 2.3025 * math.log(Y)))
	# g_id = round(g_id, 2)
	# data[3].append(g_id)

	


	

print data

print 








