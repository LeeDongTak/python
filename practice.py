##연산
print(1+1)
print(3-2)
print(5*2)
print(6/3)

print(2**3) #2의 3제곱 = 8
print(5%2) #나머지 구하기 = 1
print(10%3) #나머지 구하기 = 1
print(5//3) #몫 구하기 = 1
print(10//3) #몫 구하기 = 3

print(10 > 3) #ture
print(4 >= 7) #false
print(10 < 3) #false
print(5 <= 5) #ture

print(3 == 3) #ture
print(4 == 2) #false
print(3 + 4 == 7) #ture

print(1 != 3) #true
print(not(1 != 3)) #false

print((3>0) and (3 < 5)) #true
print((3>0) & (3 < 5)) #true

print((3 > 0) or (3 > 5)) #true
print((3 > 0) | (3 > 5)) #true
print(5 > 4 > 3) #true
print(5 > 4 > 7) #false

print(2 + 3 * 4) #14
print((2 + 3) * 4) #20
number = 2 + 3 * 4
print(number) #14
number = number + 2 #16
print(number) 
number += 2 #18
print(number)
number *= 2 #36
print(number)
number /= 2 #18
print(number)
number -= 2 #16
print(number)

number //= 5 #몫임 == 3
print(number)

## 숫자처리 함수
print(abs(-5)) #절대값 == 5
print(pow(4,2)) #두 수를 제곱함 == 4*2 = 16
print(max(5,12)) #최대값 == 12
print(min(5,12)) #최소값 == 5
print(round(3.14)) #반올림 == 3
print(round(5.99)) #반올림 == 6


##렌덤한 수 생성하기 
from math import *
print(floor(4.99)) #내림 == 4
print(ceil(3.14)) #올림 == 4
print(sqrt(16)) #제곱근 == 4

from random import *
print(random()) #0.0 ~ 1.0미만의 임의의 값 생성
print(random() * 10) #0.0 ~ 10.0미만의 임의의 값 생성
print(int(random() * 10)) #0 ~ 10미만의 임의의 값 생성
print(int(random() * 10)) #0 ~ 10미만의 임의의 값 생성
print(int(random() * 10)) #0 ~ 10미만의 임의의 값 생성
print(int(random() * 10) + 1) #1 ~ 10이하의 임의의 값 생성
print(int(random() * 10) + 1) #1 ~ 10이하의 임의의 값 생성
print(int(random() * 10) + 1) #1 ~ 10이하의 임의의 값 생성
print(int(random() * 10) + 1) #1 ~ 10이하의 임의의 값 생성
print(int(random() * 10) + 1) #1 ~ 10이하의 임의의 값 생성
print(int(random() * 10) + 1) #1 ~ 10이하의 임의의 값 생성
print()
##로또번호 생성하기 
print(int(random() * 45) + 1) #1 ~ 45이하의 임의의 값 생성
print(int(random() * 45) + 1) #1 ~ 45이하의 임의의 값 생성
print(int(random() * 45) + 1) #1 ~ 45이하의 임의의 값 생성
print(int(random() * 45) + 1) #1 ~ 45이하의 임의의 값 생성
print(int(random() * 45) + 1) #1 ~ 45이하의 임의의 값 생성
print(int(random() * 45) + 1) #1 ~ 45이하의 임의의 값 생성

print(randrange(1,46)) #1 ~ 46미만의 임의의 값 생성
print(randint(1,45)) #1 ~ 45이하의 임의의 값 생성
print()

##퀴즈
day = randint(4,28)
print("오프라인 스터디 모임 날짜는 메월 ",day,"일로 선정되었습니다 ")
print()

##문자열 처리
sentence = "나는 소년입니다"
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)

##슬라이싱 (원하는 정보만 빼오기)
jumin = "971123-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) #0 부터 2직전까지 (0,1)
print("월 : " + jumin[2:4]) #2 부터 4직전까지 (2,3)
print("월 : " + jumin[4:6]) #4 부터 6직전까지 (4,5)
print("생년월일 : " + jumin[:6]) #처음부터 부터 6직전까지
print("뒤7 자리 : "+jumin[7:]) #7부터 끝까지
print("뒤7 자리(뒤에서부터) : "+jumin[-7:]) #맨 뒤에서 부터 7번째끝까지

##문자영 처리 함수
python = "Python is Amazing"
print(python.lower()) #문자를 소문자로
print(python.upper()) #문자를 대문자로
print(python[0].isupper()) #해당 위치가 있는 문자가 대문자인지 (대문자 = true)
print(len(python))
print(python.replace("Python","Java"))





