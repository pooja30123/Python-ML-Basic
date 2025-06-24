#STATIC METHOD

#NORMAL
class pwskills :
    def students_details(self, name, email_id, number):
        print(name, email_id, number)

pw = pwskills()
pw.students_details("pooja", "verma", 658629665)
#pooja verma 658629665


#USING STATIC METHOD (NOT NEEDED TO CREATE OBJ)

class pwskills1 :
    def students_details(self, name, email_id, number):
        print(name, email_id, number)
    @staticmethod
    def mentor_class(list_mentor):
        print(list_mentor)
    def mentor(self,mentor_list):
        print(mentor_list)
        
stu1 = pwskills1()
stu2 = pwskills1()
stu3 = pwskills1()

stu1.mentor(["p","o"])    #WITHOUT STATIC METHOD WE HAVE TO ASSIGN VALUE ALL TIME
#['p', 'o']


pwskills1.mentor_class(["pooja","verma"])   #NOT CREATE OBJ ALSO NOT REPETATED
#['pooja', 'verma']


#STATIC METHOD IN CLASS METHOD
class pwskills2 :

    def students_details(self, name, mail_id, number):
        print(name, mail_id, number)

    @staticmethod
    def mentor_class(list_mentor):
        print(list_mentor)

    @classmethod
    def class_name(cls):
        cls.mentor_class(["pooja","verma"])

    def mentor(self,mentor_list):
        print(mentor_list)

pwskills2.class_name()
#['pooja', 'verma']

#STATIC METHOD IN STATIC METHOD
class pwskills2 :

    def students_details(self, name, mail_id, number):
        print(name, mail_id, number)
    
    @staticmethod
    def mentor_mail_id(mail_id_mentor):
        print(mail_id_mentor)

    @staticmethod
    def mentor_class(list_mentor):
        pwskills2.mentor_mail_id(["pooja@gmail.com","verma@gmail.com"])
        print(list_mentor)

    @classmethod
    def class_name(cls):
        cls.mentor_class(["pooja","verma"])

    def mentor(self,mentor_list):
        print(mentor_list)

pwskills2.mentor_class(["pooja","verma"])
#['pooja@gmail.com', 'verma@gmail.com']
#['pooja', 'verma']


#STATIC METHOD IN INSCTANCE CLASS
class pwskills2 :

    def students_details(self, name, mail_id, number):
        print(name, mail_id, number)

    @staticmethod
    def mentor_mail_id(mail_id_mentor):
        print(mail_id_mentor)

    @staticmethod
    def mentor_class(list_mentor):
        pwskills2.mentor_mail_id(["pooja@gmail.com","verma@gmail.com"])
        print(list_mentor)

    @classmethod
    def class_name(cls):
        cls.mentor_class(["pooja","verma"])

    def mentor(self,mentor_list):
        print(mentor_list)
        self.mentor_class(["pooja","verma"])

        
pw=pwskills2()
pw.mentor(["pooja","verma"])
#['pooja', 'verma']
#['pooja@gmail.com', 'verma@gmail.com']
#['pooja', 'verma']

