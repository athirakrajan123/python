class Book:
    lib_name = "college library"
    def detail(self,bname,author,pages):
        self.bname=bname
        self.author=author
        self.pages=pages
    def viewdetail(self):
        print("name",self.bname)
        print("author",self.author)
        print("pages",self.pages)
        print("library is",Book.lib_name)
    def view(self):
        print("book class method")
class Science(Book):
    def __init__(self,type,price):
        self.type=type
        self.price=price
        print("type",type)
        print("price",price)
    def view(self):
        print("science class method invoked")

obj = Science("cs",500)
obj.detail("cpp","balaguruswami",1000)
obj.viewdetail()
obj.view()