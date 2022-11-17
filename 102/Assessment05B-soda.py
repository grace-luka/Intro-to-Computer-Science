#   Grace Luka
#  ​ CSCI 102 – Section B
#   Assessment 05B
#   References: 
#   Time: 25 minutes

empties = int(input(f"Enter the number of empty bottles in Blaster's possession at the start og the day.\nEMPTIES> "))
found = int(input(f"Enter the number of empty bottles that Blaster found during the day.\nFOUND> "))
cost = int(input(f"Enter the number of empty soda bottles required to buy a new soda.\nCOST> "))

total = []

while empties >= cost:
    empties_a = empties // cost
    total.append(empties_a)
    empties = empties_a + (empties % cost)

new_total = found + (empties % cost)
while new_total >= cost:
    new_total_a = new_total // cost
    total.append(new_total_a)
    new_total = new_total_a + (new_total % cost)

print(f'OUTPUT {sum(total)}')
