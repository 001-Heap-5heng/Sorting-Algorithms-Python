A = ['F','I','B','O','N','A','C','C','I']

print("Unsorted Characters: ")
print(A)

print("\n")
print("Starting Insertion Sort: ")

totalComparison = 0
totalSwaps = 0

for h in reversed(range(0, len(A)-1)):
    for i in range(h, len(A)-1):
        totalComparison = totalComparison + 1
        if A[i] > A[i+1]:
            temp = A[i]
            A[i] = A[i+1]
            A[i+1] = temp
            totalSwaps = totalSwaps + 1
            print(A)
        else:
            break

print("Insertion Sort Complete")
print("\n")
        
print("Sorted Characters: ")
print(A)

print("Number of Sorted Elements: ", len(A))
print("Total Comparisons Made: ", totalComparison)
print("Total Swaps Made: ", totalSwaps)
