import inspect, os

class ClassOne:
    def method1(self):
        classtwoObj.method2()

class ClassTwo:
    def method2(self):
        curframe = inspect.currentframe()
        calframe = inspect.getouterframes(curframe, 4)
        print '\nI was called from', calframe[1][3], \
        'in', calframe[1][4][0][6: -2]

# create objects to access class methods
classoneObj = ClassOne()
classtwoObj = ClassTwo()

# start the program
os.system('cls')
classoneObj.method1()
