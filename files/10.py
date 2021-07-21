list = ['a','b','c', ['d','e','f'], ['g','h']]
print(list[0]) # a
print(list[3]) # ['d', 'e', 'f']
print(list[3][0]) # d
print(list[2:100000]) # ['c', ['d', 'e', 'f'], ['g', 'h']]


a = [1,2,3]
b = [4,5,6]
print(a+b) # [1, 2, 3, 4, 5, 6]

c = [1,2,3] *3
print(c) # [1, 2, 3, 1, 2, 3, 1, 2, 3]

print(1 in [1,2,3]) # True
print(100 in [1,2,3]) # False
