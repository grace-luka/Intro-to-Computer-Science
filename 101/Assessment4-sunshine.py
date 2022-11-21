# Grace Luka
# CSCI 101 - Section G
# Python Assessment 5
# References: 
# Time:

import csv


# Make sure to follow the provided instructions for each of the steps on Canvas!
# Step 1: Month based stats
def monthly_summary(filename, month_abbr):
    with open('sunshine_hours_by_city.csv','r', encoding='utf-8') as myFile:
        filereader = csv.reader(myFile, delimiter= ',')
        count = 0
        month_list = []
        for row in filereader:
            if count == 0:
                index = row.index(month_abbr)
                count += 1
            else:
                month_list.append(float(row[index]))
        #print(list1)

    average1 = round((sum(month_list)) / (len(month_list)))
    min1 = round(min(month_list))
    max1 = round(max(month_list))
                     
    output1 = f'OUTPUT Average: {average1} | Minimum: {min1} | Maximum: {max1}'
    return output1

# Step 2: City based stats
def city_summary(filename, city, country):
    with open('sunshine_hours_by_city.csv','r', encoding='utf-8') as myFile:
        filereader = csv.reader(myFile, delimiter= ',')
        city_hours_list = []
        for row in filereader:
            if row[1] == city:
                country = row[0]
                var = 2
                while var <= 13:
                    city_hours_list.append(float(row[var]))
                    var += 1
                #print(city_hours_list)
    average2 = round((sum(city_hours_list))/(len(city_hours_list)))
    min2 = round(min(city_hours_list))
    max2 = round(max(city_hours_list))
    output2 = f'OUTPUT Average: {average2} | Minimum: {min2} | Maximum: {max2}'
    return output2


# Step 3: Sunshine threshold
def cities_in_range(filename, minimum, maximum):
    with open('sunshine_hours_by_city.csv','r', encoding='utf-8') as myFile:
        filereader = csv.reader(myFile, delimiter= ',')
        cities_in_range_list = []
        i = 0
        for row in filereader:
            if i ==0:
                i += 1
                continue
            hours_list = []
            var = 2
            return_list = []
            while var <= 13:
                hours_list.append(float(row[var]))
                var += 1
            #print(sum(hours_list))
            sum_hours = float(sum(hours_list))
            print(sum_hours)
            if sum_hours >= minimum and sum_hours <= maximum:
                valid_element = row[1] + row[0]
                return_list.append(valid_element)
        print(return_list)


# Extra credit: Validating your input file
def valid_csv(filename):
    pass # placeholder line - delete before writing code here


# Step 4: Tying it all together
if __name__ == "__main__":
    print(f'Here comes the sun!')
    print(f'Provide the name of your csv file contining sunshine duration data')
    filename = input(f'FILENAME> ')
    print(f'------------------------------------------')
    print(f'Which of the following would you like to do?')
    print(f'(1) See the states for a specific month')
    print(f'(2) See the states for a specific city')
    print(f'(3) Find the cities that fit my sunshine preference')
    print(f'------------------------------------------')
    choice = int(input(f'CHOICE> '))
    if choice == 1:
        print(f'Enter the month abbreviation')
        month_abbr = input(f'MONTH> ')
        print(monthly_summary(filename, month_abbr))

    elif choice == 2:
        print(f"Enter the city's name")
        city = input(f'CITY> ')
        print(f"Enter the country's name")
        country = input(f'COUNTRY> ')
        print(city_summary(filename, city, country))

    elif choice == 3:
        print(f'Enter the minimum amount (in hours) of yearly sunshine')
        minimum = input(f'MIN> ')
        print(f'Enter the maximum amount (in hours) of yearly sunshine')
        maximum = input(f'MAX> ')
        print(cities_in_range(filename, minimum, maximum))
    elif choice == "i'm done":
        print(f'Goodbye!')
    else:
        print(f'Please enter a valid number')
        







