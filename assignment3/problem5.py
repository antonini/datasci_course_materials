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
  dna = record[1]
  dna = dna[:-10]
  mr.emit_intermediate(dna, 1)

def reducer(key, list_of_values):
  mr.emit((key))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
