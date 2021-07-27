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

obj = Book()
obj.detail("cpp","balaguruswami",1000)
obj.viewdetail()