import mysql.connector as pym
import json

mycon = pym.connect(host="localhost", user="root", passwd="root", database="sakila")
if not mycon.is_connected():
        print("Not Connected")
cursor = mycon.cursor()
query = "create database if not exists quiz1"
cursor.execute(query)

mycon = pym.connect(host="localhost", user="root", passwd="root", database="quiz1")
if not mycon.is_connected():
        print("Not Connected")

cursor = mycon.cursor()
query = "create table if not exists questions(id int primary key AUTO_INCREMENT, question text, optionA text, optionB text, optionC text, optionD text, answers text)"
cursor.execute(query)

def insertData(int, data):
    if not len(data) == int :
        question = data[int]["question"]
        options = data[int]["options"]
        answer = data[int]["answer"]
        print(question, options ,answer)
        query = "insert into questions(question, optionA, optionB, optionC, optionD, answers) values('{}', '{}', '{}', '{}', '{}', '{}')".format(question, options[0], options[1], options[2], options[3], answer)
        cursor.execute(query)
        mycon.commit()
        print("Record Added")
        int = int+1
        print(int)
        insertData(int, data)
    else:
        mycon.close()

with open('assets/questionBank.json', 'r+') as f:
    data = json.load(f)
    i = 0
    insertData(i, data)





    
        
        


        

