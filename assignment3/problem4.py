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
    friendObject = ['friend', friendB]
    checkObject = ['check', friendA]

    mr.emit_intermediate(friendA, friendObject)
    mr.emit_intermediate(friendB, checkObject)

def reducer(key, list_of_values):

  friends = list()
  checks = list()
  emited = list()
  for obj in list_of_values:
    objType = obj[0]
    frindName = obj[1]
    if objType == 'friend':
      if frindName not in friends:
        friends.append(frindName)
    elif objType == 'check':
      if frindName not in checks:
        checks.append(frindName)

  for friend in friends:
    if friend not in checks and friend not in emited:
      emited.append(friend)
      mr.emit((key, friend))

  for friend in checks:
    if friend not in friends and friend not in emited:
      emited.append(friend)
      mr.emit((key, friend))

  #print "reduce  -  %s  -  %s  -   %s"%(key, friends, checks)

  #print "reduce - %s   -   %s"%(key, friends)
  #mr.emit((key, len(friends)))

# Do not modify below this line
# =============================
if __name__ == '__main__':
  inputdata = open(sys.argv[1])
  mr.execute(inputdata, mapper, reducer)
