from abc import ABC,abstractmethod
class P(ABC):
    def meth1(self):
        print("Parent meth1 ")
    def meth2(self):
        pass
class Child(P):
    def meth3(self):
        print("Child meth3")
    def meth2(self):
        print("Child meth2")

c = Child()
c.meth2()
