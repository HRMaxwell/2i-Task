
#########################################################
#   Name:       Harry Maxwell                           #
#   Date:       06/02/22                                #
#   Project:    2i coding task                          #
#########################################################

# Getting the user's input of A and X
# When i was testing the code I used X = 8 and A = 2
# Assuming only integers are only being used

X = int(input("Please enter a value for X"))
A = int(input("Please enter a value for A"))

# One assumption is that i have assigned Ainput to keep the original value of A

Ainput = A

# I am using while loops as a condition needs to be met before the code moves to the next stage
# I have commented out the print statements as these were used for testing

while A != X:
    A = A * Ainput
    # print (A)
while A != 2*X:
    A = A + 1
    # print (A)
while A != 3*X:
    A = A + 2
    # print (A)

