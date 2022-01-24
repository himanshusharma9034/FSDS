#!/usr/bin/env python
# coding: utf-8
1. Why are functions advantageous to have in your programs?
AND: Functions helps in providing the reusability.




2. When does the code in a function run: when it's specified or when it's called?
ANS: On call


3. What statement creates a function?
ANS: def is a keyword used to create a function





4. What is the difference between a function and a function call?
ANS: Function is used and helpful in providing the reusability.
	Function call is used to call the builded function by the user.
	
	
	
5. How many global scopes are there in a Python program? How many local scopes?
ANS: one, which resides on the main body and will reside until the programme get terminates, where as local scopes resides inside the funtion and can be used only inside the function's. 
	These scopes are created by the user and will vanish onces user terminates the programme.






6. What happens to variables in a local scope when the function call returns?
ANS: the local variable resides inside the function and will be vanish after returning from the call.
def example():
	a = 'rrr'
	return a
as in the example a is defined as as string of 'rrr', but onces we get out of the function there is no value allocated to the variable a.






7. What is the concept of a return value? Is it possible to have a return value in an expression?
ANS:- In making the function we used return as return is not a NONETYPE datatype





8. If a function does not have a return statement, what is the return value of a call to that function?
ANS: NONE





9. How do you make a function variable refer to the global variable?
ANS By declaring the variables globally.





10. What is the data type of None?
ANS: NONETYPE



11. What does the sentence import areallyourpetsnamederic do?
ANS: import a module named areallyourpetsnamederic.


12. If you had a bacon() feature in a spam module, what would you call it after importing spam?
ANS: spam.bacon()



13. What can you do to save a programme from crashing if it encounters an error?
ANS: Will use the logging and exception handiling(try and except), where logging will generating the log files which will help 
to rectify the errors, dates etc. 



14. What is the purpose of the try clause? What is the purpose of the except clause?
ANS: Try and Except clause are used in Exception Handling, to avaoid any kind of mishappening.


