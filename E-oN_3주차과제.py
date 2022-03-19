#E-oN_3주차_과제
#E-oN 18기 21학번 이지은

kgu=list(map(int,input().split(","))) #함수 밖에서 입력 받은 수를 배열에 저장
kgu_value=0

for i in kgu:
    kgu_value += i
    
print(kgu_value)