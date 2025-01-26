class Book: 
    def __init__(self, title, author, year):
        self.title : title
        self.author : author
        self.year : year
    def __del__(self):
        if self:
            self.close()
            print(f"Deleting {self.title}")
    def __str__(self, title, author, year):
        return f"{self.title} by {self.author}, published in {self.year}"
    def __rep__(self, title, author, year):
        f"Book('{self.title}', '{self.author}', {self.year})"