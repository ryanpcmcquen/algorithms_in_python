##
## Algorithms Lesson 1: Bubblesort
## http://xoax.net/comp_sci/crs/algorithms/lessons/Lesson1/
## https://www.youtube.com/watch?v=P00xJgWzz2c
##

##
## Comparisons =
##     (n - 1) + (n - 2) + ... + 1
##     n(n - 1)/2
##     n^2/2 - n/2
##     O(n^2)
##

## Original pseudocode:
'''
for i = (n - 1) to 1
    for j = 0 to (i - 1)
        if A[j] > A[j + 1]
            swap(A[j], A[j + 1])
'''

A = [5, 9, 2, 7, 1]
n = len(A)

for i in range(n, 1, -1):
    for j in range(0, i - 1):
        if (A[j] > A[j + 1]):
            # Swap:
            A[j], A[j + 1] = A[j + 1], A[j]

print(A)

## => [1, 2, 5, 7, 9]
