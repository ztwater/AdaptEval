#!/bin/pypy
#
# TH @stackoverflow, 2016-01-20, linear time "median of medians" algorithm
#
import sys, random


items_per_column = 15


def find_i_th_smallest( A, i ):
    t = len(A)
    if(t <= items_per_column):
        # if A is a small list with less than items_per_column items, then:
        #
        # 1. do sort on A
        # 2. find i-th smallest item of A
        #
        return sorted(A)[i]
    else:
        # 1. partition A into columns of k items each. k is odd, say 5.
        # 2. find the median of every column
        # 3. put all medians in a new list, say, B
        #
        B = [ find_i_th_smallest(k, (len(k) - 1)/2) for k in [A[j:(j + items_per_column)] for j in range(0,len(A),items_per_column)]]

        # 4. find M, the median of B
        #
        M = find_i_th_smallest(B, (len(B) - 1)/2)


        # 5. split A into 3 parts by M, { < M }, { == M }, and { > M }
        # 6. find which above set has A's i-th smallest, recursively.
        #
        P1 = [ j for j in A if j < M ]
        if(i < len(P1)):
            return find_i_th_smallest( P1, i)
        P3 = [ j for j in A if j > M ]
        L3 = len(P3)
        if(i < (t - L3)):
            return M
        return find_i_th_smallest( P3, i - (t - L3))


# How many numbers should be randomly generated for testing?
#
number_of_numbers = int(sys.argv[1])


# create a list of random positive integers
#
L = [ random.randint(0, number_of_numbers) for i in range(0, number_of_numbers) ]


# Show the original list
#
# print L


# This is for validation
#
# print sorted(L)[int((len(L) - 1)/2)]


# This is the result of the "median of medians" function.
# Its result should be the same as the above.
#
print find_i_th_smallest( L, (len(L) - 1) / 2)
