# json MODULE

import json
data={
      "name":"pooja verma",
      "emil_id":"pooja123@gmail.com",
      "phone_no": 8693848441,
      "subject":["Maths","Python","Java"]
     }
with open("data.json",'w') as f:
    json.dump(data,f)

with open("data.json" , 'r') as f:
    data1=json.load(f)

data1
#{'name': 'pooja verma',
# 'emil_id': 'pooja123@gmail.com',
# 'phone_no': 8693848441,
# 'subject': ['Maths', 'Python', 'Java']}
data1['subject'][1]
#'Python'

#CSV MODULE
import csv
data=[["name","email_id","phone_number"],
      ["pooja","pooja@gmail.com",85798228],
     ["shanti","shanti@gmail.com",6282688]]

with open("data.csv",'w') as f:
    writer = csv.writer(f)   
    for i in data:
        writer.writerow(i)

with open("data.csv",'r') as f:
    read_data = csv.reader(f)
    for i in read_data:
        print(i)

'''['name', 'email_id', 'phone_number']
['pooja', 'pooja@gmail.com', '85798228']
['shanti', 'shanti@gmail.com', '6282688']'''


#BINARY NUMBER
with open("test.bin",'rb') as f:
    print(f.read())

with open("test.bin",'rb') as f:
    print(f.read())

#b'\x01\x02\x03c569'
    
