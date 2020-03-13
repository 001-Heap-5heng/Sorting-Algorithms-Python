A = ['F','I','B','O','N','A','C','C','I']

print("Unsorted Characters: ")
print(A)

print("\n")
print("Starting Quick Sort: ")

totalComparison = 0
totalSwaps = 0

def quickSort(a=[]):
    global totalComparison
    global totalSwaps

    pivotPos = len(a)//2
    pivotVal = a[pivotPos]
    b = []
    c = []

    print("Enter: ", a)
    print("Pivot: ", a[:pivotPos], pivotVal, a[pivotPos+1:])
    while len(a)-1 > pivotPos:
        tempA = a.pop(pivotPos+1)
        totalComparison = totalComparison + 1
        if tempA >= pivotVal:
            c.append(tempA)
        else:
            b.append(tempA)
        totalSwaps = totalSwaps + 1

    a.pop()
    totalSwaps = totalSwaps + 1

    while len(a) > 0:
        tempA = a.pop(0)
        totalComparison = totalComparison + 1
        if tempA > pivotVal:
            c.append(tempA)
        else:
            b.append(tempA)
        totalSwaps = totalSwaps + 1

    print("Split: ", b, pivotVal, c)

    totalComparison = totalComparison + 1
    if len(b) > 1:
        b = quickSort(b)
    totalComparison = totalComparison + 1
    if len(c) > 1:
        c = quickSort(c)

    totalSwaps = totalSwaps + 2
    b.append(pivotVal)
    b.extend(c)
    print("Return: ", b)
    return b

A = quickSort(A)

print("Quick Sort Complete")
print("\n")
        
print("Sorted Characters: ")
print(A)

print("Number of Sorted Elements: ", len(A))
print("Total Comparisons Made: ", totalComparison)
print("Total Swaps Made: ", totalSwaps)
