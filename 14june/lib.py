class Book:
    rate=1000
    def detail(self,bname,author,pages,lib_name):
        self.bname=bname
        self.author=author
        self.pages=pages
        self.lib_name=lib_name
    def viewdetail(self):
        print("name::",self.bname)
        print("author::",self.author)
        print("pages::",self.pages)
        print("library::",self.lib_name)
        print("rate::",Book.rate)

obj =Book()
obj.detail("cpp","bala",100,"college lib")
obj.viewdetail()
