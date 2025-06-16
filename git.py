

n = int(input())

# right-angled triangle pattern
for i in range(n):
    for j in range(i+1):
        print("*",end=" ")
    print()
print()
    
# horizontal pyramid pattern

for i in range(n-1):
    for j in range(i+1):
        print("*", end=" ")
    print()  # Move to the next line


for i in range(n):
    for j in range(n-i):
        print("*", end=" ")
    print()
print()

# square pattern

for i in range (n):
    for i in range (n):
        print("*", end=" ")
    print()  # Move to the next line
print()   
# piramid pattern

for i in range(n):
    for j in range(n-i-1):
        print(" ", end=" ")
    for k in range(2*i+1):
        print("*", end=" ")
    print()
    
    
    
for i in range(n):
    print(1,end=" ") 