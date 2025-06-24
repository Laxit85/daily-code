#User function Template for python3
#s = input()

# Your code here
#words = s.split()
capitalized_words = [word.capitalize() for word in words]
capitalized_line = " ".join(capitalized_words)
count = len(words)
print(capitalized_line)
print(count)

def alphabet_triangle(n):
    for i in range(n):
        for j in range(i+1):
            print(chr(65 + j), end=' ')
        print()

#sum of eliments present in tuple

def n_sum(*elements):
    a = 0
    for i in elements:
        a += i
    return a



def print_details(**details):
    for key, value in details.items():
        print(f"{key} is {value}")


# Examples of calling the function with different numbers of keyword arguments
print_details(ID=101, name="ABC", price=100)
print_details(ID=102, name="XYZ")

#find palendrom


def fun():
    n = input()
    n = n.upper() #for convertin full string to upper case
    rev = ""
    for i in n:
        rev = i + rev #reversing the string
    if rev == n:
        print("True")
    else:
        print("False")

fun() # calling the function
