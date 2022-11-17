#   Grace Luka
#  ​ CSCI 102 – Section B
#   Assessment 06B
#   References:
#   Time: 50 minutes

print('Count of numbers to estimate:')
num_count = int(input('COUNT> ')) #ask for count
print('Input each number to estimate.')


list = [] #make inputs into a list
for i in range(num_count): #each input for count
    num = float(input(f'NUMBER> '))
    list.append(num)



for i in list: #start with first index in list
    initial_guess = 10 #initialize initial_guess to 10
    num_iterations = 0
    while True:
        better_guess = (initial_guess + i / initial_guess) / 2
        num_iterations += 1
        if initial_guess == better_guess:
            break
        else:
            initial_guess = better_guess
        #print(initial_guess)
        #print(num_iterations)
    print(f'OUTPUT After {num_iterations} iterations, {i}^0.5 = {initial_guess :.2f}')
