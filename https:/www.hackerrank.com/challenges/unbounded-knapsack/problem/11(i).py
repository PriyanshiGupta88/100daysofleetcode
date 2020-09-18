#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the unboundedKnapsack function below.
def unboundedKnapsack(k, arr):
    t=[[0 for i in range(k+1)] for j in range(len(arr)+1)] 
    for i in range(1,len(arr)+1):
        for j in range(1,k+1):
            if(arr[i-1]<=j):
                t[i][j]=max((arr[i-1]+t[i][j-arr[i-1]]),t[i-1][j])
            else:
                t[i][j]=t[i-1][j]
    return t[len(arr)][k]
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    t = int(input())
    for i in range(t):

        nk = input().split()

        n = int(nk[0])

        k = int(nk[1])

        arr = list(map(int, input().rstrip().split()))

        result = unboundedKnapsack(k, arr)

        fptr.write(str(result) + '\n')

    fptr.close()
