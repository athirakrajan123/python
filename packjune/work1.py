#DUCK TYPING
class Vscode:
    def compile(self):
        print("compiling using vscode")
    def excecute(self):
        print("excecute using vscode")
    def debug(self):
        print("debug using vscode")

class Pycharm:
    def compile(self):
        print("compiling using pyhcarm")
    def excecute(self):
        print("excecute using pycharm")
    def debug(self):
        print("debug using pycharm")

class Programer:
    def coding(self,ide):
        ide.compile()
        ide.excecute()
        ide.debug()
dev=Programer()
pyc=Pycharm()
dev.coding(pyc)
vs=Vscode()
dev.coding(vs)