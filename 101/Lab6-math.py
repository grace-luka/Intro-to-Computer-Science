# Grace Luka and Jaden Nguyen
# CSCI 101 - Section G, H
# Python Lab 6
# References:
# Time:

import csv
import string

math_file = input(f'MATHFILE> ')
output_file = input(f'OUTPUTFILE> ')

with open(math_file, 'r') as myFile:
    with open(output_file, 'w') as outFile:
        filereader = csv.reader(myFile, delimiter = ',')
        filewriter = csv.writer(outFile, delimiter = ',')


        for row in filereader:
            stop = row.index('==')
            LHS = int(row[0])
            for j in range(1,stop,2): #For loop for all left sides of '=='
                if row[j] == '+':
                    LHS += int(row[j+1])
                elif row[j] == '-':
                    LHS -= int(row[j+1])
                elif row[j] == '/':
                    LHS /= int(row[j+1])
                elif row[j] == '*':
                    LHS *= int(row[j+1])
                elif row[j] == '**':
                    LHS **= int(row[j+1])
                elif row[j] == '%':
                    LHS %= int(row[j+1])
            LHS = round(LHS)
                    
            RHS = int(row[stop+1])
            for k in range(stop+2,len(row),2): #For loop for all right sides of '=='
                if row[k] == '+':
                    RHS += int(row[k+1])
                elif row[k] == '-':
                    RHS -= int(row[k+1])
                elif row[k] == '/':
                    RHS /= int(row[k+1])
                elif row[k] == '*':
                    RHS *= int(row[k+1])
                elif row[k] == '**':
                    RHS **= int(row[k+1])
                elif row[k] == '%':
                    RHS %= int(row[k+1])
            RHS = round(RHS)

            physics = (RHS == LHS) #physics because jaden is great at physics but also kinda bad

            
            filewriter.writerow([LHS, RHS, physics])
            print(LHS)
            print(RHS)
            print(physics)
        


