#Class Methods

#Normal Way
class pwskills:
    def __init__(self,name,email):
        self.name = name
        self.email = email
    def student_details(self):
        print(self.name, self.email)


        
pw = pwskills("pooja", "pooja@gmail.com")
print(pw.name)
#'pooja'
print(pw.email)
#'pooja@gmail.com'
pw.student_details()
#pooja pooja@gmail.com

#USING CLASS METHOD

class pwskills1:
    def __init__(self,name,email):
        self.name = name
        self.email = email
        
    @classmethod
    def details(cls, name, email):
        return cls(name, email)
    
    def student_details(self):
        print(self.name, self.email)

        
pw1=pwskills1.details("shanti", "shanti@gmail.com")
print(pw1.name)
#'shanti'
print(pw1.email)
#'shanti@gmail.com'
pw1.student_details()
#shanti shanti@gmail.com



class pwskills2:

    mobile_num=899655565

    def __init__(self,name,email):
        self.name = name
        self.email = email

    @classmethod
    def change_number(cls,mobile):
        pwskills2.mobile_num = mobile

    @classmethod
    def details(cls, name, email):
        return cls(name, email)

    def student_details(self):
        print(self.name, self.email, pwskills2.mobile_num)


print(pwskills2.mobile_num)
#899655565

pw_obj = pwskills2("pooja","pooja@gmail.com")

pw_obj.student_details()
#pooja pooja@gmail.com 899655565

print(pwskills2.mobile_num)
#899655565

pwskills2.change_number(558652635)

print(pwskills2.mobile_num)
#558652635

pw_obj.student_details()
#pooja pooja@gmail.com 558652635


#ADD FUNCTION IN THE CLASS

class pwskills3:

    mobile_num=899655565

    def __init__(self,name,email):
        self.name = name
        self.email = email

    @classmethod
    def change_number(cls,mobile):
        pwskills2.mobile_num = mobile

    @classmethod
    def details(cls, name, email):
        return cls(name, email)

    def student_details(self):
        print(self.name, self.email, pwskills2.mobile_num)


        
def course_details(cls, course_name):
    print("course name is",course_name)

    
pwskills3.course_details = classmethod(course_details)
pwskills3.course_details("data science")
#course name is data science


def mentor(cls, list_mentor):
    print(list_mentor)

    
pwskills3.mentor = classmethod(mentor)
pwskills3.mentor(["pooja","verma",21])
#['pooja', 'verma', 21]


#DELETE FUNCTION FROM THE CLASS

class pwskills4:

    mobile_num=899655565

    def __init__(self,name,email):
        self.name = name
        self.email = email

    @classmethod
    def change_number(cls,mobile):
        pwskills2.mobile_num = mobile

    @classmethod
    def details(cls, name, email):
        return cls(name, email)

    def student_details(self):
        print(self.name, self.email, pwskills2.mobile_num)

        
del pwskills4.change_number
pwskills4.change_number(46826296)
'''Traceback (most recent call last):
  File "<pyshell#24>", line 1, in <module>
    pwskills4.change_number(46826296)
AttributeError: type object 'pwskills4' has no attribute 'change_number' '''

delattr(pwskills4 , "details")
pwskills4.details("pooja","poojav@gmail.com")
'''Traceback (most recent call last):
  File "<pyshell#27>", line 1, in <module>
    pwskills4.details("pooja","poojav@gmail.com")
AttributeError: type object 'pwskills4' has no attribute 'details' '''

delattr(pwskills4, "mobile_num")
pwskills4.mobile_num
'''Traceback (most recent call last):
  File "<pyshell#30>", line 1, in <module>
    pwskills4.mobile_num
AttributeError: type object 'pwskills4' has no attribute 'mobile_num' '''

