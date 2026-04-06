import random
listlength = 0
randomnum = 0
randomlist = []
topran = 0
botran = 0
listcounter = 0
minvalue = 0

listlength = int(input("Please enter a list length for the list of random numbers: "))
while listlength <= 0:
    listlength = int(input("That is not a valid number. Please enter a positive number: "))
    
botran = int(input("Please enter the bottom end of the range for random numbers: "))
while botran <= 0:
    botran = int(input("That is not a valid number. Please enter a positive number: "))
    
topran = int(input("Please enter the top end of the range for random numbers: "))
while topran <= botran:
    topran = int(input("That number is not higher than the bottom number. Please enter a number higher than: ", botran))
minvalue=topran

while listcounter <= listlength:
    randomnum = random.randint(botran, topran)
    randomlist.append(randomnum)
    listcounter += 1
    print(randomlist)

for item in randomlist:
    if item < minvalue:
        minvalue = item
    print("The current minimum value is: ", minvalue)

print("The final minimum value is: ", minvalue)

#This is a random comment added by Santiago post initial upload
