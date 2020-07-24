#069
countries = ('iran', 'france', 'germany', 'canada', 'spain')
print(countries[:])
country = input("choose on of the printed countries")
print(countries.index(country))


#070
numOfCountry = int(input("Enter a number"))
print(countries[numOfCountry])

#071
sports = ['swimming','tennis']
sport = input("What is your favourite sport?")
sports.append(sport)
sports.sort()
print(sports)
#072

courses = ['math', 'sport', 'litreture', 'geography', 'history', 'english']
print(courses[:])
course = input("which of these subjects courses you don't like?")
courses.remove(course)
print(courses)
#073
food = []
food.append(input("enter food 1"))
food.append(input("enter food 2"))
food.append(input("enter food 3"))
food.append(input("enter food 4"))
dic = {}
for i in range(4):
    dic[i+1] = food[i]
print(dic)
removenum = int(input("which do you want to get rid of?"))
del dic[removenum]

    

#074
colors = ['red', 'yellow' , 'blue' , 'green' , 'purple',
          'pink', 'black', 'white', 'brown', 'orange']
start = int(input("enter start number"))
end = int(input("enter end number"))
print(colors[start:end])


#075

ThreeDigitNumbers = [123,234,567,875]
for i in ThreeDigitNumbers:
    print(i)
newnum = int(input("enter new number"))
if newnum in ThreeDigitNumbers:
    print(ThreeDigitNumbers.index(newnum))
else:
    print("that is not in the list")


#076
print("enter the names of three people you want to invite to a party")
guests = []
for i in range(3):
    guests.append(input())
answer = input("do you want to add another>?")
while answer == 'yes':
    answer = input()
    guests.append(answer)
    answer = input("do you want to add another>?")
else:
    print("you have  invited" , len(guests) , "guests")


#77

print("enter the names of three people you want to invite to a party")
guests = []
for i in range(3):
    guests.append(input())
answer = input("do you want to add another>?")
while answer == 'yes':
    answer = input()
    guests.append(answer)
    answer = input("do you want to add another>?")
else:
    print(guests[:])

print("type one of the names on the list")
nameOnaList = input()
print(guests.index(nameOnaList))
print("Do you still want to invite", nameOnaList ,"?")
ans = input()
if ans == 'no':
    guests.remove(nameOnaList)
    print(guests[:])
    


#78

proglist = ['navad','football','serial','film']
for i in proglist:
    print(i)
print("enter a show an position")
show = input()
position = int(input())
proglist.insert(position, show)
for i in proglist:
    print(i)




#79
nums = []
print("enter numbers")
for i in range(3):
    nums.append(int(input()))
    print(nums)
answer78 = input("do you still want the last number")
if answer78 == "no" :
    nums.pop()
    print(nums)
    











    
