"""
Question 1
Which of the following results in a syntax error?

answer:
"yes
no"
'yes
no'

Question 2
Which of the following results in a syntax error?

answer:
"He said, "Yes!""
''That's okay'''
'3/'


Question 3
The following is printed by a print function call:
yesterday
today
tomorrow

answer:
print('yesterday\ntoday\ntomorrow')
print('''yesterday
today
tomorrow''')


Question 4
The following is printed by a print function call:
hello-how-are-you

answer:
print('hello'+'-'+'how'+'-'+'are'+'-'+'you')
print('hello-'+'how-are-you')

Question 5
Consider this code fragment:
>>> def announce_location(country):
    # Missing function body
>>> instructor_location = announce_location('Canada')
>>> print(instructor_location)
Canada

answer:
return country


Question 6
Consider this code fragment:
>>> def announce_location(country):
    # Missing function body

>>> instructor_location = announce_location('Canada')
Canada
>>> print(instructor_location)
Canada

Select the missing function body from the options below.

answer:
print(country)
return country

Question 8
What is the first step of the Design Recipe?

answer:
Examples

Question 9
What is the last step of the Design Recipe?

answer:
Test

Question 10
What is the Type Contract for the following function definition?
def is_passing_grade(grade):
    """Return 'pass' if grade is at least 50 and return 'fail' otherwise.
    >>> is_passing_grade(45)
    'fail'
    >>> is_passing_grade(80.5)
    'pass'
     """

answer:
(number) -> str

Question 11
What is the Type Contract for the following function definition?
def total_vowels(word1, word2):
    """Return the number of vowels in words word1 and word2.
    >>> total_vowels('hello', 'hi')
    3
    """

answer:
(str,str) -> int

'''
Question 12
According to the Description of function get_oldest, what value should be returned by the Example function call?
def get_oldest(age1, age2):
    ''' (int, int) -> int

    Return the oldest of the two ages, age1 and age2.
    
    >>> get_oldest(27, 22)
    ???
    '''
answer:
27
'''

Question 13
Here is an insufficient docstring for function euro_to_dollars:

answer:
It doesn't say what the function returns.
It doesn't mention the parameters by name.

Question 14
Two function definitions are saved in the same file:
A function 
count_vowels has one parameter, a word, and returns the number of vowels in that word. A function count_consonants has one parameter, a word, and returns the number of consonants in that word.
To determine the number of letters in a word, write a one-line body for the following function that calls both 
count_vowels and count_consonants:

def count_letters(word):
    """ (str) -> int

    Return the number of letters in word.
    >>> count_letters('hello')
    5
    >>> count_letters('bonjour')
    7
    """ 
    # Write the one-line function body that belongs here.

note:
do not call any functions other than those listed above
do not use any unnecessary parentheses

answer:
return count_vowels(word)+count_consonants(word)


Question 15
Two function definitions are saved in the same file:
A function get_capital has one string parameter that represents a country and returns its capital.
A function longer has two string parameters and returns the longer of the two strings.
Variables country1 and country2 refer to str values. Write a one-line expression that produces the longer of the capitals of country1 and country2. Your expression should involve calls on both get_capital and longer.
Note: 
do not call any functions other than those listed above
do not use any unnecessary parentheses

answer:
longer(get_capital(country1), get_capital(country2))

Question 16
What is the value of average after the following code is executed?
grade1 = 80
grade2 = 90
average = (grade1 + grade2) / 2
grade1 = 100

answer:
85.0

Question 17
Below is an image of the Python Visualizer in action. The line with the red arrow (line 15) is about to be executed. When we press Forward, function convert_to_minutes will be called, control will move to line 11 of the code (the first line of that function), and a new stack frame will be created containing variable num_hours. What value will num_hours refer to then? (We are looking for a value, not a memory address.)
(If the image is too small, right-click on it and open it in a new browser tab. Then you can zoom in.)

answer:
5

Question 18
The line with the red arrow (line 15) is about to be executed. After stepping through to the end of the code below (we can do this by pressing the Last button), how many variables (excluding those that refer to functions) will be on the stack?  Recall that the stack is represented by the images on the left-hand side of the model.  (If the image is too small, right-click on it and open it in a new browser tab. Then you can zoom in.)

answer: 
2

"""