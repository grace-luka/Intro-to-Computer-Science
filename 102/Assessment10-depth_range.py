# Grace Luka
# CSCI 102 - Section B
# Assesment 10
# References: Megan
# Time:

import csv
with open('formations.csv', 'r') as myFile:
    with open('formations_parsed.csv', 'w') as myOutFile:
        filewriter = csv.writer(myOutFile, delimiter = ',')
        filereader = csv.reader(myFile, delimiter=',')
        header = ['Depth','Start Depth','End Depth','Difference in Depth','Formation','Age of Formation']
        filewriter.writerow(header)
        i = 0
        for row in filereader:
            if i == 0:
                i += 1
                continue
            depth = row[0]
            var = depth.split('-')
            start_depth=float(var[0])
            end_depth=float(var[1])
            difference = end_depth - start_depth
            formation = row[1]
            if start_depth < 700:
                age_of_form = 'Paleocene'
            else:
                age_of_form = 'Cretaceous'
            filewriter.writerow([depth,start_depth,end_depth,f'{difference:.2f}',formation,age_of_form])

'''
            print(depth)
            print(start_depth)
            print(end_depth)
            print(difference)
            print(formation)
            print(age_of_form)
'''
