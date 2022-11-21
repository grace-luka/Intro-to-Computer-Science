#   Grace Luka
#   CSCI 102 - Section B
#   Assessment 12C
#   References:
#   Time: 45 minutes


# Function 1 ---------------------------

def load_file(filename):
    with open(filename, 'r') as myFile:
        lines = []
        contents = myFile.readlines()
        for i in contents:
            i = i.strip()
            lines.append(i)
    return lines

# Function 2 ---------------------------

def update_string(string1, string2, num):
    #string1 = list(string1)
    new_string = string1[:num] + string2 + string1[num+1:]
    print(new_string)

# Function 3 ---------------------------

def find_word_count(mylist, string):
    count = 0
    for i in mylist:
        var = i.count(string)
        count += var
    print(count)

# Function 4 ---------------------------

def score_finder(players, scores, string):
    string = string[0].upper() + string[1:]
    for i in players:
        i = i.lower()
        #print(i)
    if string not in players:
        #print(string)
        print('OUTPUT player not found')
    else:
        index = players.index(string)
        #print(index)
        print(f'OUTPUT {string} got a score of {scores[index]}')

# Function 5 ---------------------------

def union(scores, players2):
    end_list = []
    for i in scores:
        if i not in players2:
            end_list.append(i)
    for j in players2:
        if j not in end_list:
            end_list.append(j)
    return end_list

# Function 6 ---------------------------

def intersect(players2, players):
    endlist = []
    for i in players2:
        if i in players:
            endlist.append(i)
    print(endlist)

# Function 7 ---------------------------

def not_in(players2, players):
    final_list = []
    for i in players2:
        if i not in players:
            final_list.append(i)
    return final_list