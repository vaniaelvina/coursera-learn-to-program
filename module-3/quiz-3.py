"""
Question 1
Variable  dollars refers to the value 8. Select the expression(s) that produce True.

answer:
8 >= dollars
dollars == 8.0

Question 2
Variable cents refers to the value 34. Select the expression(s) that produce True.

answer:
not not cents >= 33
not cents < 12

Question 3
Variable dollars refers to the value 18 and variable cents refer to the value 53. Select the expression(s) that produce True.

answer:
(not dollars == 18) or cents == 53
not dollars < 10 and cents > 15

Question 4
The following is a valid Python expression, where x is a variable that refers to an int value:
3 <= x < 10
Select the expression that is equivalent to the one above. Remember that you can try this out in the Python shell.

answer:
3 <= x and x < 10

Question 5
What does the expression int(99.9)produce?

answer:
99

Question 6
if eggs % 12 == 0:
    return False
else:
    return True

answer:
return eggs % 12 != 0
return not eggs % 12 == 0

Question 7
Consider this code:
age1 = input("How old are you? ")
age2 = input("How old is your best friend? ")
The user enters the ages in years as whole numbers (e.g., 2).  Select the code fragment(s) that print the sum of the ages. Be sure to use Python 3.

answer:

print(int(age1) + int(age2))

x = int(age1)
y = int(age2)

Question 8
The math module has a function that finds the ceiling of a number (the smallest integral value greater or equal to the number). Assuming that the math module has already been imported, write an expression that calls the ceiling function from to find the ceiling of 84.2. 
Hint: In IDLE, 
import math and then use dir and help on the math module to determine the name of the function that you need to use.

answer: 
math.factorial(84.2)

Question 9
A program in assignment.py uses functions defined in question.py.  In order to call functions from the question module, what statement must appear in the assignment module?

answer:
import question

Question 10
What is printed when this code is executed?
def traffic_report(light):
    if light == 'red':
        return 'stop'
    elif light == 'yellow':
        return 'slow'
    elif light == 'green':
        return 'go'
        
print(traffic_report('yellow'))

answer:
slow

Question 11
What is printed when this code is executed?
def traffic_report(light):
    if light == 'red':
        return 'stop'
    elif light == 'yellow':
        return 'slow'
    elif light == 'green':
        return 'go'
        
print(traffic_report('orange'))

answer:
None

Question 12
Consider the following function definition:
def grade_report(grade):
    if grade >= 80:
        return 'excellent'
    elif grade >= 50:
        return 'pass'

answer:
grade_report(70)
grade_report(50)

Question 13
grade1 and grade2 represent two grades (floats) between 0.0 and 100.0, inclusive. A passing grade is greater than or equal to 50.   Select the code fragment(s) that prints the average of all passing grade(s). The printed value should be 0.0 if neither grade is a passing grade, the passing grade if exactly one grade is a passing grade, and the average of the two grades if both are passing grades.
Watch your ifs and elifs!

answer:
total = 0
grade_count = 0

if grade1 >= 50:
    total = total + grade1
    grade_count = grade_count + 1
if grade2 >= 50:
    total = total + grade2
    grade_count = grade_count + 1

if grade_count > 0:
    print(total / grade_count)
else:
    print(0.0)

Question 14
Question 14
Including the global frame for the main program, how many stack frames exist at the current point of execution (indicated by the Python Visualizer with blue highlighting)?  Remember that the red arrow indicates the line that is about to be executed.
To answer this, you should use the Python Visualizer for this code: greeting.py

answer:
1

Question 15
Including the global frame for the main program, how many stack frames exist at the current point of execution?  Remember that the red arrow indicates the line that is about to be executed.
To answer this, you should use the Python Visualizer for this code: greeting.py

answer:
3

Question 16
Including the global frame for the main program, how many stack frames exist at the current point of execution?  Remember that the red arrow indicates the line that is about to be executed.
To answer this, you should use the Python Visualizer for this code: greeting.py

answer: 
3
"""