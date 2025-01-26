class Book: 
    def __init__(self, title, author, year):
        self.title : "1984"
        self.author : "George Orwell"
        self.year : "1949"
    def __del__(self):
        if self:
            self.close()
            print(f"Deleting {self.title}")
    def __str__(self):
        return f"{self.title} by {self.author}, published in {self.year}"
    def __repr__(self):
        f"Book('{self.title}', '{self.author}', {self.year})"