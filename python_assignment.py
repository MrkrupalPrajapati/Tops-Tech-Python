# -*- coding: utf-8 -*-
"""Python Assignment.ipynb

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1URtyJpA1Ue7q33JrBcheETke-nu7kUF3

#Python Assignment
#####by:- krupal prajapati

1) Write a Python program to check if a number is positive, negative or
zero.
"""

data = int(input("please enter the number :- "))

if data > 0:
  print("Number is positive")
elif data < 0:
  print("number is Negative")
elif data == 0:
  print("Number is ZERO")

print(data)

"""2) Write a Python program to get the Factorial number of given numbers."""

data =  int(input("Enter the number"))
facto = 1
for i in range(2,data+1):
  facto =  facto*i
print(f"Factorial of {data} is",facto)

"""3) Write a Python program to get the Fibonacci series of given range."""

# prompt: Write a Python program to get the Fibonacci series of given range

# 3) Write a Python program to get the Fibonacci series of given range.
n_terms = int(input("Enter the number of terms: "))

# first two terms
n1, n2 = 0, 1
count = 0

# check if the number of terms is valid
if n_terms <= 0:
  print("Please enter a positive integer")
elif n_terms == 1:
  print("Fibonacci sequence upto", n_terms, ":")
  print(n1)
else:
  print("Fibonacci sequence:")
  while count < n_terms:
    print(n1)
    nth = n1 + n2
    # update values
    n1 = n2
    n2 = nth
    count += 1

"""4) Write python program that swap two number with temp variable
and without temp variable.
"""

# with Temp :-

def swap_with_temp(x,y):
  temp = x,
  x = y,
  y = temp
  return("this is x :",x,"this is y :",y)

swap_with_temp(10,20)


#without Temp :-

def without_temp(x,y):
  x,y = y,x
  return("this is x :",x,"this is y :",y)

without_temp(10,20)

"""5) Write a Python program to find whether a given number is even
or odd, print out an appropriate message to the user.
"""

def even_odd(a):
  if a % 2 == 0:
    return (f"Number {a} is an even Number")
  else:
    return (f"Number {a} is an odd Number")

even_odd(10)

"""6) Write a Python program to test whether a passed letter is a vowel
or not.
"""

def check_vowel(a):
  if len(a) == 1 and a.isalpha():
    if a in ("aeiou"):
      return("it is a vowel")
    elif a in ("AEIOU"):
      return("it is a vowel")
    else:
      return("it is not vowel")

check_vowel("c")

"""7) Write a Python program to sum of three given integers. However, if
two values are equal sum will be zero.
"""

def equal_sum_zero(a,b,c):
  if a == b or a == c or b == c:
    return(0)
  else:
    return("your grand total of give three integer is : ",a+b+c)

i1 = int(input("please enter the first number : "))
i2 = int(input("please enter the second number : "))
i3 = int(input("please enter the third number : "))

equal_sum_zero(i1,i2,i3)

"""8) Write a Python program that will return true if the two given
integer values are equal or their sum or difference is 5.
"""

def QA8(a,b):
  if (a == b) or (a + b == 5) or (abs(a - b) == 5):
    return True
  else:
    return False

QA8(2,7)

"""9) Write a python program to sum of the first n positive integers."""

def QA9(x):
  if x > 0:
    total = sum(range(1,x+1))
    return(f"Sum of the first {x} positive integers is {total}")
  else:
    return("please enter a positive integer")

QA9(4)

"""10) Write a Python program to calculate the length of a string."""

def find_len_string(a):
  return (len(a))

str1=input("enter the string : ")
find_len_string(str1)

"""11) Write a Python program to count the number of characters
(character frequency) in a string
"""

def find_frequency(a):
  for i in a:
    print(i,":",a.count(i))

str1=input("enter the string : ")
find_frequency(str1 )

"""12) Write a Python program to count occurrences of a substring in a string."""

string = input("enter the string : ")
substring = input("enter the sub string that need to be count : ")
count = string.count(substring)
print(f"The substring '{substring}' occurs {count} times in the string '{string}'.")

"""13) Write a Python program to count the occurrences of each word in a
given sentence
"""

sentence = input("Enter a sentence: ")
words = sentence.split()

print("Word frequency:")
for word in set(words):
    print(f"{word}: {words.count(word)}")

"""14) Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string.
"""

string1 = input("enter the first string : ")
string2 = input("enter the second string : ")

new_str1 = string2[0:2] + string1 [2:]
new_Str2 = string1[0:2] + string2 [2:]

print(new_str1 , new_Str2)

"""15) Write a Python program to add 'in' at the end of a given string (length
should be at least 3). If the given string already ends with 'ing' then
add 'ly' instead if the string length of the given string is less than 3,
leave it unchanged.
"""

def Q15A(s):
  if len(s) < 3:
    print(s)
  elif s[-3:] == "ing":
    print(s + "ly")
  else:
    print(s + "ing")

Q15A("king")

"""16) Write a Python function to reverses a string if its length is a multiple
of 4.
"""

def Q16A(a):
  if len(a) % 4 == 0:
    return a[::-1]
  else:
    return a

input = input("enter the string : ")
Q16A(input)

"""17) Write a Python program to get a string made of the first 2 and the last
2 chars from a given a string. If the string length is less than 2, return
instead of the empty string.
"""

def Q17A(st):
  new_string = ""
  if len(st) < 2:
     print(new_string)
  else:
     new_string = st[0:2] + st[-2:]
     print(new_string)

user_input = input("Enter the string: ")
Q17A(user_input)

"""18) Write a Python function to insert a string in the middle of a string."""

def Q18A(f1, f2):
    mid = len(f1) // 2  # Find the middle index
    return f1[:mid] + f2 + f1[mid:]  # Insert f2 in the middle of f1

ui1 = input("Enter the first string: ")
ui2 = input("Enter the second string: ")

print(Q18A(ui1, ui2))  # Print the result

"""19) Write a Python function to get the largest number, smallest num
and sum of all from a list.
"""

list1 = [1,2,3,4,5]
print("minimum number :-",min(list1))
print("maximum number :-",max(list1))
print("Total sum of the list :-",sum(list1))

"""20) Write a Python program to count the number of strings where the string
length is 2 or more and the first and last character are same from a given list
of strings.
"""

def Q20A(user_string):
  count = 0
  for words in user_string:
    if len(words) >= 2 and words[:1] == words[-1:]:
      count += 1
  return count

user_input = ["krupal","jeel","MAM","NooN"]
Q20A(user_input)

"""21) Write a Python program to remove duplicates from a list."""

def remove_duplicate(list1):
  uniqur_list = []
  for i in list1:
    if i not in uniqur_list:
      uniqur_list.append(i)
  return uniqur_list

user_list = ["krupal","jeel","MAM","NooN","krupal"]
remove_duplicate(user_list)

"""22) Write a Python program to check a list is empty or not."""

knight = []
krupal = [1,2,3]

def List_empty_or_not(ul):
  if len(ul) >= 1:
    return("list is not empty")
  else:
    return("list is empty")

List_empty_or_not(knight)

"""23) Write a Python function that takes two lists and returns true if they
have at least one common member.
"""

list1 = ["kp","mp","fp","bp"]
list2 = ["ding","dang","dung","kp"]

def Q23A(L1,L2):
  for i in L1:
    if i in L2:
      return True
  return False

Q23A(list1,list2)

"""24) Write a Python program to generate and print a list of first and last 5
elements where the values are square of numbers between 1 and 30.
"""

sqare_list = []
for i in range(1,31):
   sqare = i*i
   sqare_list.append(sqare)
print(sqare_list)

first_5_element = sqare_list[0:5]
last_5_element = sqare_list[-5:]

final_list = []
final_list = first_5_element + last_5_element
print("final_list_with_first5_&_last5_elements" , final_list)

"""25) Write a Python function that takes a list and returns a new list with
unique elements of the first list.
"""

def Q25A(L1):
  new_list = []
  for i in L1:
    if i not in new_list:
      new_list.append(i)
  return new_list

LIST1 = ["KP","KP","JP","JP","SP","DP","KN","KN"]
Q25A(LIST1)

"""26) Write a Python program to convert a list of characters into a string."""

def Q26A(ch_list):
  stri = ""
  for i in ch_list:
    stri = stri + i
  return stri

list = ["k","r","u","p","a","l"]
Q26A(list)

"""27) Write a Python program to select an item randomly from a list."""

import random as rand
list = ["kp","mp","jp","rp","hp"]
print(rand.choice(list))

"""28) Write a Python program to find the second smallest number in a list."""

list = [1,4,3,6,8,9]
print(list.sort())
seconde_smallest_number = list[1]
print("seconde_smallest_number :-",seconde_smallest_number )

"""29) Write a Python program to get unique values from a list"""

def Q29A(L1):
  new_list = []
  for i in L1:
    if i not in new_list:
      new_list.append(i)
  return new_list

LIST1 = [1,4,3,6,8,9,9,4,3,2,1,10,12,12]
Q29A(LIST1)

"""30) Write a Python program to check whether a list contains a sub list"""

Main_List = ["k","R","U","P","A","L"]
Sub_List = ["U","P","A","n"]

for i in Sub_List:
  if i in Main_List:
     print(f"yes {i} exhist in the main list")
  else:
    print(f"no {i} not exhist in the main list")

"""31) Write a Python program to split a list into different variables."""

main_list = [10,20,30]

A,B,C = main_list

print(A)
print(B)
print(C)

"""32) Write a Python program to create a tuple with different data types."""

T = (90,3.14,"hy",[10,20,23],{'a':10,'b':20})

print("Main Tuple :- ",T)
print()
for item in T:
  print(f"{item} and it's Type {type(item)}")

"""33) Write a Python program to unzip a list of tuples into individual lists."""

list_of_tuple = [(1,1),(2,2),(3,3)]

lst1,lst2 = zip(*list_of_tuple)

l1=list(lst1)
l2=list(lst2)

list_one = l1
list_two = l2

print(l1)
print(l2)

"""34) Write a Python program to convert a list of tuples into a dictionary."""

list_of_tuple = [("A",1),("B",2),("C",3)]

DICT1 = dict(list_of_tuple)

print(DICT1)
DICT1.keys()

"""35) How will you create a dictionary using tuples in python?"""

# List of tuples
tuple_list = [("a", 1), ("b", 2), ("c", 3)]

# Dictionary comprehension
my_dict = {key: value for key, value in tuple_list}

print(my_dict)

"""36) Write a Python script to sort (ascending and descending) a
dictionary by value.
"""

dict1 = {'a':10,
         'b':15,
         'c':2,
         'd':12}

# Ascending order
print(dict(sorted(dict1.items(), key=lambda x: x[1])))

# Descending order
print(dict(sorted(dict1.items(), key=lambda x: x[1], reverse=True)))

"""37) Write a Python script to concatenate following dictionaries to create
a new one.
"""

dict1 = {'a':1}
dict2 = {'b':2}

new_dect =  dict1 | dict2
print(new_dect)

"""38) Write a Python script to check if a given key already exists in a
dictionary.
"""

main_script = {'a':1,'b':2}

def Q38A(s):
  if s in main_script:
    return("yes the key is exists")
  else:
    return("No the key is not exist")

Q38A('c')

"""39) Write a Python script to print a dictionary where the keys are
numbers between 1 and 15.
"""

keys = []
values = ['krupal','manoj','hetal','jeel','divya','neeta','naresh','ankita','riddhi','vikas','nikunj','bhhomi','chirag','sweta','ruhan']
dictionary = {}
for i in range(1,16):
 # for j in values:
    dictionary[i] = values[i-1]
print(dictionary)

dictionary.keys()
dictionary.values()

"""40) Write a Python program to check multiple keys exists in a dictionary"""

keys_to_check = [1,2,5]

if all(keys in dictionary for keys in keys_to_check):
  print("yes all the keys are exists")
else:
  print("every keys are not present in the main dictionary")

"""41) Write a Python script to merge two Python dictionaries"""

#41) Write a Python script to merge two Python dictionaries
dict1 = {'1':'krupal'}
dict2 = {'2':'jeel'}

dict1.update(dict2)
print(dict1)

"""42) Write a Python program to map two lists into a dictionary"""

keys = [1,2,3,4,5]
values = ['manoj',"jeel","hetal","krupal","rajvi"]

dict3 = {}

for i in keys:
  dict3[i] = values[i-1]
print(dict3)

"""43) Write a Python program to find the highest 3 values in a dictionary"""

dict4 = {"a":12,"b":13,"c":2,"d":15,"e":17}
top_3_values = sorted(dict4.items(), key=lambda x: x[1], reverse=True)[:3]

# Displaying result
print("Top 3 highest values:")
for key, value in top_3_values:
    print(f"{key}: {value}")

"""44) Write a Python program to combine values in python list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount':
300}, o {'item': 'item1', 'amount': 750}]
"""

data = [
    {'item': 'item1', 'amount': 400},
    {'item': 'item2', 'amount': 300},
    {'item': 'item1', 'amount': 750}
]

# Dictionary to store combined values
result = {}

# Iterate through the list
for entry in data:
    item = entry['item']
    amount = entry['amount']

    # Add or update the amount in the result dictionary
    result[item] = result.get(item, 0) + amount

# Display the result
print(result)

"""45) Write a Python program to create a dictionary from a string.
Note: Track the count of the letters from the string.
"""

from collections import Counter

text = "apple"
letter_count = dict(Counter(text))

print(letter_count)

"""46) Sample string:
'w3resource'
"""

from collections import Counter

text = 'w3resource'
letter_count = dict(Counter(text))

print(letter_count)

"""47) Write a Python function to calculate the factorial of a number (a
nonnegative integer)
"""

def factorial(n):
    if n == 0 or n == 1:
        return 1  # Base case: 0! = 1 and 1! = 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result

num = int(input("Enter a non-negative integer: "))
if num < 0:
    print("❌ Factorial is not defined for negative numbers.")
else:
    print(f"Factorial of {num} is {factorial(num)}")

"""48) Write a Python function to check whether a number is in a given range"""

def check_in_range(num, start, end):
    if start <= num <= end:
        return f"✅ {num} is in the range [{start}, {end}]"
    else:
        return f"❌ {num} is NOT in the range [{start}, {end}]"

# Example usage
num = int(input("Enter a number: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(check_in_range(num, start, end))

"""49 ) Write a Python function to check whether a number is perfect or not."""

def check_in_range(num, start, end):
    if start <= num <= end:
        return f"✅ {num} is in the range [{start}, {end}]"
    else:
        return f"❌ {num} is NOT in the range [{start}, {end}]"

# Example usage
num = int(input("Enter a number: "))
start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

print(check_in_range(num, start, end))


## or

numbers = list(range(1, 101))
def c_i_r(x):
  if x in numbers:
    print("yes it is between this number")
  else:
    print("No it is not between the given range")

number = int(input("enter the number"))
c_i_r(number)

"""50) Write a Python function that checks whether a passed string is
palindrome or not
"""

def is_palindrome(s):
    # Remove spaces and convert to lowercase for accurate comparison
    cleaned_str = s.replace(" ", "").lower()

    # Check if the string is the same when reversed
    if cleaned_str == cleaned_str[::-1]:
        return f"✅ '{s}' is a palindrome."
    else:
        return f"❌ '{s}' is NOT a palindrome."

# Example usage
text = input("Enter a string: ")
print(is_palindrome(text))

"""51) Write a Python program to read an entire text file."""

from google.colab import files
uploaded = files.upload()

with open('file_read.txt', 'r') as file:
    content = file.read()
    print(content)

"""52) Write a Python program to append text to a file and display the text."""

from google.colab import files
uploaded = files.upload()

with open('file_read.txt','a') as file:
  file.write(" krupal is amazing")
  file.close()

with open('file_read.txt','r') as file:
  content = file.read()
  print(content)

"""53) Write a Python program to read first n lines of a file."""

from google.colab import files
uploaded = files.upload()

with open('file_read.txt','r') as file:
  first_line = file.readline()
  print(first_line)

"""54) Write a Python program to read last n lines of a file."""

from google.colab import files
uploaded = files.upload()


file_name = list(uploaded.keys())[0]

with open(file_name, 'r') as file:
    lines = file.readlines()


n = int(input("Enter the number of lines to read: "))


print(''.join(lines[-n:]))

"""55) Write a Python program to read a file line by line and store it into a list"""

from google.colab import files
uploaded = files.upload()


file_name = list(uploaded.keys())[0]

with open(file_name, 'r') as file:
    lines = file.readlines()


print("File content as a list:")
print(lines)

"""56) Write a Python program to read a file line by line store it into a variable."""

from google.colab import files
uploaded = files.upload()

# Read file content and store it in a variable
file_name = list(uploaded.keys())[0]  # Automatically gets the uploaded file name

with open(file_name, 'r') as file:
    content = file.read()  # Reads the entire file into a variable

# Display the content
print("File content stored in a variable:\n")
print(content)

"""57) Write a python program to find the longest words."""

from google.colab import files
uploaded = files.upload()

# Read file and find the longest word(s)
file_name = list(uploaded.keys())[0]  # Automatically gets the uploaded file name

with open(file_name, 'r') as file:
    words = file.read().split()  # Split file content into words

# Find the longest word(s)
max_length = max(len(word) for word in words)
longest_words = [word for word in words if len(word) == max_length]

# Display the result
print("Longest word(s):", longest_words)
print("Length of longest word(s):", max_length)

"""58) Write a Python program to count the number of lines in a text file."""

from google.colab import files
uploaded = files.upload()

# Read file and count the number of lines
file_name = list(uploaded.keys())[0]  # Automatically gets the uploaded file name

with open(file_name, 'r') as file:
    line_count = sum(1 for line in file)  # Count each line

# Display the result
print(f"Total number of lines in the file: {line_count}")

"""59) Write a Python program to count the frequency of words in a file."""

from google.colab import files
uploaded = files.upload()

file_name = list(uploaded.keys())[0]

with open(file_name, 'r') as file:
    content = file.read().lower().split()


from collections import Counter
word_count = Counter(content)


print("Word Frequency in the File:")
print(word_count)

"""60) Write a Python program to write a list to a file."""

my_list = ['apple', 'banana', 'cherry', 'orange']


with open('my_list.txt', 'w') as file:
    for item in my_list:
        file.write(item + '\n')

print("List has been written to 'my_list.txt'.")

"""61) Write a Python program to copy the contents of a file to another file."""

from google.colab import files
uploaded = files.upload()

# Get the uploaded file name
source_file = list(uploaded.keys())[0]

# Copy contents in one step
open('copied_file.txt', 'w').write(open(source_file).read())

print("Contents have been copied successfully!")

"""62) Write python program that user to enter only odd numbers, else
will raise an exception.
"""

try:
    num = int(input("Enter an odd number: "))
    if num % 2 == 0:
        raise ValueError("That's an even number! Please enter an odd number.")
    print(f"Great! {num} is an odd number.")
except ValueError as e:
    print(e)