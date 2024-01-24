# Create variables to use as counters.
# One forwards, one backwards.
# Set the range needed to work within.

row = 1
new_row = 5

for i in range (1,10):
    if row <5: 

        # Making sure our loop stops counting at 5.
        # Taking into consideration range always starts at zero.
        print("* "*row)
        row = row+1
    
    # Entering the second conditional onece the count has reached 5.
    else:
        print ("* "*new_row)
        new_row = new_row -1