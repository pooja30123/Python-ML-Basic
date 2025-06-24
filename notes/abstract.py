#sceleton of abstract class
import abc
class pwskills:
    @abc.abstractmethod
    def student_details(self):
        pass
    @abc.abstractmethod
    def student_assignment(self):
        pass
    @abc.abstractmethod
    def student_marks(self):
        pass

    
class student_details(pwskills):
    def student_details(self):
        return "this is meth for taking student details"
    def student_assignment(self):
        return "this is meth for assign details for perticular details"

    
class data_science_masters(pwskills):
    def student_details(self):
        return "this will return a student details for data science masters"
    def student_assignment(self):
        return "this will give you a student assignment detailes for data science master"

    
dsm=data_science_masters()
dsm.student_details()
#'this will return a student details for data science masters'
sd=student_details()
sd.student_details()
#'this is meth for taking student details'

