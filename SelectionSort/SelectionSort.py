A = ['F','I','B','O','N','A','C','C','I']

print("Unsorted Characters: ")
print(A)

print("\n")
print("Starting Selection Sort: ")

totalComparison = 0
totalSwaps = 0

curLargestPos = 0
curPointerPos = 0

for h in range(0, len(A)-1):
    curLargestPos = 0
    for i in range(1, len(A)-h):
        curPointerPos = i
        totalComparison = totalComparison + 1
        if A[curPointerPos] > A[curLargestPos]:
            curLargestPos = curPointerPos
    temp = A[len(A)-h-1]
    A[len(A)-h-1] = A[curLargestPos]
    A[curLargestPos] = temp
    totalSwaps = totalSwaps + 1
    print(A)
            

print("Selection Sort Complete")
print("\n")
        
print("Sorted Characters: ")
print(A)

print("Number of Sorted Elements: ", len(A))
print("Total Comparisons Made: ", totalComparison)
print("Total Swaps Made: ", totalSwaps)
