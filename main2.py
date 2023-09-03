import sys

max = 50

def Process(input):
    #print(int((input/max)*100))
    sys.stdout.write("\r" + str(int((input/max)*100)))
    sys.stdout.flush()
    

for i in range(10000):
    Process(i+1)