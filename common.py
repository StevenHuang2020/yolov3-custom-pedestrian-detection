#python3
#Steven common
import numpy as np


def getRowAndColumn(N):
    """give a positive number,return suitable a*b for subplot matrix """
    if N <= 0:
        return (0,0)
    if N == 1:
        return (1,1)

    if N % 2 != 0: #odd number
        N +=1

    match = []
    for i in np.arange(1,N/2+1,dtype=np.int8):
        #print(i)
        if N % i == 0:
            match.append((int(i), int(N/i)))
    #print(match)

    '''(a,b) find the minimum abs(a-b) as the suitable result'''
    minInter = abs(match[0][0]-match[0][1])
    res = match[0]
    for i in match:
        if minInter > abs(i[0]-i[1]):
            minInter = abs(i[0]-i[1])
            res = i
            
    return res[0],res[1]

def main():
    print(getRowAndColumn(78))

if __name__=='__main__':
    main()
