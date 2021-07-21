# append(), insert(), extend()
# 파괴적 함수외 비파괴적 함수: 자기 자신이 바뀌나 안바뀌나


a=[1,2,3]
a.append(4)
print(a) # [1, 2, 3, 4]
a.insert(4,1) 
print(a) # [1, 2, 3, 4, 1] --> 파괴적 함수

b=[]
b.extend([5,6,7])
b.extend([1])
print("b::", b) # [5, 6, 7, 1]


c="hello"
print(c.upper()) # HELLO
print(c) # hello --> 비파괴적 함수


d = [1,2,3,4,5,6,7]
del d[1]
print(d) # [1, 3, 4, 5, 6, 7]
del d[0:3]
print(d) # [5, 6, 7]
d.pop(1)
print(d) # [5, 7]
d.remove(7)
print(d)

