class Book:
    lib_name = "tcr library"
    def detail(self, bname, author, pages):
        self.bname = bname
        self.author = author
        self.pages = pages
    def viewdetail(self):
        print("name::", self.bname)
        print("author::", self.author)
        print("pages::", self.pages)
        print("library::", Book.lib_name)
    def __str__(self):
            return self.bname

obj = Book()
obj.detail("cpp", "balaguruswami", 1000)
obj.viewdetail()
print(obj)

#The__str__(self)method in python represents the class objects as a string type.
#it can be used for classes.The __str__() method should easy to read and output all the string members of the class.
#This method is also used as a string function in a class.
#it is only deals with the string type variables in a class.
#not supporting int type variables.
#when the object prints by this function returns the reference that used in the program.