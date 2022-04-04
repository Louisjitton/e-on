#E-oN_5주차_이지은

arr= list(map(int, input("1개 이상 100개 이하의 수를 입력하세요.: ")))
print (arr)
commands= list(map(int, input("[i,j,k]에 해당하는 값을 입력하세요.: ").split("","")))
print (commands)

def solution(array, commands):
   answer=[]
   
   for i in commands:
       new_array=array[i[0]-1: i[1]]        # n번째부터 자른다 하면, n-1번째 인덱스부터 자름
       new_array.sort()                     # sort 함수로 정렬
       answer.append(new_array[i[2]-1])     # K번째 값 추가
       
   return answer                   #정렬된 리스트 값이 담긴 리스트 반환
 
print(solution(array, commands))