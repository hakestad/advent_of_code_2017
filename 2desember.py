#checksum = 0
#with open("puzzle_2.txt") as puzzle:

#	for line in puzzle:
#		numberslist = [int(i) for i in line.split()]
#		diff = max(numberslist) - min(numberslist)
#		checksum += diff

#print("Checksum:", checksum)

# part 2

sum_results = 0
with open("puzzle_2.txt") as puzzle:
	for line in puzzle:
		rownumbers = [int(i) for i in line.split()]
		# keep track of whether an even division is found on this row yet
		found = False
	
		for index, divident in enumerate(rownumbers):
			for idx, divider in enumerate(rownumbers):
				# skip dividing by itself
				if (idx != index):
					leftover = divident % divider
					if (leftover == 0):
						print("Numbers found", divident, divider)
						sum_results += int(divident/divider)
						# Break out of nested loops if a value has been found to avoid unecessary computations
						found = True
						break 

print("Sum results:", sum_results)
		
