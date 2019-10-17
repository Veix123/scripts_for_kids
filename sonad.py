#!/usr/bin/python3

import csv
import random   
import sys

db = []


with open('data.txt') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    line_count = 0
    for row in csv_reader:
        db.append(row)

random.shuffle(db)

print("Anni inka irregular verbs")
print("Sisesta kolm vormi ja eralda need tühikuga")

points = 0
tries= 0

try:
    for row in db:
        points_available=1
        while True:
            answer = input(row[3]+ ": ")
            answers = answer.split()
            
            tries += 1
            if(answers == row[0:3]):
                print("Õige\n")
                points += points_available
                break
            else:
                print("Vale\n")
                points_available=0
except KeyboardInterrupt:
    print("VALMIS! Punkte kokku: " + str(points) + "/" + str(tries) + " = " + str(points/float(tries) * 100) + "%")
    sys.exit()




    print("VALMIS! Punkte kokku: " + str(points) + "/" + str(tries) + " = " + str(points/float(tries) * 100) + "%")
