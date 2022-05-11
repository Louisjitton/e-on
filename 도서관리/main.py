from service_file import service

while 1:
    a= service()
    
    print("1. 도서추가 \n2. 도서검색 \n3. 도서 정보 수정 \n4. 도서 삭제 \n5.현재 총 도서 목록 출력 \n6. 저장 \n7. 프로그램 나가기")
    select = int(input("초기 메뉴를 선택하세요. :"))
    
    if select == 1:
        a.add()
        a.save_book()
        a.show()
        
    elif select == 2:
        a.find_book()
    
    elif select == 3:
        a.modify_book()
        a.save_book()
        a.show()
    
    elif select == 4:
        a.delete_book()
        a.save_book()
        a.show()
        
    elif select == 5:
        a.show()
    
    elif select == 6:
        a.save_book()
        a.show()
        
    elif select == 7:
        a.save_book()
        print("자동저장 되었습니다.")
        exit()
    
    else:
        print("1-7 사이의 숫자를 입력해주세요.:")
    
    break
