"""1. 암묵적 형변환
- 서로 다른 두 자료형의 연산 시
  값의 범위가 작은 자료형이 큰 자료형으로 자동 변환되는 것
"""
print("--- 암묵적 형변환 ---")

print('1 + 2.3 =', 1 + 2.3) # 3.3
# int + float  -> float + float = float
# int가 float로 변환!

print('True + 3 =', True + 3) # 4
# bool + int  -> int + int = int
# bool이 int로 변환!

print('True + True =', True + True) # 2
# bool + bool -> int + int = int
# bool은 더하기 연산이 안되기 때문에, 가능한 int로 자동 형변환

# print('1' + 1)
# TypeError: can only concatenate str (not "int") to str
# -> '문자열은 문자열 끼리만 + 연산을 할 수 있다' 라는 오류!


""" 2. 명시적 형변환
- 지정된 값을 원하는 자료형으로 강제 형변환
"""
print("--- 명시적 형변환 ---")
print(int('3') + 4)  
# int(str) + int -> int + int

print(3, float(3), float('3'))
# print(float('삼')) # 숫자가 아니므로 숫자로 변환 불가

print('1' + str(2)) # 12 (문자열 이어쓰기)

print(bool(1), bool(0)) # True False


""" Truthy, Falsy 
- Truthy : True로 해석되는 것들
- Falsy  : Flase로 해석되는 것들
 -> 0, 0.0, '' (빈 문자열), [] (빈 리스트),
    () (빈 튜플), {} (빈 딕셔너리), None
"""
print("--- bool() 형변환 - Truthy ---")
print('bool(100):', 100, bool(100))
print('bool(-100):', -100, bool(-100))
print("bool('abcd'):", 'abcd', bool('abcd'))
print("bool(' '):", ' ', bool(' ')) # 공백 문자 /스페이스
print('bool([1, 2]):', [1, 2], bool([1, 2]))
print('bool((1, 2)):', (1, 2), bool((1, 2)))
print("bool({'is_friday': True}):", {'is_friday': True}, bool({'is_friday': True}))


print("--- bool() 형변환 - Falsy ---")
print("bool(0):", '', bool(0))
print('bool(0.0):', 0.0, bool(0.0))
print("bool(''):", '', bool('')) # 빈 문자열
print('bool([]):', [], bool([])) # 빈 리스트
print('bool(()):', (), bool(())) # 빈 튜플
print('bool({}):', {}, bool({})) # 빈 딕셔너리
print('bool(None):', None, bool(None))


# 실사용 예시
""" 한 줄 조건문
```
[A] if 조건문 else [B]
```
[A]: 조건문이 참 일때 반환되는 값
[B]: 조건문이 거짓 일때 반환되는 값

조건식 : 연산 결과가 True 또는 False인 식
"""

age = 19
print("성인" if age >= 20 else "미성년자")


s1 = ''
# print('내용 O' if 조건식 else '내용 X')

print('내용 O' if len(s1) > 0 else '내용 X')

print('내용 O' if bool(s1) else '내용 X')

print('내용 O' if   s1   else '내용 X')