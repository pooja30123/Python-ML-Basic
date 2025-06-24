class data_science:
    def syllabus(s):
        print("this is my syllubus for my data science")

        
class web_dev:
    def syllabus(s):
        print("this is my syllabus for web dev")

        
def class_parcer(a):
    for i in a:
        i.syllabus()

        
data_science =data_science()
web_dev = web_dev()
a=[data_science,web_dev]
class_parcer(a)
#this is my syllubus for my data science
#this is my syllabus for web dev
