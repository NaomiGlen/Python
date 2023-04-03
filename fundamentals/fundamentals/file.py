num1 = 42 #variable declaration,data type-number initialized
num2 = 2.3 #variable declaration,data type-float initialized
boolean = True #variable declaration, data type-boolean initialized
string = 'Hello World' #variable declaration,data type-string initialized
pizza_toppings = ['Pepperoni', 'Sausage', 'Jalepenos', 'Cheese', 'Olives'] #variable declaration,data type-list initialized
person = {'name': 'John', 'location': 'Salt Lake', 'age': 37, 'is_balding': False} #variable declaration,data type-dictionary initialized
fruit = ('blueberry', 'strawberry', 'banana') #variable declaration,data type-tuple initialized
print(type(fruit)) #print to console,type check
print(pizza_toppings[1]) #print to console,list access value
pizza_toppings.append('Mushrooms') #list add value
print(person['name']) #print to console, dictionary access value
person['name'] = 'George' #dictionary change value
person['eye_color'] = 'blue' #dictionary change value
print(fruit[2]) #print to console, tuple access data

if num1 > 45: #conditional-if, evaluation
    print("It's greater") #print to console
else: #conditional-else
    print("It's lower") #print to console

if len(string) < 5: #conditional-if, evaluation
    print("It's a short word!") #print to console
elif len(string) > 15: #conditional-elif, evaluation
    print("It's a long word!") #print to console
else: #conditional-else
    print("Just right!") #print to console

for x in range(5): #for loop starting at 0 and going up until 5
    print(x) #print to console
for x in range(2,5): #for loop starting at 2 and going up until 5
    print(x) #print to console
for x in range(2,10,3): #for loop starting at 2 and going up until 10 by incremements of 3
    print(x) #print to console

x = 0 #variable declaration, data type- number initialized
while(x < 5): #while loop, evaluation
    print(x) #print to console
    x += 1 #increment increase

pizza_toppings.pop() #list delete value at end
pizza_toppings.pop(1) #list delete value at index

print(person) #print to console of dictionary
person.pop('eye_color') #dictionary delete value
print(person) #print to console of dictionary

for topping in pizza_toppings: #for loop through a list
    if topping == 'Pepperoni': #conditional-if
        continue #for loop-continue
    print('After 1st if statement') #print to console
    if topping == 'Olives': #conditional-if
        break #for loop-break

def print_hello_ten_times(): #function declaration
    for num in range(10): #for loop starts at 0 and goes up until 10
        print('Hello') #print to console

print_hello_ten_times() #function call 

def print_hello_x_times(x): #function declaration with parameter
    for num in range(x): #for loop until a given number
        print('Hello') #print to console

print_hello_x_times(4) #function call arguement of 4

def print_hello_x_or_ten_times(x = 10): #function declaration with default parameter
    for num in range(x): #for loop until x(10)
        print('Hello') #print to console

print_hello_x_or_ten_times() #function call goes to 10 times
print_hello_x_or_ten_times(4) #function call goes to 4 times


"""
Bonus section
"""

# print(num3)
# num3 = 72
# fruit[0] = 'cranberry'
# print(person['favorite_team'])
# print(pizza_toppings[7])
#   print(boolean)
# fruit.append('raspberry')
# fruit.pop(1)