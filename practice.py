##### 자료형 #####
##연산자
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

# 퀴즈
day = randint(4,28)
print("오프라인 스터디 모임 날짜는 메월 ",day,"일로 선정되었습니다 ")
print()


##### 문자열 처리 #####
## 문자열
sentence = "나는 소년입니다"
print(sentence)
sentence2 = "파이썬은 쉬워요"
print(sentence2)
sentence3 = """
나는 소년이고,
파이썬은 쉬워요
"""
print(sentence3)


## 슬라이싱 (원하는 정보만 빼오기)
jumin = "971123-1234567"
print("성별 : " + jumin[7])
print("연 : " + jumin[0:2]) #0 부터 2직전까지 (0,1)
print("월 : " + jumin[2:4]) #2 부터 4직전까지 (2,3)
print("월 : " + jumin[4:6]) #4 부터 6직전까지 (4,5)
print("생년월일 : " + jumin[:6]) #처음부터 부터 6직전까지
print("뒤7 자리 : "+jumin[7:]) #7부터 끝까지
print("뒤7 자리(뒤에서부터) : "+jumin[-7:]) #맨 뒤에서 부터 7번째끝까지


## 문자영 처리 함수
python = "Python is Amazing"
print(python.lower()) #문자를 소문자로
print(python.upper()) #문자를 대문자로
print(python[0].isupper()) #해당 위치가 있는 문자가 대문자인지 (대문자 = true)
print(len(python)) #문자열 전체 글자 수 길이
print(python.replace("Python","Java")) #원하는 문자 바꾸기(python -> java)

index = python.index("n") # 문자n 이 몇번째 위치해 있는지 확인 
print(index) # 5
index = python.index("n", index + 1) # 문자 n 다음에 오는 n이 몇번째 위치에 있는 지 확인 
print(index) # 15


# find
print(python.find("java")) # -1 반환 
# print(python.index("java")) # 에러남
## index : 해당 문자가 없을 때 에러남
## find : 해당 문자가 없을 때 -1을 반환

print(python.count("n")) # n 이 몇번 나오는지 알려줌


## 문자열 포멧
# 방법1
print("나는 %d살 입니다. " % 20) # %d : 숫자
print("나는 %s 를 좋아해요." % "파이썬") # %s : 문자
print("Apple 은 %c 로 시작해요. " % "A") #%c : 한글자만

# %s 는 공통
print("나는 %s살 입니다. " % 20) 
print("나는 %s 를 좋아해요." % "파이썬") 
print("Apple 은 %s 로 시작해요. " % "A")

# 두개도 가능
# 방법1
print("나는 %s 색과 %s 색을 좋아해요" % ("파란","빨강"))

# 방법2
print("나는 {}살입니다." .format(20)) 
print("나는 {} 색과 {} 색을 좋아해요" .format("파란", "빨강"))
print("나는 {0} 색과 {1} 색을 좋아해요" .format("파란", "빨강"))
print("나는 {1} 색과 {0} 색을 좋아해요" .format("파란", "빨강"))

# 방법3
print("나는 {age}살이며 {color}색을 좋아해요.".format(age=20,color="빨강"))
print("나는 {age}살이며 {color}색을 좋아해요.".format(color="빨강",age=20))

# 방법4(3.6이상)
age = 20
color = "빨강"
print(f"나는 {age}살이며 {color}색을 좋아해요.")


## 탈출문자
print("백문이 불여일견 \n백견이 불여일타") #/n : 줄바꿈

#저는 "이동탁" 입니다. 
print("저는 '이동탁' 입니다. ")
print('저는 "이동탁" 입니다. ')
print("저는 \"이동탁\" 입니다. ") # \" \' : 문장내에서 따음표로 인식함

# \\ : 문장내에서 \
# (파열경로를 표시할 때 \를 쓰는 데 문장내에서는 오류가 나기 때문에 \\를 씀)
print("D:\\C 드라이브 자료\\Desktop\\pythonworkspace")

# \r : 커서를 맨 앞으로 이동
print("Red Apple\rPine") #Red라는 문자 대신에 Pine이 쓰임

# \b : 백 스페이스 (한글자 지움)
print("Redd\bApple")

# \t : 탭
print("Red\tApple")
#주의사항 : 탈출문자 양옆에 공백이 없어야 함

# 퀴즈 
url = "http://naver.com"
url = url[7:]
url = url[:-4]
password = url[:3] + str(len(url)) + str(url.count("e")) + "!"
print(password)

##### 자료구조 #####
## 리스트 []
# 지하철 칸별로 10명, 20명, 30명
subway1 = 10  
subway2 = 20
subway3 = 30

subway = [10,20,30]
print(subway)

subway = ["유재석","조세호", "박명수"]
print(subway)

# 조세호씨가 몇번째 칸에 타고 있는가?
print(subway.index("조세호"))

# 하하씨가 다음 정류장에서 탐
subway.append("하하")
print(subway)

# 정형돈씨를 유재석/조세호 사이에 태워봄
subway.insert(1,"정형돈")
print(subway)

# 지하철에 있는 사람을 한명씩 뒤에서 꺼냄
print(subway.pop())
print(subway)

print(subway.pop())
print(subway)

# 같은 이름의 사람이 몇명있는지 확인 
subway.append("유재석")
print(subway)
print(subway.count("유재석"))

# 정렬도 가능
num_list = [5,4,3,2,1]
num_list.sort()
print(num_list)

# 순서뒤집기 가능
num_list.reverse()
print(num_list)

# 모두 지우기 
num_list.clear()
print(num_list)

# 다양한 자료형 사용가능
mix_list = ["조세호", 20, True]
print(mix_list)

# 리스트 확장
num_list = [5,4,3,2,1]
num_list.extend(mix_list)
print(num_list)

## 사전 {key:value}
cabinet = {3:"유재석",100:"김태호"}
print(cabinet[3])
print(cabinet[100])

print(cabinet.get(3))
print(cabinet.get(100))

# 값이 없으면?
# print(cabinet[5]) #에러남
print(cabinet.get(5)) #none 출력
print(cabinet.get(5, "사용가능")) #none 대신 기본값 출력 출력
print("hi")

# 값이 있는지 확인 하는 방법
print(3 in cabinet) #True
print(5 in cabinet) #False

# 키는 정수뿐만 아니라 문자 도 가능 
cabinet = {"A-3":"유재석","B-100":"김태호"}
print(cabinet["A-3"])
print(cabinet["B-100"])

# 데이터 추가 /삭제
# 새 손님 (추가)
print(cabinet)
cabinet["A-3"] = "김종국"
cabinet["C-20"] = "조세호"
print(cabinet)

# 간 손님 (삭제)
del cabinet["A-3"]
print(cabinet)

# key들만 출력
print(cabinet.keys())

# value만 출력
print(cabinet.values())
 
# key, value 쌍으로 출력
print(cabinet.items())

# 목용탕 페점
cabinet.clear();
print(cabinet)


# 튜플 (요소 추가, 변경, 삭제 불가능 대신 리스트보다 빠름)
menu = ("돈까스", "치즈까스")
print(menu[0])
print(menu[1])

# menu.add("생선까스") ##추가 불가

name = "김종국"
age = 20
hobby = "코딩"
print(name,age,hobby)

(name, age, hobby) = ("김종국", 20, "코딩")
print(name,age,hobby)


## 집합(set)
# 중복 안됨
my_set = {1,2,3,3,3}
print(my_set)

java = {"유재석", "김태호", "양세형"}
python = set(["유재석", "박명수"])

# 교집합 (java와 python을 모두 할 수 있는 개발자)
print(java & python)
print(java.intersection(python))

# 합집합 (java 할 수 있거나 pyhton 할 수 있는 개발자)
print(java | python)
print(java.union(python))

# 차집합 (java는 할 수 있지만 python은 할 줄 모르는 개발자)
print(java - python)
print(java.difference(python))

# python 할 줄 아는 사람이 늘어남
python.add("김태호")
print(python)

# java를 잊었어요
java.remove("김태호")
print(java)

# 자료구조 변경
# 커피숍
menu = {"커피","우유","쥬스"}
print(menu, type(menu))

menu = list(menu)
print(menu, type(menu))

menu = tuple(menu)
print(menu, type(menu))

menu = set(menu)
print(menu, type(menu))

# 퀴즈
lst = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
shuffle(lst)
print(lst)
chickon = sample(lst,1)
coffee = sample(lst,3) 
print("치킨 당첨자 : ",chickon)
print("커피 당첨자 ", coffee)

## 퀴즈 정답
users = range(1,21) # 1부터 20까지의 숫자를 생성
print(type(users)) # type이 리스트가 아닌 range
users = list(users) # type을 list로 변경
print(type(users)) # type이 list로 바뀜

print(users)
shuffle(users)
print(users)

winnners = sample(users,4)
print(winnners)
print("-- 당첨자 발표 --")
print("치킨 당첨자 : {0}".format(winnners[0]))
print("커피 당첨자 : {0}".format(winnners[1:]))
print("-- 축하합니다. --")








































