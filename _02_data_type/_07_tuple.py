"""
tuple
- 바깥 요소 재대입을 허용하지 않는 불변 시퀀스이다.
- 저장순서 기억
- 주로 데이터의 집합을 안전하게 유지하거나, 함수에서 여러 값을 반환할 때 사용
- list는 바뀔 수 있는 목록, tuple은 구조가 고정된 값 묶음으로 설명할 수 있다.
- 예: 학생 정보처럼 계속 수정될 수 있으면 list, 
      RGB값처럼 고정된 묶음은 tuple
"""


print("--- tuple ---")

t1 = () # 빈 튜플
t2 = (10) # 값이 하나만 존재하는 튜플 == 일반 변수
t3 = (10,) # [진짜] 값이 하나만 존재하는 튜플

print(f't1: {t1} - {type(t1)}') # t1: () - <class 'tuple'>
print(f't2: {t2} - {type(t2)}') # t2: 10 - <class 'int'>
print(f't3: {t3} - {type(t3)}') # t3: (10,) - <class 'tuple'>

t4 = (10, 20)
t5 = 10, 20     # 변수는 값 하나만 저장
                # -> 자동으로 tuple 하나로 묶음
print(f't4: {t4} - {type(t4)}') # t4: (10, 20) - <class 'tuple'>
print(f't5: {t5} - {type(t5)}') # t5: (10, 20) - <class 'tuple'>               

print("--- tuple indexing ---")
tpl = ('a', 'b', 'c', 'd')
print('tpl[0]:', tpl[0])
print('tpl[1]:', tpl[1])


print("--- tuple slicing ---")
print("--- tuple indexing ---")
tpl = ('a', 'b', 'c', 'd')
print('tpl[0]:', tpl[0])
print('tpl[1]:', tpl[1])


print("--- tuple slicing ---")
print('tpl[0:3]:', tpl[0:3])


""" tuple unpacking
- 묶여있는 값을 푸는 방법

- *튜플변수
"""

print("--- tuple unpacking ---")
# tpl = ('a', 'b', 'c', 'd')

# ('A', 'a', 'b', 'c', 'd') 만들기
tpl_ =   ('A',) + tpl
print("('A',) + tpl =", tpl_)

tpl_ = 'A', *tpl
print("'A', *tpl = ", tpl_)

# tpl 이용해서 ('A', 'b', 'c', 'd') 만들기

# tpl = ('a', 'b', 'c', 'd')
#tpl[0] = 'A' # TypeError

tpl_ = 'A' , *tpl[1:]
print(" 'A' , *tpl[1:] = ", tpl_)

# 튜플 활용하기
# - 복수개의 값을 변수에 할당하기
# 튜플 활용하기
# - 복수개의 값을 변수에 할당하기
print("--- 복수개의 값을 변수에 할당하기 ---")
# a = 100
# b = 200
# c = 300
# a, b, c = (100, 200, 300)
a, b, c = 100, 200, 300
print(a, b, c)


print("--- 값 교환 ---")
x, y = 88, 99

# 보편적인 방법
temp = x
x = y
y = temp
print(x, y) 

# 튜플 이용 방법
x, y = 100, 200
x, y = y, x

# 튜플 이용 방법
x, y = 100, 200
x, y = y, x
print("x: ",x, "y: ", y)

"""  in 연산자
- 시퀀스 타입에서 사용 가능한 연산자
```
찾고싶은값 in 시퀀스타입(list,tuple)
```
- in을 기준으로 왼쪽 값이 오른쪽 시퀀스에 있는지 확인
 -> True/False
"""

address = '서울시 서초구 효령로 335'
print('서울시' in address)
print('용인시' in address)

# 리스트
location = ['서울', '부산', '인천', '광주', '세종']
print('인천' in location) # True
print('울산' in location) # False

# 튜플
names = ('김철수', '홍길동', '이미영')
print('이미영' in names) # True
print('김미영' in names) # False

#-------------------혼자 이것저것-------------------------
print(tpl)
print(*tpl)
print(tpl + tpl)
print(*tpl + tpl)
print ('안', '녕')
print('안' + '녕')
print('a', 'b', 'c', 'd')


tpl2 = (1,2,3,4)
print(tpl2)
print(*tpl2)
a = 1,2,3,4
b = 1,2,3,4
print(a)
print(a+b)
print(a,b)
# print(*tpl2 + tpl)
print(*tpl, *tpl)