# print(5)
# print(-10)
# print(3.14)
# print(100000)
# print(5+3)
# print(2*18)
# print(3*(3+1))
# print('풍선')
# print("나비")
# print("ㅋㅋㅋㅋㅋㅋㅋㅋ")
# print("z"*9)
# print(5 > 10)
# print(5 < 10)
# print(True)
# print(not True)
# print(not False)
# print(not 5 > 10)

# age = 5
# animal = "고양이"
# name = "나비"
# hobby = "낮잠"
# is_adult = age >= 3


# print("우리집 "+ animal + "의 이름은 " + name + "에요")
# print(name + "는  " + str(age) + "살이며, "+ hobby + "을 아주 좋아해요")
# print(name + "는 어른일까요?" + str(is_adult))

# print("우리집" , animal, "은 사람같다") 

# station = "사당"
# print(station + "행 열차가 들어오고 있습니다.")

# station = "신도림"
# print(station + "행 열차가 들어오고 있습니다.")

# station = "인천공항"
# print(station + "행 열차가 들어오고 있습니다.")

# print(2**3)

# print(5%3) 
# print(5//3)
# print(5 >= 5)

# print(3 == 3)
# print((3 > 0) and (3 <5))
# print((3 > 0) | (3 > 5))

# number = 2 + 3 * 4

# print(number)

# number = number + 2
# print(number)
# number += 2
# print(number)
# number *= 2
# number /= 2

# from random import *

# # print(int(random()))
# # print(int(random() * 45) + 1) 
# # print(randrange(1,46))

# date = str(randint(4,28))
# date = str(int(random()*26 + 3))
# print("오프라인 스터디 모임 날짜는 매월 " + date + "일로 선정되었습니다.")

# date = randint(4,28)
# print("오프라인 스터디 모임 날짜는 매월 " + str(date) + "일로 선정되었습니다.")

# print("오프라인 스터디 모임 날짜는 매월" + str(date) + "일로 선정되었습니다.")

# print("오프라인 스터디 모임 날짜는 매월", date, "일로 선정되었습니다.")

'''from random import *

def 복권() :
    print(randint(1,45))
    print(randint(1,45))
    print(randint(1,45))
    print(randint(1,45))
    print(randint(1,45))
    print(randint(1,45))

복권() '''


# sentence = '나는 소년입니다.'
# print(sentence)

# sentence2 = "파이썬은 쉬워요"
# print(sentence2)

# sentence3 = """
# 나는 파이썬을 공부중이고,
# 유튜브로 독학중이에요.
# """
# print(sentence3)



# jumin = "990316-1234567"

# print("성별 : " + jumin[7])
# print("연 : " +jumin[0:2]) #0 부터 2 직전꺼지
# print("월 : " +jumin[2:4])
# print("생년월일 : " +jumin[:6]) # [0:6] = [:6]
# print("뒷자리 : " + jumin[7:14]) # [7:14] = [7:]
# print("뒷자리를 역순으로 : " + jumin[-7:])


# python = "Python is Amazing"

# print(python.lower())
# print(python.upper())
# print(python[0].isupper())
# print(len(python))
# print(python.replace("Python", "Java"))

# index = python.index("n")
# print(index)

# index = python.index("n", index + 1)
# print(index)



# print("나는 %d살입니다." %26)
# print("나는 %s을 공부중입니다." %"파이썬")
# print("Python은 %c로 시작해요" % "P")

# print("%s와 %s" % ("너" , "나"))

# print("{}와 {}".format("너" , "나"))
# print("{0}와 {1}".format("너" , "나"))
# print("{1}와 {0}".format("너" , "나"))


# print("나는 {food}과 {customer}을 싫어한다".format(food = "버섯", customer = "고객"))
# print("나는 {food}과 {customer}을 싫어한다".format(customer = "고객" , food = "버섯" ))

# age = 26
# color = "black"

# print(f"I'm {age} years old, I like {color}")



# print("나를 알고 \n적을 알면 백전백승")
# print("C:\\Users\\EC\\Desktop\\Python workspace>")

# print("red apple\rpine")
# print("redd\b")
# print("red\tapple")


# site = "www.naver.com"
# rule1 = site.replace("www.", "")
# rule2 = rule1[:rule1.index(".")] # rule1[:5]
# password = rule2[:3] + str(len(rule2)) + str(rule2.count("e")) + "!"
# print(password)



# subway = [10, 20, 30]
# subway = ["Jhon", "kali", "uro"]
# subway.append("ura")

# num_list = [6,8,4,10]
# num_list.sort()
# mix_list = ["human", True, 5]
# num_list.extend(mix_list)
# print(num_list)


# cabinet = {3:"유재석", 100:"김태호"}

# print(cabinet[3]) 
# print(cabinet.get(3))

# print(cabinet.get(5, "시용 가능"))

# cabinet = {"A-3": "유재석"}
# cabinet["B-3"] = "조세호" #값을 추가하는 경우


# print(cabinet.keys())
# print(cabinet.values())
# print(cabinet.items())



# name = "안은철"
# age = 26
# hobby = "코딩"
# (name, age, hobby) = ("안은철", 26, "코딩")
# print(name, age, hobby)


# java = {"유재석", "김태호", "양세형"}
# python = set(["유재석", "박명수"])

# print(java.intersection(python)) # java & python
# print(java.union(python)) ## java | python

# print(java - python)

# java.add("하하")
# print(java)
# java.remove("김태호")
# print(java)



# menu = {"커피","우유", "주소"}
# print(menu, type(menu))
# menu = list(menu)
# print(menu, type(menu))
# menu = tuple(menu)
# print(menu, type(menu))
# menu = set(menu)
# print(menu, type(menu))

# from random import *

# users = range(1,21) #타입이 range로 나와서 리스트로 변경을 해줘야 리스트 관련 함수를 쓸 수 있음
# users = list(users)

# shuffle(users)

# winners = sample(users, 4)

# print("치킨담청자 : {}".format(winners[0]))
# print("커피 당첨자 : {}".format(winners[1:]))

# weather = input("오늘 날씨는 어때요?")

# if weather == "비" or weather == "눈":
#     print("우산을 챙기세요")
# elif weather == "미세먼지":
#     print("마스크를 챙기세요")
# else:
#     print("오늘은 준비물이 필요없어요")


# temp = int(input("오늘 기온은 어때요?"))

# if 30 <= temp:
#     print("너무 더워요 나가지마세요")
# elif 10 <= temp <30:
#     print("날씨가 좋아요")
# elif 0 <= temp and temp < 10:
#     print("외투를 챙기세요")
# else:
#     print("너무 추워요 나가지 마세요")

# for waiting_num in [1,2,3,4,5]: # in range(1,6)
#     print("대기번호: {}".format(waiting_num))

# starbucks = ["아이언맨", "토르", "그루트"]
# for customer in starbucks:
#     print("{}님, 커피가 준비되었습니다.".format(customer))

# customer = "토르"
# index = 5
# while index >= 1:
#     print("{0}, 커피가 준비 되었습니다. {1}번 남았습니다.".format(customer, index))
#     index -= 1
#     if index == 0:
#         print("커피는 폐기처분되었습니다.")


    # customer = "아이언맨"
    # index = 1
    # while True:
    #     print("{0}, 커피가 준비 되었습니다. 호출 {1}회.".format(customer, index))
    #     index += 1
#무한 루트 -> ctrl c 누르면 강제 종료

# customer = "그루트"
# person = "unknown"

# while person != customer:
#      print("{0}, 커피가 준비 되었습니다.".format(customer))
#      person = input("이름이 어떻게 되세요?")

# absent = [2,5]
# no_book = [7]
# for student in range(1,11):
#     if student in absent:
#         continue
#     if student in no_book:
#         print("오늘 수업 여기까지. {}은 교무실로 따라와".format(student))
#         break
#     print("{}번, 책을 읽어봐".format(student))


# students =[1,2,3,4,5]
# students = [i+100 for i in students]
# print(students)

# students = ["Thor", "Groot", "Iron man"]
# students = [len(x) for x in students]
# print(students)


# students = ["Thor", "Groot", "Iron man"]
# students = [x.upper() for x in students]
# print(students)


# from random import *
# passenger = 0
# for i in range(1,51):
#     time = randrange(5,51)
#     if 5 <= time <= 15:
#         print("[O] {}번째 손님" "(소요시간 : {} ".format(i, time))
#         passenger += 1
#     else:
#         print("[ ] {}번째 손님" "(소요시간 : {} ".format(i, time))
# print("총 탑승 승객 : {}".format(passenger))


# def open_account():
#     print("새로운 계좌가 생성되었습니다.")


# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("잔액이 부족합니다. 잔액은 {}입니다".format(balance))
#         return balance

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission


# balance = 2000
# # balance = deposit(balance, 2000)
# # balance = withdraw(balance, 1000)

# commission, balance = withdraw_night(balance, 500)


# def profile(name, age, main_lang):
#     print("이름 : {} \t나이 : {} \t주 사용 언어 : {}".format(name, age, main_lang))

# def profile(name, age=17, main_lang= "파이썬"):
#     print("이름 : {} \t나이 : {} \t주 사용 언어 : {}".format(name, age, main_lang))

# profile("유재석", 25, "자바")
# profile("안은철", 26, "파이썬")


# def profile(name, age, *language):
#     print("이름 : {0}\t나이 : {1}\t   ".format(name, age), end=" ")
#     for lang in language:
#         print(lang, end=" ")

# profile("유재석", 20, "python", "swift", "Kotlin")


# gun = 10

# def checkpoint(soliders):
#     global gun
#     gun = gun - soliders
#     print("[함수 내] 남은 총 : {}".format(gun))


# def checkpoint_ret(gun, soliders):
#     gun = gun - soliders
#     print("[함수 내] 남은 총 : {}".format(gun))
#     return gun

# print("[전체 총] : {}".format(gun))
# gun = checkpoint_ret(gun, 2)
# # checkpoint(2)
# print("남은 총 : {}".format(gun))




# def std_weight(gender, height):
#     m_weight = round((height/100) * (height/100) * 22, 2)
#     w_weight = round((height/100) * (height/100) * 21, 2)
#     if gender == 1:
#         print("키 {}cm 남자의 표준 체중은 {}kg입니다.".format(height, m_weight) )
#     else:
#         print("키 {}cm 여자의 표준 체중은 {}kg입니다." .format(height, w_weight))


# def std_weight(height, gender):
#     if gender == "남자":
#         return height * height *22
#     else:
#         return height * height *21
    
# height = 173
# gender = "남자"
# weight = round(std_weight(height/100, gender), 2)
# print("키 {}cm {}의 표준 체중은 {}kg입니다".format(height, gender, weight))

# scores = {"수학":40, "영어":70, "코딩":80}
# for subject, score in scores.items():
#     print(subject.ljust(8), str(score).rjust(4), sep=":")

# for number in range(1,21):
#     print("대기번호" , str(number).zfill(3), sep=" : ") 


# answer = input("아무값이나 입력하세요 : ")
# print("입력하신 값은" + answer + "입니다.")


# print("python", "java", sep=" vs ")


# print("{0: >10}".format(500)) # 빈 자리는 빈 공간으로 두고, 오른쪽 정렬을 하되, 총 10자리 공간을 확보





# def open_account():
#     print("새로운 계좌가 생성되었습니다.")

# balance = 10000

# def withdraw_night(balance, money):
#     commission = 100
#     return commission, balance - money - commission

# # commission, balance = withdraw_night(balance, 500)

# open_account()

# def deposit(balance, money):
#     print("입금이 완료되었습니다. 잔액은 {} 원입니다.".format(balance + money))
#     return balance + money

# def withdraw(balance, money):
#     if balance >= money:
#         print("출금이 완료되었습니다. 잔액은 {}원 입니다.".format(balance - money))
#         return balance - money
#     else:
#         print("잔액이 부족합니다. 잔액은 {}입니다".format(balance))
#         return balance

# deposit(balance , 2000)
# print(balance)










