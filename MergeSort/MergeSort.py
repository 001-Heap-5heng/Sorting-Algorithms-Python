A = ['F','I','B','O','N','A','C','C','I']

print("Unsorted Characters: ")
print(A)

print("\n")
print("Starting Merge Sort: ")

totalComparison = 0
totalSwaps = 0

def mergeSort(a=[]):
    global totalComparison
    global totalSwaps
    b = []
    c = []
    totalComparison = totalComparison + 1
    if len(a) <= 1:
        return a
    else:
        print("Divide: ", a)
        b = mergeSort(a[:(len(a)//2)])
        c = mergeSort(a[(len(a)//2):])

    print("Conquer: ", b, " and ", c)
    d = []
    while True:
        totalComparison = totalComparison + 2
        if len(b) == 0:
            totalComparison = totalComparison - 1
            d.extend(c)
            totalSwaps = totalSwaps + 1
            break
        elif len(c) == 0:
            d.extend(b)
            totalSwaps = totalSwaps + 1
            break

        totalComparison = totalComparison + 1
        if b[0] < c[0]:
            d.append(b.pop(0))
        else:
            d.append(c.pop(0))
        totalSwaps = totalSwaps + 1
        print(d)
    print(d)
    print("Return: ", d)
    return d

A = mergeSort(A)

print("Merge Sort Complete")
print("\n")
        
print("Sorted Characters: ")
print(A)

print("Number of Sorted Elements: ", len(A))
print("Total Comparisons Made: ", totalComparison)
print("Total Swaps Made: ", totalSwaps)
