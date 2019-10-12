#Function to return Most Significant Bit of the number
def getMSB(num):
    msb = 0
    while(num):
        num >>= 1;
        msb += 1
    return msb
#print(getMSB(32))

#Function to return MSB using binary logarithm
import math
def getMSBwithLn(num):
    return int(math.log2(num) + 1)
#print(getMSBwithLn(32))
