A = ['F','I','B','O','N','A','C','C','I']

print("Unsorted Characters: ")
print(A)

print("\n")
print("Starting Bubble Sort: ")

for h in range(0, len(A)):
    sorted = True
    for i in range(0, len(A)-h-1):
        if A[i] > A[i+1]:
            sorted = False
            temp = A[i]
            A[i] = A[i+1]
            A[i+1] = temp
            print(A)
    if sorted:
        break

print("Bubble Sort Complete")
print("\n")
        
print("Sorted Characters: ")
print(A)
