#045
total = 0
while (total <51):
    total += int(input("enter number"))
    print("the total is :", total)
    if total >50 :
        break

#046
int1 = int(input("enter a number"))
while int1 <= 5:
    int1 = int(input("enter a number"))
print("the last number you entered", int1 )

    
#047

numbers = []
print("insert two numbers")
for i in range(2):
    numbers.append(int(input()))
sumOfNums = sum(numbers[:])
addAnother = input("Do you want to add another number")
while addAnother == 'y' :
    numbers.append(int(input("enter another num")))
    sumOfNums = sum(numbers[:])
    addAnother = input("Do you want to add another number")
print ("total is:" , sumOfNums)
    
    
#048
count = 0
guest = input("who you want to invite to party")
print(guest, "has now been invited")
count += 1
moreGues = input("Do you want to invite somebody else: yes/no")
while moreGues == 'yes':
    count +=1
    moreGues = input("Do you want to invite somebody else: yes/no")
print(count, "people are coming to party")
    

#049
compnum = 50
countt = 1
usernumber = int(input("enter a number"))
while usernumber != 50:
    if usernumber <50 :
        print("too low")
    elif usernumber >50:
        print("too high")
    usernumber = int(input("enter another number"))
    countt +=1
else: print("Well done. you took", countt, "attemps")


#050
numBet10and20 = int(input("enter a value between 10 and 20"))
while numBet10and20  < 10 or numBet10and20  > 20 :
    if numBet10and20  < 10:
        print("Too low")
        numBet10and20 = int(input("enter another value between 10 and 20")) 
    elif numBet10and20  > 20 :
        print("Too high")
        numBet10and20 = int(input("enter another value between 10 and 20"))
    else :
        break

print("thank you")



#051
num= 10
print("There are ",num," green bottles hanging on the wall, "\
      ,num," green bottles hanging on the wall"\
      ,"and if 1 green bottle should accidently fall")
num -= 1
while True:
    bottles=int(input('How many green bottles will be hanging on the wall?? '))
    
    if bottles == num:
        if num ==0:
            print("There are no more bottles hanging on the wall")
            break
        else:
            print("There will be ",num," green bottles on the wall")
            print("There are ",num," green bottles hanging on the wall, "\
              ,num," green bottles hanging on the wall"\
              ,"and if 1 green bottle should accidently fall")
            num -= 1
    
    elif ans != num:
        print("No,try again")
