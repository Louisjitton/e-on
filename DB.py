#mode 작성 ; r(읽기) t(텍스트)
#원본파일 내용을 라인별로 리스트 형태로 리턴 
with open('input.txt', 'rt') as r:
    book_chart = r.readlines()
    
#개행문자(\n) 삭제
book_chart=[line.rstrip('\n') for line in book_chart]