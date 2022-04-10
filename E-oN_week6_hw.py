#E-oN_6주차_과제

piece=int(input("피자의 조각수를 입력하세요. :"))
case=[1,1]      #값을 저장할 리스트 생성

for i in range(2, piece+1):
    case.append(case[i-2] + case[i-1])      #리스트에 요소 추가
    
print(case[piece])