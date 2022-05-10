#E-oN_도서관리프로그램_이지은

import DB

#도서관리 함수 클래스
class Book_char:
    def __init__(self) -> None:
        pass
    
    def book_append():
        add = str(input("도서명, 저자, 출판연도, 장르 순으로 입력하세요. :\n"))
        DB.book_chart.append(add)
        print("도서가 추가되었습니다.")
    
    def book_ref():
        setnum = int(input("1.도서명 2.저자 3.출판연도 4.출판사명 5.장르 \n"))
        setref = str(input("검색하고자 하는 정보의 번호를 입력하세요.: \n"))
        for value1 in DB.book_chart:
            chart = value1.split()
            for value2 in range(len(value1.split())):
                if (value2 + 1) % setnum == 0:
                    if chart[value2] == setref:
                        print("검색하신 도서의 정보입니다.\n")
                        print (value1)
        
    def book_modify(): #insert(인덱스, 값) 형태
        char_idx = int(input("정보를 수정할 도서의 번호를 입력하세요: \n"))
        print(DB.book_chart[char_idx-1])
        mod= str("도서명, 저자, 출판연도, 장르 순으로 입력하세요. :\n")
        del DB.book_chart [char_idx-1]
        DB.book_chart.insert([char_idx-1], mod)  #삭제된 도서 정보의 자리에 수정된 정보 추가
        
    
    def book_delete():
        char_idx = int(input("삭제할 도서의 번호를 입력하세요: \n"))
        del DB.book_chart [char_idx-1]
        print("%d번 도서가 삭제 되었습니다." % char_idx)
    
    def book_print():
        with open('input.txt', 'rt') as r:
            book_chart = r.readlines()
            print("현재 도서의 총 목록입니다.")
            print(book_chart)  
        
    def book_save():
        with open('input.txt', 'wt') as w: #mode 작성; w(쓰기), t(텍스트)
            for k in DB.book_chart :
                w.writelines(k)   #한꺼번에 모든 줄을 텍스트 파일에 쓰기
                
#메뉴 선택 클래스
class BOOK_MENU:
    def __init__(self) -> None:
        pass
        
    def Select(book_chart):
        print("도서 관리 프로그램\n")
        print("1: 도서 추가(도서명, 저자, 출판연도, 장르)\n")
        print("2: 도서 검색\n")
        print("3: 도서 정보 수정\n")
        print("4: 도서 삭제\n")
        print("5: 현재 총 도서 목록 출력\n")
        print("6: 저장\n")
        print("7: 프로그램 나가기(자동저장)")
        
        num= int(input("메뉴에서 수행할 기능의 번호를 입력하세요. :\n"))
    
        if num == 1 :
            Book_char.book_append()
        elif num == 2 :
            Book_char.book_ref()
        elif num == 3 :
            Book_char.book_modify()
        elif num == 4 :
            Book_char.book_delete()
        elif num == 5 :
            Book_char.book_print()
        elif num == 6 :
            Book_char.book_save()
        elif num == 7 :
            Book_char.book_save()
            print("자동 저장 후 프로그램을 종료합니다.\n")
            exit()            
        else: print("1~7 사이의 숫자를 다시 입력하십시오.:\n")
        
while 1:
    print("BOOK_SYSTEM_MENU")
    BOOK_MENU.Select(DB.book_chart)