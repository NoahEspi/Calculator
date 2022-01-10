import os
import time
from getkey import getkey, keys

#splits a string into a list of characters
def split(word):
  return list(word);


# function that turns off the calculator
def off(offVar):

  offVar = True;
  
  os.system('clear');
  print("           Powering off..");
  time.sleep(1);
  os.system('clear');

  return offVar;
  

# clears the console screen
def clear(clearVar):

  os.system('clear');
  print("Welcome to calculator. For a list of functions, type 'help'.\n\n");

  clearVar = True;
  return clearVar;


# changes ever instance of "ans" in userInput into the previous answer given
def ans(expression, previousAns):

  ansCount = expression.lower().count('ans')

  for i in range(ansCount):

    ansLocation = expression.lower().find('ans');

    expression = expression[0:ansLocation] + str(previousAns) + expression[ansLocation+3:];

  return expression;


def factorial():
  pass


# removes all spaces from userInput
def removeSpaces(expression):

  spaceCount = expression.count(" ");

  for i in range(spaceCount):

    spaceLocation = expression.find(" ");

    expression = expression[0:spaceLocation] + "" + expression[spaceLocation+1:];

  return expression;


# displays the help menu 
def help(helpVar):

  helpVar = True;

  os.system('clear');

  print("""Here is a list of functions:
Currently, some functions/processes may not work as intended.

  
Display functions:
 help → lists all available functions
 clear → clears the screen
 off → turns the calculator off
  
Math functions:
 + → addition
 - → subtraction
 * → multiplication
 / → division
 ** → exponent
 % → returns the remainder of a division problem
 ans → returns answer to previous equation
 pi → returns pi
 e → returns Euler's number
 tan(number) → returns tangent of 'number'
 cos(number) → returns cosine of 'number' 
 sin(number) → returns sine of 'number'
 sqrt(number) → returns the square root of 'number'
 factorial(number) → returns the factorial of 'number'
 
 """);

  print("Press any key to return back to calculator.");

  getkey();

  os.system('clear');

  print("Welcome to calculator. For a list of functions, type 'help'.\n\n");

  return helpVar;