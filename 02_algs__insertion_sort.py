##
## Algorithms Lesson 2: Insertion Sort
## http://xoax.net/comp_sci/crs/algorithms/lessons/Lesson2/
## https://www.youtube.com/watch?v=c4BRHC7kTaQ
##

##
## Comparisons =
##

## Original pseudocode:
'''
for i = 1 to n - 1
    j = i
    while j > 0 and A[j] < A[j - 1]
        swap(A[j], A[j - 1])
        j = j - 1
'''

A = [24, 13, 9, 64, 7, 23, 34, 47]
n = len(A)

for i in range(1, n):
    j = i
    while j > 0 and A[j] < A[j - 1]:
        # Swap:
        A[j], A[j - 1] = A[j - 1], A[j]
        j = j - 1

print(A)

## => [7, 9, 13, 23, 24, 34, 47, 64]
