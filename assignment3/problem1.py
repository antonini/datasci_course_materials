import MapReduce
import sys

"""
Word Count Example in the Simple Python MapReduce Framework
"""

mr = MapReduce.MapReduce()

# =============================
# Do not modify above this line

def mapper(record):
    # value: document contents
    # key: document identifier
    documentKey = record[0]
    value = record[1]
    words = value.split()
    for w in words:
      # print "map - %s - %s"%(w, documentKey)
      mr.emit_intermediate(w, documentKey)

def reducer(key, list_of_values):
    result_array = list()
    for v in list_of_values:
      if v not in result_array:
        result_array.append(v)

    mr.emit((key, result_array))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
