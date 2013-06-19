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
    # value: document contents
    # key: document identifier
    recordKey = record[1]
    mr.emit_intermediate(recordKey, record)

def reducer(key, list_of_values):
  orders = list()
  itens = list()
    #result_array = list()
  for record in list_of_values:
    recordType = record[0]
    if recordType == 'order':
      orders.append(record)
    elif recordType == 'line_item':
      itens.append(record)

  for order in orders:
    for item in itens:
      line = copy.copy(order)
      for col in item:
        line.append(col)
      #print 'LINE %s '%(line)
      mr.emit((line))
    #  if v not in result_array:
    #    result_array.append(v)

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
