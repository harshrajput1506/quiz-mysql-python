# Developed By Harsh Rajput, Priya Yadav & Priyanshu Rana 12 D


# Imports Required Packages
import mysql.connector as pym  
import random

# MySql Connection

mycon = pym.connect(host="localhost", user="root", passwd="root", database="quiz")
if not mycon.is_connected():
        print("Not Connected")

# Get Data from MySql Table
def getData():
        Dlist = []
        cursor = mycon.cursor()
        query = "select * from questions"
        cursor.execute(query)
        data = cursor.fetchall()
        for element in data:
                question = element[1]
                options = [element[2], element[3], element[4], element[5]]
                answer = element[6]
                dataDict = {"question":question, "options":options, "answer":answer}
                Dlist.append(dataDict)
        mycon.close() # Close The Connection
        return Dlist
# Function - Play Quiz Game
def play():
        print("\n==========QUIZ START==========")
        score = 0

        dataList = getData()  # Data List from SQL
        
        for i in range(10):
                
                no_of_questions = len(dataList)
                rn = random.randint(0, no_of_questions-1)  # Random Integer for Random Question
                Qnum = str(i+1)    
                question = dataList[rn]["question"]   #Question
                print('\nQ'+Qnum+".",question,"\n")
                for option in dataList[rn]["options"]:
                        print(option)       # Options
                answer = input("\nEnter your answer: ")
                choosedAns = answer[0].upper()
                if(choosedAns == 'A' or choosedAns == 'B' or choosedAns == 'C' or choosedAns == 'D'):
                        correctAns = dataList[rn]["answer"][0]  # Correct Answer
                        if(choosedAns == correctAns):  # Check User Answer with Correct Answer
                                print("\nYou are Right")
                                score += 1 # Getting Score 
                        else:
                                print("\nYou are Wrong")
                                del dataList[rn]
                else:
                        print("\nINVALID OPTION")
        print("\nFINAL SCORE:", score, "Out of 10")
        
# Function - Rules of The Game
def rules():
        print('''\n==========RULES==========
1. Each round consists of 10 random questions. To answer, you must press A/B/C/D (case-insensitive).
Your final score will be given at the end.
2. Each question consists of 1 point. There's no negative point for wrong answers.
        ''')

# Function - About US 
def about():
        print('''\n==========ABOUT US==========
This project has been created by Harsh Rajput, Priya Yadav & Priyanshu Rana of Class 12 D.
It is a basic Python Quiz Game Program.''')


# Main Intitalization
if __name__ == "__main__":
        choice = 1
        while choice != 7:
                print('\n=========WELCOME TO HYPER QUIZ==========')
                print('-----------------------------------------')
                print('1. PLAY QUIZ')
                print('2. SEE INSTRUCTIONS ON HOW TO PLAY THE GAME')
                print('3. EXIT')
                print('4. ABOUT US')
                choice = int(input('ENTER YOUR CHOICE: '))
                if choice == 1:
                        play()
                elif choice == 2:
                        rules()
                elif choice == 3:
                        break
                elif choice == 4:
                        about()
                else:
                        print('WRONG INPUT. ENTER THE CHOICE AGAIN')
