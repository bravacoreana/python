# format()
print("".format(1,2,3)) # nothing
print("{} {} {} {}".format(1,2,3,4)) # 1 2 3 4
print("{}년 {}월 {}일 {}요일".format(2021,7,20,"화")) # 2021년 7월 20일 화요일

# upper() & lower()
print("Hello".upper()) # HELLO
print("Hello".lower()) # hello

# strip()
print(" abc de   ".strip()) # abc de
print(" abc de   ".lstrip()) # abc de
print(" abc de   ".rstrip()) #  abc de

# find() : 왼쪽부터 찾아 처음 나오는 인덱스
print("abcde-abcde".find("d")) # 3
print("abcde".find("z")) # -1

# rfind() : 찾고자 하는 값이 중복일 때 가장 오른쪽에 있는 것이 우선
print("abcde-abcde".rfind("d")) # 9 

# in : 연산자임
print("a" in "abcde") # True
print("z" in "abcde") # False

# split
print("10 20 30 40 50".split(" ")) # ['10', '20', '30', '40', '50']
print("10,20,30,40,50".split(" ")) # ['10,20,30,40,50']
print("10,20,30,40,50".split(",")) # ['10', '20', '30', '40', '50']
