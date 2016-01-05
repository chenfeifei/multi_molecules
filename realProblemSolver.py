from random import *
import sys
from scipy import *


# inputFileName = sys.argv[1]
# outputFileName = sys.argv[2]

def solver(inputFileName, outputFileName):
	candidates=[]

	inputFile = open(inputFileName, 'r')
	outputFile = open(outputFileName,'w')

	numberOfVariables, numberOfPoints = inputFile.readline().split()
	targetPoints=inputFile.readline().split()

	constraintEqua1=""
	constraintEqua2=""
	# remember there is one slack variable

	# obtain candidates list
	for line in inputFile:
		candidates.append(line.split()[1:])

	# constraint: the sum of each candidate's composition percentage equals to 1; "each percentage is bigger or equal to 0."
	for i in range(1,int(numberOfVariables)+2):
		if(i == int(numberOfVariables)+1): #remember there is one slack variable
			constraintEqua1 = constraintEqua1 + " x{} = 1".format(i)
			constraintEqua2 = constraintEqua2 + " x{} >= 0".format(i)
		else:
			constraintEqua1 = constraintEqua1 + " x{} + ".format(i)
			constraintEqua2 = constraintEqua2 + " x{} >= 0,".format(i)


	constraintEqua3=""
	objectiveFunction = ""

	for i in range(0,len(targetPoints)):
		# objective function
		if(i==len(targetPoints)-1): 
			objectiveFunction = objectiveFunction + " X{} ".format(i+1)	
		else:
			objectiveFunction = objectiveFunction + " X{} + ".format(i+1)	
			
		tempEqua1 = "X{} ".format(i+1)
		tempEqua2 = "X{} ".format(i+1)
		for j in range(0,len(candidates)):
			atuple = candidates[j]
			if(j==len(candidates)-1 and float(atuple[i]) >= 0):
				tempEqua1=tempEqua1 + " - {} x{} ".format(abs(float(atuple[i])),j+1)
				tempEqua2=tempEqua2 + " + {} x{} ".format(abs(float(atuple[i])),j+1)
			elif(j==len(candidates)-2 and float(atuple[i]) < 0):
				tempEqua1=tempEqua1 + " + {} x{} ".format(abs(float(atuple[i])),j+1)
				tempEqua2=tempEqua2 + " - {} x{} ".format(abs(float(atuple[i])),j+1)
			elif(float(atuple[i]) >= 0):
				tempEqua1=tempEqua1 + " - {} x{} ".format(abs(float(atuple[i])),j+1)
				tempEqua2=tempEqua2 + " + {} x{} ".format(abs(float(atuple[i])),j+1)
			elif(float(atuple[i]) < 0):
				tempEqua1=tempEqua1 + " + {} x{} ".format(abs(float(atuple[i])),j+1)
				tempEqua2=tempEqua2 + " - {} x{} ".format(abs(float(atuple[i])),j+1)
			

		if(float(targetPoints[i])>=0):
			tempEqua1=tempEqua1 + " >= - {} ".format(abs(float(targetPoints[i])))
			tempEqua2=tempEqua2 + " >= + {} ".format(abs(float(targetPoints[i])))
		else: # targetPoints[i])<0
			tempEqua1=tempEqua1 + " >= + {} ".format(abs(float(targetPoints[i])))
			tempEqua2=tempEqua2 + " >= - {} ".format(abs(float(targetPoints[i])))

		constraintEqua3 = constraintEqua3 + tempEqua1 + "," + tempEqua2 + ","



	outputFile.write("Minimize \n")
	outputFile.write("\t objective: "+objectiveFunction + '\n')
	outputFile.write("Subject To \n")
	outputFile.write("\t constraint: "+constraintEqua1 + '\n')

	constraint3List = constraintEqua3.split(',')

	for i in range(0,len(constraint3List)-1):	
		outputFile.write("\t constraint{}: ".format(i)+constraint3List[i] + '\n')
	outputFile.write("End")

	outputFile.close()


	'''
	outputFile.write(constraint)
	outputFile.write("    minimize "+ objectiveFunction)

	outputFile.close()

	'''


# solver(inputFileName, outputFileName)

