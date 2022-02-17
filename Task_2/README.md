# TASK-2

Task two is all about writing two pseudo code and flow chart for them

## Problem - 1

Write pseudocode and flowchart for a program that outputs ‘True’ if a given number is divisible by 3 and ‘False’ otherwise, without using the ‘%’ operator explicitly (like N % 3 == 0).
NOTE: You can use ‘%’ operator to separate each digit of the given number(like N % 10).

>> Sample Input 1 :123
>> Sample Output 1 : True

>> Sample Input 2 : 98
>> Sample Output 2 : False

> Approach : 
>> As we're instructed not to use modulous operator with '3' 
>> We'll find divisiblity with a different approach 
>> Create two variables one with datatype integer and other with real numbers
>> divide the given integer with 3 as we are checking divisibitily for3
>> And store the result in a real/ float data type intger 
>> Which stores decimal value if needed
>> Store this real value in a integer variable which converts decimal to integer if present
>> if both the integer value and real value is equal then it is divisible
>> As , if its not divisible real value will have something like "x.kk" if its divisible it 
>> will be like "x.00" , so if its divisible the values will be equal.

## Problem - 2

Write pseudocode and flowchart for program that prints Nth fibonacci number. (Nth Fibonacci Number denoted as F(N), F(0)=0, F(1)=1, F(2)=1, F(3)=2,…)

>> Sample Input 1 : 5
>> Sample Output 1 : 5

>> Sample Input 2 : 11
>> Sample Output 2 : 89

> Approach
>> Normal fibanocci logic of adding both values , swapping them 
>> And printing the N th value of the series using for loop 
>> which itterates n times.
