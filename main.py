import re
import csv
import datetime


import datetime

def validate(date_text):

    day, month, year = date_text.split('/')

    isValidDate = True
    try:
        datetime.datetime(int(year), int(month), int(day))
    except ValueError:
        isValidDate = False

    if(isValidDate):
        print("Input date is valid ..")
        return True
    else:
        print("Input date is not valid..")

from datetime import datetime

def validate(date_text):
    try:
        if date_text != datetime.strptime(date_text, "%Y-%m-%d").strftime('%Y-%m-%d'):
            raise ValueError
        return True
    except ValueError:
        return False


regex = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'


def check(email):
    # pass the regular expression
    # and the string into the fullmatch() method
    if (re.fullmatch(regex, email)):
        print("Valid Email")
        return True

    else:
        print("Invalid Email")

def checkMobile(phone):
    val = True
    Pattern = re.compile("^01(0|1|2|5){1}[0-9]{8}")
    if Pattern.match(phone):
        print("Valid Phone number")
        return True
    else:
        print("Invalid Phone number")

print("user registration form")

Firstname = input("please enter your first name : ")
Lastname = input("please enter your last name : ")
while True:
    email = input("enter a valid email : ")
    if check(email):
        break
password = input("enter password : ")

while True:
    confirm = input("confirm your password : ")
    if (password==confirm):
        break
    else:
        print("password doesn't match")
        continue


while True:
    phone = input("Enter your phone number : ")
    if checkMobile(phone):
        break
print("\nRegistration complete\n")


with open(r"C:\Users\karaw\Downloads\Python\lab3\users.csv", 'a+', encoding='UTF-8', newline='') as csvFile:
    # csvwriter = csv.writer(csvFile, delimiter=',')
    # csvwriter.writerow([Firstname, Lastname, email, password, phone])
    csvFile.seek(0)
    users = csvFile.readlines()
# #######################################################3 LOGIN section
    print("login")
    email2=input("Login with email")
    password2=input("Enter password")

for u in users:
    found: int = 0
    user = u.split(",")
    if user[2] == email2:
        if user[3] == password2:
            print(user)
            found = 1
if found == 0:
    print("not found")

#
# #######################################################3projects section
# print("Chose the operation you want to make from the list :\n")
# print("1 - view all projects")
# print("2 - Add new project")
# print("3 - Edit a project")
# print("4 - Delete a project")
# print("5 - logout")
# choice=input("")
# if choice == 1:
#

# ############################################## ADD project


projectname=input("Enter project name: ")
details=input("Enter project details: ")
target=input("Enter targeted amount: ")
while True:
    starting = input("Enter starting date ")
    if validate(starting):
        break
    else:
        print("incorrect date format")


ending = input("Enter end date: ")
validate(ending)

with open(r"C:\Users\karaw\Downloads\Python\lab3\projects.csv", 'a+', encoding='UTF-8', newline='') as csvFile:
    csvwriter = csv.writer(csvFile, delimiter=',')
    csvwriter.writerow([projectname, details, target, starting, ending, email])
    # csvFile.seek(0)
    # users = csvFile.readlines()

########################################################### view all
file=open('projects.csv','r')

reader = csv.reader(file)

projects=[]

for row in reader:
    projects.append(row)

number=0
for item in projects:
    print(item)
    number = number + 1
    print(number)

#########################################################delete



