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
    friendA = record[0]
    friendB = record[1]
    mr.emit_intermediate(friendA, friendB)

def reducer(key, list_of_values):

  friends = list()
  for friend in list_of_values:
    if friend not in friends:
      friends.append(friend)
  #print "reduce - %s   -   %s"%(key, friends)
  mr.emit((key, len(friends)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
