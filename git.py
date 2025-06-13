
# right-angled triangle pattern
n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
    
    
# horizontal pyramid pattern
n1 = int(input()) 

for i in range(n-1):
    for j in range(i+1):
        print("*", end=" ")
    print()  # Move to the next line
    
for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()