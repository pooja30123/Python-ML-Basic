#SPECIAL MAGIC OR DUNDER METHOD

dir(int)

dir(str)

a=5
a + 100
#105
a.__add__(100)
#105


class pwskills:
    def __init__(self):
        self.mob_no = 8693848441

        
pw = pwskills()
pw.mob_no
#8693848441


class pwskills:

    def __new__(cls):
        print("this is new")
        
    def __init__(self):
        print("this is my init")
        self.mob_no = 8693848441

pw = pwskills()
#this is new

class pwskills1:
    
    def __init__(self):
        self.mob_no = 8693848441

        
class pwskills1:

    def __init__(self):
        self.mob_no = 8693848441
    def __str__(self):
        return "this is magic call"

    
pw1 = pwskills1()
pw1
#<__main__.pwskills1 object at 0x0000014D3D4E1910>
print(pw1)
#this is magic call
