##
## Algorithms Lesson 3: Merge Sort
## http://xoax.net/comp_sci/crs/algorithms/lessons/Lesson3/
## https://www.youtube.com/watch?v=GCae1WNvnZM
##

##
## Comparisons =
##

## Original pseudocode:
'''
Merge(A, end1, end2)
    i = 0, j = end1, k = 0
    while i < end1 and j < end2
        if(A[i] < A[j])
            temp[k] = A[i]
            i = i + 1, k = k + 1
        else
            temp[k] = A[j]
            j = j + 1, k = k + 1
    while i < end1
        temp[k] = A[i]
        i = i + 1, k = k + 1
    while j < end2
        temp[k] = A[j]
        j = j + 1, k = k + 1
    for (i = 0; i < end2; i++)
        A[i] = temp[i]


for i = 1; i < size; i = 2i
    for j = 0; j < size - i; j = j + 2i
        Merge(&A[j], i, min(2i, size - j))
'''

A = [24, 13, 9, 64, 7, 23, 34, 47]

