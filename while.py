# Declare variables.

number = -1
num_counter = 0
average = 0
user_num = int(input("Enter your number here "))

# Programme will run until -1 is entered.
while user_num != number: 

    # keep track of how many numbers entered.
    num_counter += 1 
    average += user_num 
    user_num = int(input("Enter another number here "))
    # Incase first number entered
if (num_counter==0): print (average) 
else:
    print ("The total average for numbers entered is", average/num_counter)
