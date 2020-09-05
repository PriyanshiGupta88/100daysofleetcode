#!/bin/python3

import os
import sys

#
# Complete the getMoneySpent function below.
#
def getMoneySpent(keyboards, drives, b):
    #
    # Write your code here.

    #
    keyboards.sort()
    drives.sort()
    if(keyboards[-1]+drives[-1]<=b):
        return(keyboards[-1]+drives[-1])
    m=0
    for i in range(len(drives)-1,-1,-1):
        for j in range(len(keyboards)-1,-1,-1):
            if(drives[i]+keyboards[j]<=b):
                c=(drives[i]+keyboards[j])
                m=max(m,c)
    if(m>0):
        return m
    else:
        return -1

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
