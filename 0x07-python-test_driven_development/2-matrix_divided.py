#!/usr/bin/python3

"""a function that divides all elements of a matrix."""

def matrix_divided(matrix, div):
	"""
	divides all elements of a matrix and return new matrix

	args:
		matrix (list): matrix of two  dimensional array
		div (int or float): element that divide each element of the list

	Raises:
		TypeError:
			matrix must be a matrix (list of lists) of integers/floats
			Each row of the matrix must have the same size
			div must be a number
		ZeroDivisionError:
			zero division error

	"""
	if (not isinstance(matrix, list) or matrix == [] or not all(isinstance(row, list) for row in matrix)
	or not all(isinstance(element, int) or isinstance(element, float) for element in [num for row in matrix for num in row])):
		raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

	if (not all(len(row) == len(matrix[0]) for row in matrix)):
		raise TypeError("Each row of the matrix must have the same size")

	if (not isinstance(div, int) and not isinstance(div, float)):
		raise TypeError("div must be a number")

	if (div == 0):
		raise ZeroDivisionError("division by zero")

	return ([[round(num / div, 2) for num in row] for row in matrix])




