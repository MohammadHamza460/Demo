import random as rd

y = ["1","2","3","4","5","6","7","8","9","0"]

def create():
    global y
    FIRST_NAME = input("Enter your name: ")
    for x in FIRST_NAME:
        y.append(x)
    
def game():
    global y
    print(y[rd.randint(0,len(y)-1)]+y[rd.randint(0,len(y)-1)]+y[rd.randint(0,len(y)-1)]+y[rd.randint(0,len(y)-1)]+y[rd.randint(0,len(y)-1)])
    y = ["1","2","3","4","5","6","7","8","9","0"]


