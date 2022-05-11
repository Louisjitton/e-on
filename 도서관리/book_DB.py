from unicodedata import name
from pip import main


class DB:
    def __init__(self, name, year, company, genre, author): #객체를 생성할 때 변수를 매개변수로
        self.name = name
        self.year = year
        self.company = company
        self.genre = genre
        self.author = author
    def show_book(self):
        print(self.name,end=" ")
        print(self.author,end=" ")
        print(self.year,end=" ")
        print(self.company,end=" ")
        print(self.genre,end=" ")
        
    def get_book(self):
        return self.name + " " + self.author + " " + self.year+ " " + self.company +" " + self.genre + "\n"