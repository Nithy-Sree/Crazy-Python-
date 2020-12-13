#SortingBasedOnUnitDigits

n=int(input("Enter the number of elements: "))
x=list(map(int, input("Enter the n elements with space: ").split()[:n]))

# a list to store sorted numbers
soted_array=[]

# iterating through the digits 0 to 9
for i in range(0, 10):
    l=[]
    for j in x:
        if j%10 == i:
            l.append(j)
    # if there are two numbers with same unit digits
    # sorting it using sort method
    l.sort()
    soted_array+=l

print(soted_array)
