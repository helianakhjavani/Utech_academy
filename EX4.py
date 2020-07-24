#012
integer1= int(input("Enter yout first umber"))
integer2 = int(input("Enter yout second umber"))

if integer1 > integer2 :
    print(integer1 , " " , integer2)
else:
    print(integer2 , " " , integer1)
#013
integer3 = int(input("Enter number less than 20"))
if integer3 >20 :
    print("Too high")
else:
    print("Thank you")
#014
integer4 = int(input("Enter number between 10 and 20"))
if integer4 <20 and integer4 >10 :
    print("Thank you")
else:
    print("Incorrect answer")
#015
colour = input("enter your favourite colour ")
if colour == "red" or colour == "RED":
    print("I like red too")
else:
    print("I dont like ", colour, " I prefer red")


#016
answer1  = input("Is it raining? ").lower()
if answer1 == 'yes':
    answer2  = input("Is it windy? ").lower()
    if answer2 == 'yes':
        print("It is too windy for an umbrella")
    else:
        print("Take an umbrella")
else:
    print("Enjoy yout day")


#017
age  = int(input("Enter your age"))
if age >= 18:
    print("You can vote")
elif age == 17:
     print("You can learin to drive")
elif age == 16:
    print("You can buy a lottery ticket")
else:
    print("You can go Trick or Training")

#018
integer5  = int(input("Enter a number"))
if integer5 <10 :
    print("Too low")
elif integer5 >10 and integer5 <20:
    print("Correct")
else:
    print("Too high")

#019
integer6  = int(input("Enter 1, 2 or 3"))
if integer6 ==1:
    print("Thank you")
elif integer6 == 2:
    print("Well done")
elif integer6 ==3:
    print("Correct")
else:
    print("Error message")
    
    
    


