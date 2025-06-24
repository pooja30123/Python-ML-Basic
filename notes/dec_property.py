#PROPERTIE DECORATOR

#"_" single underscore means protected
#"__" double underscore means private


#NORMAL
class pwskills:
    def __init__(self, course_price, course_name):
        self.__course_price = course_price
        self.course_name = course_name

        
pw = pwskills(3500,"data science")
pw.course_name
#'data science'
pw._pwskills__course_price
#3500



#PROPERTY
class pwskills:
    def __init__(self, course_price, course_name):
        self.__course_price = course_price
        self.course_name = course_name
    @property
    def course_price_sccess(self):
        return self.__course_price

    
pw = pwskills(3500,"data science")
pw.course_name
#'data science'
pw.course_price_sccess
#3500

#SETTER
class pwskills:
    def __init__(self, course_price, course_name):
        self.__course_price = course_price
        self.course_name = course_name
    @property
    def course_price_access(self):
        return self.__course_price
    @course_price_access.setter
    def course_price_set(self, price):
        if price<=3500:
            pass
        else:
            self.__course_price = price

            
pw = pwskills(3500,"data science")
pw.course_price_access
#3500
pw.course_price_set = 4500
pw.course_price_access
#4500

#DELETER
class pwskills:
    def __init__(self, course_price, course_name):
        self.__course_price = course_price
        self.course_name = course_name
    @property
    def course_price_access(self):
        return self.__course_price
    @course_price_access.setter
    def course_price_set(self, price):
        if price<=3500:
            pass
        else:
            self.__course_price = price
    @course_price_access.deleter
    def delete_course_price(self):
        del self.__course_price

        
pw=pwskills(4000,"data science")
pw.course_name
#'data science'
pw.course_price_access
#4000
pw.course_price_set = 5000
pw.course_price_access
#5000
del pw.delete_course_price
pw.course_price_access
'''Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    pw.course_price_access
  File "<pyshell#58>", line 7, in course_price_access
    return self.__course_price
AttributeError: 'pwskills' object has no attribute '_pwskills__course_price' '''


