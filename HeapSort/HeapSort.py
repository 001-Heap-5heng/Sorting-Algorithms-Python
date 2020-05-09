'''
Max-Heap

Given: A[i]

i = 0              <- Root
floor((i-1)/2)     <- Parent of i
((i+1) * 2) - 1    <- Left Child of i
((i+1) * 2)        <- Right Child of i

'''

A = ['F','I','B','O','N','A','C','C','I']

print("Unsorted Characters: ")
print(A)

print("\n")
print("Starting Heap Sort: ")

totalComparison = 0
totalSwaps = 0

def heapSort(a=[]):
    global totalComparison
    global totalSwaps

    lastParent = (len(a)-2)//2
    if lastParent < 0:
        return a

    print("------------------------")
    print("Step1: Building Max Heap")
    print("------------------------")
    for mainParent in range(lastParent, -1, -1):
        curParent = mainParent
        while True:
            print(a)
            totalComparison = totalComparison + 1
            if (len(a)-1) < (((curParent+1) * 2) - 1):  #Left Child is Missing (not a parent)
                print("Leaf at index ", curParent)
                break
            elif (len(a)-1) < (((curParent+1) * 2)):                   #Right Child is Missing (parent with 1 child)
                totalComparison = totalComparison + 1
                totalComparison = totalComparison + 1
                if a[((curParent+1) * 2) - 1] > a[curParent]:          #Left Child larger than Parent
                    totalSwaps = totalSwaps + 1
                    temp = a[((curParent+1) * 2) - 1]
                    a[((curParent+1) * 2) - 1] = a[curParent]
                    a[curParent] = temp
                    print("Swap Larger Left Child of index ", curParent)
                break
            else:
                totalComparison = totalComparison + 1
                if a[((curParent+1) * 2)] > a[((curParent+1) * 2) - 1]:#Right Child larger than Left Child
                    totalComparison = totalComparison + 1
                    if a[((curParent+1) * 2)] > a[curParent]:          #Right Child larger than Parent
                        totalSwaps = totalSwaps + 1
                        temp = a[((curParent+1) * 2)]
                        a[((curParent+1) * 2)] = a[curParent]
                        a[curParent] = temp
                        print("Swap Larger Right Child of index ", curParent)
                        curParent = ((curParent+1) * 2)
                    else:
                        print("No need Swap Right Child of index ", curParent)
                        break
                else:                                                  #Left Child larger than Right Child
                    totalComparison = totalComparison + 1
                    if a[((curParent+1) * 2) - 1] > a[curParent]:      #Left Child larger than Parent
                        totalSwaps = totalSwaps + 1
                        temp = a[((curParent+1) * 2) - 1]
                        a[((curParent+1) * 2) - 1] = a[curParent]
                        a[curParent] = temp
                        print("Swap Larger Left Child of index ", curParent)
                        curParent = ((curParent+1) * 2) - 1
                    else:
                        print("No need Swap Left Child of index ", curParent)
                        break

    print("------------------------------------")
    print("Step2: Recursive Removal of Max Heap")
    print("------------------------------------")
    for lengthA in range(len(a)-1, 0, -1):
        print("Remove the Max Root")
        temp = a[0]
        a[0] = a [lengthA]
        a[lengthA] = temp
        
        curParent = 0
        while True:
            print(a)
            totalComparison = totalComparison + 1
            if (lengthA-1) < (((curParent+1) * 2) - 1):  #Left Child is Missing (not a parent)
                print("Leaf at index ", curParent)
                break
            elif (lengthA-1) < (((curParent+1) * 2)):                  #Right Child is Missing (parent with 1 child)
                totalComparison = totalComparison + 1
                totalComparison = totalComparison + 1
                if a[((curParent+1) * 2) - 1] > a[curParent]:          #Left Child larger than Parent
                    totalSwaps = totalSwaps + 1
                    temp = a[((curParent+1) * 2) - 1]
                    a[((curParent+1) * 2) - 1] = a[curParent]
                    a[curParent] = temp
                    print("Swap Larger Left Child of index ", curParent)
                break
            else:
                totalComparison = totalComparison + 1
                if a[((curParent+1) * 2)] > a[((curParent+1) * 2) - 1]:#Right Child larger than Left Child
                    totalComparison = totalComparison + 1
                    if a[((curParent+1) * 2)] > a[curParent]:          #Right Child larger than Parent
                        totalSwaps = totalSwaps + 1
                        temp = a[((curParent+1) * 2)]
                        a[((curParent+1) * 2)] = a[curParent]
                        a[curParent] = temp
                        print("Swap Larger Right Child of index ", curParent)
                        curParent = ((curParent+1) * 2)
                    else:
                        print("No need Swap Right Child of index ", curParent)
                        break
                else:                                                  #Left Child larger than Right Child
                    totalComparison = totalComparison + 1
                    if a[((curParent+1) * 2) - 1] > a[curParent]:      #Left Child larger than Parent
                        totalSwaps = totalSwaps + 1
                        temp = a[((curParent+1) * 2) - 1]
                        a[((curParent+1) * 2) - 1] = a[curParent]
                        a[curParent] = temp
                        print("Swap Larger Left Child of index ", curParent)
                        curParent = ((curParent+1) * 2) - 1
                    else:
                        print("No need Swap Left Child of index ", curParent)
                        break
    return a
    
A = heapSort(A)

print("Heap Sort Complete")
print("\n")
        
print("Sorted Characters: ")
print(A)

print("Number of Sorted Elements: ", len(A))
print("Total Comparisons Made: ", totalComparison)
print("Total Swaps Made: ", totalSwaps)
