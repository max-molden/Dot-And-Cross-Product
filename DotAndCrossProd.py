# cross product and dot prodcut calc

def main():
	# info for user
	print('\n')
	delim = '*'
	num_delim = 75
	print(num_delim * delim)

	print("The following is a list of supported operations.\n")
	print("1.\tDot Product\n2.\tCross Product\n3.\tBoth\n")
	print("If you wish to perform a cross product, your vector must be of length 3.")

	print(num_delim * delim + "\n")

	# get op choice, size of vects, and sees if cross prod possible (robustly)
	choice = getOp()
	size = getLens()
	valid_cross_prod = validCrossProd(size, choice)

	while not (valid_cross_prod):
		choice = getOp()
		size = getLens()
		valid_cross_prod = validCrossProd(size, choice)

	# get vectors
	vector1 = getVect(size, "first")
	vector2 = getVect(size, "second")

	# call output func
	displaying = printRes(choice, vector1, vector2, size)
	print(displaying)


'''
gets from the user the number of the operation they would like to perform
input: none
output: int (number of operation to perform)
processing: robust check with while loop, operation must be 1, 2, or 3. return to func call
'''
def getOp():
	op = int(input("Please enter the number of the operation you would like to perform from the list. "))
	while not ((op == 1) | (op == 2) | (op == 3)):
		print("\nInvalid selection.")
		op = int(input("Please enter one the number of the operation you would like to perform from the list. "))

	return op

'''
gets the lengths of the vectors on which operations will be performed
input: none
output int(length of the 2 vectors), only need one because they are forced to be equal
processing: robust checks with while loops that each length is at least 1. robust checks that lens are equal. return to func call
'''
def getLens():
	len1 = int(input("\nPlease enter the length of the first vector: "))
	while not (len1 > 0):
		print("\nError: Vector must have length of at least 1.")
		len1 = int(input("\nPlease enter the length of the first vector: "))

	len2 = int(input("Please enter the length of the second vector: "))
	while not (len2 > 0):
		print("\nError: Vector must have length of at least 1.")
		len2 = int(input("Please enter the length of the second vector: "))

	while not (len1 == len2):
		print("\nError: Vector dimensions must agree")
		len1 = int(input("Please enter the length of the first vector: "))
		while not (len1 > 0):
			print("\nError: Vector must have length of at least 1.")
			len1 = int(input("\nPlease enter the length of the first vector: "))
		len2 = int(input("Please enter the length of the second vector: "))
		while not (len2 > 0):
			print("\nError: Vector must have length of at least 1.")
			len2 = int(input("Please enter the length of the second vector: "))

	return len1

'''
validates if cross product is possible: this program only supports cross products with 2 vectors each of length 3
input: int (length of one of the vectors (at this point they are already validated to be equal)), int (operation num)
output: bool
processing: if the dimension of the vectors is 3 but the operation chosen is to perform a cross prod or a cross and dot prod then false is returned,
			else: ok.  return to func call.  if false is returned the user will be asked to re enter all info until true is returned
'''
def validCrossProd(dim, operation):
	if (dim != 3) & ((operation == 2) | (operation == 3)):
		print("\nError: This program only supports 3-Dimensional cross products.\n")
		return False
	else:
		return True

'''
gets the two vectors and stores as arrays
input: int (size of the vectors), str (first or second vector )
output: list (acts as vector, contains all elements entered by user)
processing: gets each element one by one. gets first separately so message can make sense, gets rest except last so message makes sense, gets last
			last so message can make sense.  all elements stored in list. return to func call
'''
def getVect(dimension, which):
	vect = []

	vect.append(float(input(f"\nEnter the first component of the {which} vector: ")))
	for element in range(1, dimension - 1):
		vect.append(float(input(f"Enter the next component of the {which} vector: ")))
	vect.append(float(input(f"Enter the last component of the {which} vector: ")))

	return vect

'''
function to calculate the cross product and display correct signs (-/+) of operations
input: list (the two vectors)
output: str (3 strings containing various information about calculating the cross product at different stages of math/completion and the final vector in the form x*i+y*j+z*k)
processing: creates the initial string and uses selecction structure to append next work with correct signage (+/-). no need to use a for-loop as there will always only be 3 elements
'''
def crossProd(arr1, arr2):
	work_str = f"(({arr1[1]} * {arr2[2]}) - ({arr1[2]} * {arr2[1]}))i - (({arr1[0]} * {arr2[2]}) - ({arr1[2]} * {arr2[0]}))j + (({arr1[0]} * {arr2[1]}) - ({arr1[1]} * {arr2[0]}))k "
	next_work_str = f"({arr1[1]*arr2[2]} - {arr1[2]*arr2[1]})i - ({arr1[0]*arr2[2]} - {arr1[2]*arr2[0]})j + ({arr1[0]*arr2[1]} - {arr1[1]*arr2[0]})k"

	last_str = f"{arr1[1]*arr2[2] - arr1[2]*arr2[1]}i"
	if (arr1[0]*arr2[2] - arr1[2]*arr2[0]) >= 0:
		last_str += f" - {arr1[0]*arr2[2] - arr1[2]*arr2[0]}j"
	else:
		last_str += f" + {abs(arr1[0]*arr2[2] - arr1[2]*arr2[0])}j"

	if (arr1[0]*arr2[1] - arr1[1]*arr2[0]) >= 0:
		last_str += f" + {arr1[0]*arr2[1] - arr1[1]*arr2[0]}k"
	else:
		last_str += f" - {abs(arr1[0]*arr2[1] - arr1[1]*arr2[0])}k"

	return work_str, next_work_str, last_str

'''
calculates the dot product as well as creates a string to display the products and sums to show the user the work being done
input: list(the two vectors), int(the length of the vectors (just one, its the same for both))
output: the dotproduct (a sum) and two strings representing the mathematical work that is done
processing: instantiates the cumulaitve sum and resultant/work string to empty. multiplies the first component of each vector together and then the 
			rest in a for loop. it is done separatelty to make concatenating the string easier due to the plus sign, see value for res_str inside for loop
'''
def dotProd(vect1, vect2, length):
	cum_sum = vect1[0] * vect2[0]
	res_str = f"({vect1[0]} * {vect2[0]})"
	work_str = f"{vect1[0] * vect2[0]}"

	for i in range(1, length):
		cum_sum += vect1[i] * vect2[i]
		res_str += f" + ({vect1[i]} * {vect2[i]})"
		if (vect1[i] * vect2[i]) < 0:
			work_str += f" - {abs(vect1[i] * vect2[i])}"
		else:
			work_str += f" + {vect1[i] * vect2[i]}"


	return cum_sum, res_str, work_str

'''
takes the vector info and creates the correct information to display
input: int(pick of op), list (two vectors) int(length)
output: returns back the correct value of output var which contains the info that should be displayed to the user
processing: uses selection structure based on op choice, calls upon dotProd() and crossProd() where appropriate
'''
def printRes(pick, v1, v2, lngth):
	if pick == 1:
		dot_sum, dot_str, dot_work = dotProd(v1, v2, lngth)
		output = f"\nPerforming the dot product on the two vectors {__str__(v1, lngth)} and {__str__(v2, lngth)} gives:\n\t{dot_str}\
			\n\tWhich simplifies to: {dot_work}\n\tWhich evaluates to: {dot_sum}."
	elif pick == 2:
		cross_first, cross_second, cross_last = crossProd(v1, v2)
		output = f"\nPerforming the cross product on the two vectors {__str__(v1, lngth)} and {__str__(v2, lngth)} gives:\n\t{cross_first}\
			\n\tWhich simplifies to: {cross_second}\n\tWhich evaluates to the vector: {cross_last}"
	else:
		output = printRes(1, v1, v2, lngth) + "\n\n" + printRes(2, v1, v2, lngth)

	return output

def __str__(array, end):
	return [array[i] for i in range(end)]

'''
Pythonic implementation of a "do-while loop"
'''
while True:
	main()
	again = input("Would you like to performm another operation (y/n)? ")

	# add another if to ask about properties then call on func for displaying them

	if not ((again == 'y') | (again == 'Y')):
		break


'''
good start but later can add functionality to ask user if they want to see properties about their vectors
such as: when they are perpendicular etc.
'''
