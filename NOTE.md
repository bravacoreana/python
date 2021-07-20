# 문자

```python
# 문자열 연산자
print("a" + "b") # ab
print("a" * 3 ) # aaa
print("bilbo"[0]) # b0

# 문자 선택 연산자
print("hello"[0]) # h
print("hello"[4]) # o
print("hello"[-0]) # h
print("hello"[-1]) # o
print("hello"[-5]) # h

# 문자열 범위 선택 연산자
print("hello"[0:1]) # h
print("hello"[:4]) # hell
print("abcde"[-2:-1]) # d

# 문자열 길이 구하기
print(len("abcde")) #5
```

# 숫자

1. 숫자의 종류
   - 소수점이 없는 숫자 (정수) - Integer: 1, 2, 3
   - 소수점이 있는 숫자 (실수) - Floating point: 22.342, 2.123, 2.0
   - 존재하지 않는 수 (허수) - 10 + 1j
2. 숫자에 적용하는 연산자: +, -, \*, /, \*\*(power), %(remainder), //(quotient)

# 변수와 입력

```python
pi = 3.14
print(pi) # 3.14

a = input("tell me sth >>> ")
print(a)
print(type(a))
# input() 함수의 결과는 string
```

# 문자열 변환

```python
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
```

# boolean

```python
# 비교 연산자

print(10 == 100) # False
print(10 != 100) # True
print(10 > 100) # False
print(10 < 100) # True
print(10 >= 100) # False
print(10 <= 100) # True

x = 20
print(10 < x < 20) # False
print(10 < x < 100) # True


# 단항 연산자
not True
not False

# 이항 연산자
True and True # True
True and False # False
False and True # False
False and False # False

True and True # True
True and False # True
False and True # True
False and False # False
```

# if

```python
# if <condition> :
    # when condition is true
```
