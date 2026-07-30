for i in range(5):
    for j in range(5):
        print("*", end=" ")
    print()

print("\n")

for i in range(1,6):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n")

for i in range(1,6):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

print("\n")

for i in range(1,6):
    for j in range(i):
        print(i, end=" ")
    print()

print("\n")

for i in range(5,0,-1):
    for j in range(i):
        print("*", end=" ")
    print()

print("\n")

for i in range(5,0,-1):
    for j in range(1,i+1):
        print(j, end=" ")
    print()

print("\n")
n=5

for i in range(1,n+1):

    # print spaces
    for j in range(n-i):
        print(" ",end="")

    # print stars
    for k in range(2*i-1):
        print("*", end="")
        
    print()

print("\n")
n=5

for i in range(n):

    # print spaces
    for j in range(i):
        print(" ",end="")

    # print stars
    for k in range(2*(n-i)-1):
        print("*", end="")
        
    print()

print("\n")
n=5

#upper pyramid
for i in range(1,n+1):

    # print spaces
    for j in range(n-i):
        print(" ",end="")

    # print stars
    for k in range(2*i-1):
        print("*", end="")
        
    print()

#lower pyramid
for i in range(n):

    # print spaces
    for j in range(i):
        print(" ",end="")

    # print stars
    for k in range(2*(n-i)-1):
        print("*", end="")
        
    print()

print("\n")

#increasing part
for i in range(1,6):
    for j in range(i):
        print("*",end="")
    print()

#decreasing part
for i in range(4,0,-1):
    for j in range(i):
        print("*",end="")
    print()

print("\n")
n=5

for i in range(1, n+1):

    if i % 2 == 0:
        num = 0
    else:
        num = 1

    for j in range(i):
        print(num,end=" ")

        #flip 0 to 1
        num = 1-num

    print()

print("\n")

n = 4

for i in range(1, n+1):

    # increasing numbers
    for j in range(1, i+1):
        print(j, end="")

    # spaces
    for j in range(2*(n-i)):
        print(" ", end="")

    # decreasing numbers
    for j in range(i, 0, -1):
        print(j, end="")

    print()

print("\n")

n = 5
num = 1

for i in range(1, n+1):
    for j in range(i):
        print(num, end=" ")
        num += 1
    print()

print("\n")

n = 5

for i in range(1, n+1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

print("\n")

n = 5

for i in range(n, 0, -1):
    for j in range(i):
        print(chr(65 + j), end="")
    print()

print("\n")

n = 5

for i in range(n):
    for j in range(i+1):
        print(chr(65 + i), end="")
    print()

print("\n")

n = 4

for i in range(n):
    
    # spaces
    for j in range(n-i-1):
        print(" ", end="")
        
    # increasing letters
    for j in range(i+1):
        print(chr(65 + j), end="")
        
    # decreasing letters
    for j in range(i-1, -1, -1):
        print(chr(65 + j), end="")
        
    print()

print("\n")

n = 5

for i in range(n):
         
    # letters
    for j in range(i+1):
        print(chr(65 + n - i - 1 + j), end=" ")
        
    print()

print("\n")

n = 5

# upper half
for i in range(n):
    
    # left stars
    for j in range(n-i):
        print("*", end="")
        
    # spaces
    for j in range(2*i):
        print(" ", end="")
        
    # right stars
    for j in range(n-i):
        print("*", end="")
        
    print()

# lower half
for i in range(n):
    
    # left stars
    for j in range(i+1):
        print("*", end="")
        
    # spaces
    for j in range(2*(n-i-1)):
        print(" ", end="")
        
    # right stars
    for j in range(i+1):
        print("*", end="")
        
    print()

print("\n")

n = 5

# upper half
for i in range(1, n+1):
    
    # left stars
    for j in range(i):
        print("*", end="")
        
    # spaces
    for j in range(2*(n-i)):
        print(" ", end="")
        
    # right stars
    for j in range(i):
        print("*", end="")
        
    print()

# lower half
for i in range(n-1, 0, -1):
    
    for j in range(i):
        print("*", end="")
        
    for j in range(2*(n-i)):
        print(" ", end="")
        
    for j in range(i):
        print("*", end="")
        
    print()

print("\n")

n = 4

for i in range(1, n+1):
    for j in range(1, n+1):
        
        if i == 1 or i == n or j == 1 or j == n:
            print("*", end=" ")
        else:
            print(" ", end=" ")
            
    print()

print("\n")

n = 4
size = 2*n - 1

for i in range(size):
    for j in range(size):
        
        top = i
        left = j
        bottom = size - i - 1
        right = size - j - 1
        
        val = n - min(top, left, bottom, right)
        
        print(val, end=" ")
        
    print()