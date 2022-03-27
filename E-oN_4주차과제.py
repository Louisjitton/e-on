#이온_4주차_과제_이지은

arr = list(map(int,input("값을 입력하세요: \n").split()))     #입력받은 수를 배열에 저장

def bubble_sort(arr):
    for i in range(len(arr) -1, 0, -1):   #배열의 길이보다 1 작은 값부터 한 단계씩 내려옴
        swapped = False
        for j in range(i):
            if arr[j] > arr [j+1]:
                arr[j], arr[j+1]= arr[j+1], arr[j]
                swapped = True                       #두 수 중 작은 수를 앞으로, 큰 수를 뒤로 정렬
                
        if not swapped:
            break             #수의 정렬이 일어나지 않으면 if문 종료
        
        return arr #정렬된 값을 반환
        
print(bubble_sort(arr))