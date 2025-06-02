# Python - Debug
"""
Setting breakpoints
Stepping through code
Source code listing
Viewing stack traces
"""
import pdb


# Example from Inheritance
# parent class
class ParentDemo:
    def __init__(self, msg):
        self.message = msg

    def showMessage(self):
        pdb.set_trace()
        print(self.message)


# child class
class ChildDemo(ParentDemo):
    def __init__(self, msg):
        # ParentDemo.__init__(self, msg) # Type-1
        # use of super function
        # super(ChildDemo, self).__init__(msg) # Type-2
        super().__init__(msg)  # # Type-3


# creating instance
obj = ChildDemo("Welcome to Tutorialspoint!!")
# import pdb; pdb.set_trace()
print(obj.__dir__())
obj.showMessage()

for i in range(100):
    if i == 35:
        pdb.set_trace()
        print("Start debug your code")
    else:
        print(f"Each line: {i}")
