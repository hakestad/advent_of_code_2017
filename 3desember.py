puzzleinput = 368078

layerNum = 0
numbersPlaced = 1
n = 1

coordX = 0
coordY = 0

while numbersPlaced <= puzzleinput:
	nextN = n + 2
	layerNum += 1

	numbersInSquare = nextN**2
	numbersInLayer = numbersInSquare - (n**2)
	positionsPerSide = nextN - 1 # Will be 1 less than each side, as two of the positions will belong to two sides

	# For current layer
	startNum = numbersPlaced + 1
	stopNum = startNum + numbersInLayer

	if (startNum <= puzzleinput <= stopNum):
		# We now  know which layer the puzzleinput is located at
		# So we can check to see at what position within the layer it is
	 	
		# One of the coords will always be the same as the current layer number
		# Doesn't matter which one of the coords it is, because the distance will be the same around the sqared cirle
		coordX = layerNum

		pos = puzzleinput - startNum + 1
		posInSide = pos % positionsPerSide
		coordY = abs(layerNum - posInSide)

		# Break out of loop when result is found
		break
					
	numbersPlaced += numbersInLayer
	n = nextN

print("Coords:", coordX, coordY)

returnCoords = [0, 0]
puzzleCoords = [coordX, coordY]
manhattanDistance = abs(puzzleCoords[0] - returnCoords[0]) + abs(puzzleCoords[1] - returnCoords[1])
print("Manhattan distance:", manhattanDistance)

# Part 2

dimensions = 30
coordinates = []
# setup coordinate system
for i in range(0, dimensions):
	coordinates.append([])
	for j in range(0, dimensions):
		coordinates[i].append(0)

currentX = int(dimensions / 2)
currentY = int(dimensions / 2)
coordinates[currentX][currentY] = 1

def getSurroundingValues(currX, currY):
	value = 0
	value += coordinates[currX + 1][currY]
	value += coordinates[currX + 1][currY + 1]
	value += coordinates[currX][currY + 1]
	value += coordinates[currX - 1][currY + 1]
	value += coordinates[currX - 1][currY]
	value += coordinates[currX - 1][currY - 1]
	value += coordinates[currX][currY - 1]
	value += coordinates[currX + 1][currY - 1]
	return value

values = [1]
n = 1
while values[len(values)-1] < puzzleinput:
	newN = n + 2
	numzPerSquare = newN**2
	numzPerLayer = numzPerSquare - (n**2)
	numzPerSide = newN - 1 #int(numzPerLayer / newN)
	print("nums per side", numzPerSide)
	print("nums per layer", numzPerLayer)
	
	currentSide = 1

	for m in range(0, int(numzPerLayer / numzPerSide)):
		if (currentSide == 1):
			currentX += 1
		elif(currentSide == 2):
			currentX -= 1
			currentY -= numzPerSide - 1
		elif (currentSide == 3):
			currentX -= numzPerSide - 1
			currentY += 1
		elif (currentSide == 4):
			currentY += numzPerSide - 1
			currentX += 1

		for q in range(0, numzPerSide):
			if (currentSide == 1):
				res = getSurroundingValues(currentX, currentY - q)
				coordinates[currentX][currentY - q] = res
				values.append(res)
			elif (currentSide == 2):
				res = getSurroundingValues(currentX - q, currentY)
				coordinates[currentX - q][currentY] = res
				values.append(res)
			elif (currentSide == 3):
				res = getSurroundingValues(currentX, currentY + q)
				coordinates[currentX][currentY + q] = res
				values.append(res)
			else:
				res = getSurroundingValues(currentX + q, currentY)
				coordinates[currentX + q][currentY] = res
				values.append(res)
			if (values[len(values) - 1] > puzzleinput):
				break
			
		currentSide += 1
		
		if (values[len(values) - 1] > puzzleinput):
			print("VALUE:", values[len(values) - 1], "is the first value larger than puzzle input")
			break

	currentX += numzPerSide - 1
	n = newN
	print(values)


	
