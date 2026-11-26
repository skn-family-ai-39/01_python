""" 문자열(str)

- 문자가 나열된 형태
- 리터럴 표기법: " ", ' ', """ """, ''' ''' 

- 문자열은 문자들이 순서대로 나열된 텍스트 시퀀스이다.
- 문자의 순서는 0 부터 시작
- 이때, 시퀀스 순서를 index라고 부른다


"""
# str 리터럴 표기법
print("--- 홑따옴표, 쌍따옴표 ---")
s1 = '안녕'
s2 = "잘가"
# s3 = "배고파' # Error, 따옴표는 같은 것 쌍으로 존재해야한다

print(f's1: {s1} - {type(s1)}')
print(f's2: {s2} - {type(s2)}')

print("--- 삼중 홑따옴표, 삼중 쌍따옴표 ---")
s4 = ''' 1번줄
2번줄
3번줄
'''

s5 = """ aaaaa
bbbbb
ccccc
"""

print(s4)
print(s5)

# 문자열 전용 연산자

# + 연산자:  문자열 이어쓰기 
print('+ 연산자는 ' + '문자열을 ' + '이어쓰기 해주는 ' + '연산자입니다.')

# * 연산자:  문자열 반복 작성
print('* 는 문자열 반복 / ' * 5)

""" 문자열(str) 전용 메서드

- https://docs.python.org/ko/3.13/library/stdtypes.html#str

"""

# len(문자열 또는 객체): 파이썬 객체(문자열, 리스트, 튜플, 딕셔너리, 셋...)

print("--- len(문자열 또는 객체) ---")
text = "hello"
print("len(text): ", len(text)) # 5



# str.replace(old, new) : 문자열 중 old를 찾아서 new로 변환
print('--- str.replace() ---')
today = '2026-11-25'

today_ = today.replace('-', '/')

print(today_)


"""
세상에서 제일 긴 게 뭘까요?
기차? 기린의 목? 코끼리의 코?
전부 아닙니다.
여러분의 무한한 가능성입니다^^
"""

# str.strip(문자열) : 문자열 시작/끝 부분 공백 제거
print("--- str.strip() ---")
text = '   hello   '
print(text.strip()) # hello
print(text.lstrip()) # hello   
print(text.rstrip()) #    hello


""" 
문자열(문자 + 배열)
- 파이썬의 문자열을 나타내는 str은 text sequence 형태를 갖는다.
- sequence: 순서가 있는 데이터 구조 (0-based index)
- 0-based index: 0부터 시작, 마지막 인덱스는 (길이-1)
- 인덱스를 통해 접근 가능
"""

print("--- 문자열 인덱싱 ---")
temp = "혼자 공부하는 파이썬"
print(temp[0],  temp[5], temp[10])

print( temp[len(temp) - 1] )   # 마지막 글자 찾기


# 문자열 역 인덱싱: 음수를 이용해서 인덱싱
print("--- 문자열 역 인덱싱 ---")
temp = "혼자 공부하는 파이썬"
print(temp[-1], temp[-2], temp[-3]) # 썬 이 파

# slicing 지원
# - 문자열의 일부를 가져오는 방법
# - [start:stop:step]
# - start 시작하는 인덱스 (inclusive)
# - stop 종료 인덱스 (포함되지 않음. exclusive)
# - step 인덱스 이동 간격 (기본값 1)


print("--- slicing ---")
temp = "파이썬 머신러닝 판다스 데이터 분석"
print("--- slicing ---")
temp = "파이썬 머신러닝 판다스 데이터 분석"

print(temp[0:3]) # 파이썬
print(temp[4:8]) # 머신러닝

""" stop을 작성하지 않은 경우 == 끝까지 """
print(temp[9:]) # 판다스 데이터 분석
print(temp[-2:]) # 분석

text = "파이썬 텍스트 마이닝 완벽 가이드"
print(text[0:3:1]) # 파이썬
print(text[0:3:2]) # 파썬
print(text[0:10:2]) # 파썬텍트마
print(text[::2]) # 파썬텍트마닝완 이

# 음수 step
print(text[::-1]) # 문자열 뒤집기
print(text[::-2]) # 드가벽 이 스 이
print(text[4::2])


teacher_name = "다람쥐"

print(f"안녕하세요. 오늘부터 여러분과 함께 공부할 {teacher_name} 강사입니다~!")
