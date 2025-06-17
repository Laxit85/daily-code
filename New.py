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

