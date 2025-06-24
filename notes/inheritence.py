# simple inheritence
class test:
    def test_meth(self):
        return "this is my first class"

class child_test(test):
    pass

child_test_obj = child_test()
child_test_obj.test_meth()
#'this is my first class'

c=child_test()
c.test_meth()
#'this is my first class'


#multi level inheritance

class class1:
    def test_class1(self):
        return "this is method from class1"

    
class class2(class1):
    def test_class2(self):
        return "this is method from class2"

class class3(class2):
    pass

obj=class3()
obj.test_class1()
#'this is method from class1'
obj.test_class2()
#'this is method from class2'


#multiple inheritence

class class1:
    def test_class1(self):
        return "this is class 1"

    
class class2:
    def test_class2(self):
        return "this is class 2"

    
class class3(class1, class3):
    pass

obj_class3 = class3()
obj_class3.test_class1()
#'this is class 1'
obj_class3.test_class2()
#'this is method from class2'
