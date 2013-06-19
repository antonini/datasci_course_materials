import MapReduce
import sys
import copy

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
  mr.emit_intermediate('multiply', record)

def reducer(key, list_of_values):
	matrixA = {}
	matrixB = {}
	matrixResult = {}

	cellsToSum = 0
	resultRows = 0
	resultCols = 0
	for record in list_of_values:
		#print type (record)
		matrixName = record[0]
		row = record[1]
		col = record[2]
		val = record[3]
		if matrixName == 'a':
			if cellsToSum < col:
				cellsToSum = col
			if resultRows < row:
				resultRows = row
			#print "ROW  %s  -  %s  -  %s"%(row, val, record)
			if row not in matrixA:
				subMatrix = {}
				matrixA[row] = subMatrix
			subMatrix = matrixA[row]
			subMatrix[col] = val
		elif matrixName == 'b':
			if resultCols < col:
				resultCols = col
			if col not in matrixB:
				subMatrix = {}
				matrixB[col] = subMatrix
			subMatrix = matrixB[col]
			subMatrix[row] = val

	# Fixing to be able to use range
	resultRows += 1
	resultCols += 1
	cellsToSum += 1

	#print "reduce  -  %s  -  %s  -  %s"%(key, matrixA, matrixB)
	for row in range(resultRows):
		for col in range(resultCols):
			rowA = matrixA[row]
			colB = matrixB[col]
			celValue = 0
			for inner in range(cellsToSum):
				if (inner in rowA and inner in colB):
					celValue += (rowA[inner] * colB[inner])

			resultObject = [row, col, celValue]
			#print "RESULT %s"%(type (resultObject))
			#mr.emit((resultObject))
			mr.emit((row, col, celValue))

			#matrixB.append(record)
  #mr.emit((key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
