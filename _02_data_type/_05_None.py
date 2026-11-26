""" None
- 값이 없음을 나타내는 객체
- 자료형은 NoneType
- 다른 객체 지향 언어의 null과 같은 의미
"""

a = None
print(f"a: {a} - {type(a)}")
# a: None - <class 'NoneType'>

b = "파이썬"
print(f"b: {b} - {type(b)}")

# b 변수에 값이 있었으나, 없는 상태로 만든 것을 명시
b = None
print(f"b: {b} - {type(b)}")