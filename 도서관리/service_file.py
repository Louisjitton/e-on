import os
import book_DB

class service:
    def __init__(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'input.txt')
        f = open(my_file,'r',encoding="UTF-8")
        book_List = f.readlines() #한줄씩 불러오기
        self.book_list = []
        for i in range(0, len(book_List)):
            self.book_list.append(book_DB.DB(book_List[i].split()[0],
                                        book_List[i].split()[1],
                                        book_List[i].split()[2],
                                        book_List[i].split()[3],
                                        book_List[i].split()[4]))
    def show(self):
        for book in self.book_list:
            book.show_book()
            print() #빈칸으로 두면 엔터
    
    def add(self):
        new_book = str(input("추가할 도서의 도서명, 저자, 출판연도, 출판사명, 장르를 입력하세요. :")).split()
        self.book_list.append(book_DB.DB(new_book[0],
                                      new_book[1],
                                      new_book[2],
                                      new_book[3],
                                      new_book[4]))
    
    def delete_book(self):
        self.show()
        delete_index = int(input("삭제할 도서를 선택하세요.: "))
        self.book_list.pop(delete_index).show_book()
        print("이 삭제되었습니다.")
        
    def modify_book(self):
        self.show()
        modify_index = int(input("수정할 도서를 선택하세요.: "))
        modify_book = str(input("수정할 도서의 도서명, 저자, 출판연도, 출판사명, 장르를 입력하세요. :")).split()
        self.book_list.pop(modify_index).show_book()
        print("==================수정되었습니다.==================")
        self.book_list.append(book_DB.DB(modify_book[0],
                                         modify_book[1],
                                         modify_book[2],
                                         modify_book[3],
                                         modify_book[4],))
        
    def find_book(self):
        find_index = int(input("검색할 정보를 선택하세요. : 1. 도서명, 2. 저자, 3. 출판연도, 4. 출판사명 5. 장르"))
        find_text = str(input("검색어를 입력하세요.: "))
        result = []
        for book in self.book_list:
            if find_index == 1:
                if find_text in book.name:
                    book.show_book()
            if find_index == 2:
                if find_text in book.author:
                    book.show_book()
            if find_index == 3:
                if find_text in book.year:
                    book.show_book()
            if find_index == 4:
                if find_text in book.company:
                    book.show_book()
            if find_index == 5:
                if find_text in book.genre:
                    book.show_book()
                    
        
    def save_book(self):
        THIS_FOLDER = os.path.dirname(os.path.abspath(__file__))
        my_file = os.path.join(THIS_FOLDER, 'input.txt')
        f = open(my_file,'w',encoding="UTF-8")
        for book in self.book_list:
            f.write(book.get_book())
