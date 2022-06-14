import csv
import re
file=open('projects.csv','r')

reader = csv.reader(file)

projects=[]

for row in reader:
    projects.append(row)
# number=0
for item in projects:
    print(item)
    # number = number + 1
    # print(number)

###################delete

# deletethis = input("enter a project nunmber to delete it")
user = "zeko@gmail.com"

for line in projects:
    found =0
    project = line.split(",")
    if project[5] == user:
        found = 1

if found == 0:
    print("you don't have access")

lines = list()

members = input("Please enter a member's name to be deleted.")

with open('projects.csv', 'r') as readFile:

    reader2 = csv.reader(readFile)

    for row in reader2:

        lines.append(row)

        for field in row:

            if field == members:

                lines.remove(row)

with open('projects.csv', 'w') as writeFile:

    writer = csv.writer(writeFile)

    writer.writerows(lines)