import math; from math import *; 
import cmath;
import warnings; from warnings import *
import functions;
import time;
import os;
from getkey import getkey, keys;

print("Welcome to calculator. For a list of functions, type 'help'\n\n");


off = False;

warnings.filterwarnings("ignore");

while not off:

  fact = False;
  helpMenu = False;
  clearing = False;
  Enter = False;

  # takes input from user and makes sure no error occurs when they input "ctrl + c"
  try:
    userInput = input("").lower();
  except KeyboardInterrupt:
    userInput = "off";

  #removes spaces from equation
  if " " in userInput.lower():
      userInput = functions.removeSpaces(userInput);


  #avoids returning an error if user hits enter
  if userInput == "":
    Enter = True;


  #off button 
  if userInput.lower() == "off":
    off = functions.off(off);


  #help menu
  if userInput.lower() == "help":
    helpMenu = functions.help(helpMenu);  
          

  #clear screen button
  if userInput.lower() == 'clear':
    clearing = functions.clear(clearing);
    






    
    
  if '!' in userInput:
    # FACTORIAL HERE !!!!!!!!!!!!!
    factCount = userInput.count('!');
    
    for i in range(factCount):

      factNum = [];

      userInputSplit = functions.split(userInput);

      factLoc = userInputSplit.index('!');

      originalFactLoc = factLoc

      while True:
        
        factLoc -= 1
        

        item = userInputSplit[factLoc]

        if not item in '1234567890.':
          break

        else:
          factNum.insert(0,item)

        if factLoc == 0:
          break


      factNum = ''.join(factNum);

      calcdNum = factorial(int(factNum));

      userInput = ''.join(userInputSplit)

      if factLoc == 0:
        userInput = userInput[1:factLoc+1] + str(calcdNum) + userInput[originalFactLoc+1:]
      else:
        userInput = userInput[0:factLoc+1] + str(calcdNum) + userInput[originalFactLoc+1:]
      

         








  #ans function
  if 'ans' in userInput.lower():
    
    try:
      userInput = functions.ans(userInput, prevAns);
    except NameError:
      userInput = "Oops, sowwy, that function doesn't workies uwu"

  #final exec function that calculates userInput
  if not off and not helpMenu and not clearing and not Enter:

    try:
      exec('y='+userInput)
      print("               ", y, "\n-------------------------");
      prevAns = y

    except Exception:
      print("           ERROR: SYNTAX\n-------------------------");
