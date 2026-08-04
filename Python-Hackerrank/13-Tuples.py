#Python 2

n = int(raw_input())
integer_list = map(int, raw_input().split())
t= tuple(integer_list)
print(hash(t))

#Python 3

n = int(input())
numbers = input().split()
t = tuple(map(int, numbers))
print(hash(t))