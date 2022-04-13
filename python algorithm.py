
# Given an integer, , perform the following conditional actions:

# If  is odd, print Weird
# If  is even and in the inclusive range of 2 to 5 , print Not Weird
# If  is even and in the inclusive range of 5 to 10, print Weird



# def conditional_test(n):
#     if n % 2 != 0:
#         return "Weird"
#     if (n % 2 == 0) and (n in range(2, 5)):
#         return "Not Weird"
#     if (n % 2 == 0) and (n in range(5, 10)):
#         return "Weird"
#     else:
#         return "Number is not within range"
    

# print(conditional_test(26))

# The provided code stub reads two integers, a and b, from STDIN.

# Add logic to print two lines. The first line should contain the result of integer division, a //b . The second line should contain the result of float division,  a/b .

# No rounding or formatting is necessary.

# def division_integer(a, b):
#     return a//b
   
# def division_float(a, b):
#     return a/b
   
# print(division_float(10, 3))   
    
# print(division_integer(10, 2))

# def newCode(a,b):
#         return a+b, a-b, a*b

# print(newCode(3,5))

#lists can store different data types arrays [] can only store one data type

#Creating a for in loop with using range

# def square_number(n):
#     squares = []
#     for i in range(n +1):
#         squares.append(i * i)
#     return squares
        
        
# print(square_number(10))

# def range_number(n,b):
#     squares = []
#     for i in range(n, b+1):
#         squares.append(i * i)
#     return squares

# print(range_number(10,12))




# new_list=[ x for x in range(10)]

# print(new_list)

# #filtered_list = [ x for x in range(50) if x % 2 == 0 if x % 5 == 0]
# #print(filtered_list)

#!Using List comprehensions

from asyncore import loop


names=["lauren", "Ally", "Kirstin", "Tina"]

# # l_names= [name for name in names if name.startswith("l")] 

# print(l_names)

# def L_names(name):
#     lnames = []
#     for i in name:
#         if i.startswith("l"):
#                 lnames.append(i)
#         return lnames
    
    

# print(L_names(names))

# def new_number(b):
#         numbers_10 = [x for x in range(b) if x > 3]
#         return (numbers_10)
               
# print (new_number(7))

# #Turn below into list comprehension
# j=[0,1,2,3,4,5]
# # 

# def loopFunction(list):
#     plus_six=[]
#     # iterates through the list, the range is set to the length of the list
#     for x in range(len(list)):
#         if x < 3:
#             x += 6 
#             plus_six.append(x)
#     return plus_six  
# print(loopFunction(j))


# j=[0,1,2,3,4,5]



# # # 
# def loopFunction(list):
#         plus_six = [number for number in list if number < 3 ]
#         return plus_six

# print(loopFunction(j))
# n =  [i for i in range(0,5+1)]
# print(n)


# def newCode(a,b):
#         print (a+b) 
#         print (a-b)
#         print (a*b)
        
# print(newCode(3,5))

# list = [3,4,7,1]

# list.sort(key=int)


    
# print(list)

# def sort_function(list):
#     new_list = []
#     list.sort(key=int)
#     new_list.append(list[1])
#     return new_list


    
# print(sort_function(list))

# python_students = [['Harry', 37.21], ['Berry', 37.21],  ['noodle', 37.21], ['Tina', 37.2], ['Akriti', 41], ['Harsh', 39]]

# def second_lowest_grades(list): 
#   second_index=[]
#   final_list=[]
#   newlist=sorted(list, key=lambda v: (v[1], v[0]))
#   second_index = newlist[1]
# #   return newlist
#   for x in newlist:
#         if x[1] == second_index[1]:
#            final_list.append(x)
#            final_list.append(second_index)
#            return final_list
       

  
# print(second_lowest_grades(python_students))

#! above we are sorting a nested loop using a lambda as a key. we are sorting this by the test scores so that is the first element in the list v[1]

# def split_and_join(line):
#     split_by_delimiter = line.split(" ")
#     split_by_delimiter = "-".join(split_by_delimiter)
#     return split_by_delimiter
   
# print(split_and_join('this is a string'))


# def print_full_name(first, last):
#     return (f"hello,{first} {last} you just delved into python")
    
# print(print_full_name("Tony", "Bolony"))



# def endPalindrome()

#! Anagram test that takes in two sentences 

#first need to get ride of each space in sentences
#second need to get ride of capital letters
# assign each letter a number value with a for of loop

new = "G o d"
nope = "G o d"

def anagram(str1, str2):
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()
    if len(str1) != len(str2):
        return False
    count = {}
    for letter in str1:
        if letter in count:
            count[letter] += 1
        else: 
            count[letter] = 1
    for letter in str2:
        if letter in count:
            count[letter] -= 1
        else: count[letter] = 1
    for k in count:
        if count[k] != 0: 
           return False
    return True
   
    
print(anagram(new, nope))

# Reference youtube video for refresher
