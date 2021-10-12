previous = 0
nextVal = 0

while(nextVal < 50):
  print(nextVal)
  nextVal = nextVal + previous
  previous = nextVal - previous
  if(nextVal == 0):
    nextVal = nextVal + 1
