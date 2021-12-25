from datetime import date
import os, sys

today = date.today()
save = ""
name = ""
nerd = ""
load = 'BASIC Memory'

def Go(num):
    """
    Go(num)
    #Execute the code for inputed time.
    """
    for i in range(num):
        exec(save)

def findNum(word):
    """
    findNum(word)
    #Identify the inputed word is digit or not.
    """
    for i in word:
        if i.isdigit():
            return True
    return False

def eliminate(word):
    """
    eliminate(word)
    #Eliminate the first word from the string line.
    """
    return " ".join(word.split()[1:])

"""
Program start
"""
rose = "© Blake Gouthro and JinHo Mo | DEMO Rosewell BASIC | V1.3 | Rosewell Software | 2021 - " + str(today.year) + " ©"
print(rose)

print("Enough Basic Bytes Free")
print("Ready")

import subprocess, os, sys, random, webbrowser

content = ""

while True:
    line = input()
#goto
    if "goto" in line.lower():
        Go(int(line.split()[-1:][0]))
        continue
    
    if findNum(line):
        save += eliminate(line) + "\n"
        continue
#Help
    if line == "Help" or line == "help":
      print('''--Help-- Commands
GoTo (num) - runs and repeats code (num) amount of times
Help - list all the features of BASIC
Save - Allows you to save BASIC programs to a file
Run - allows you to run BASIC programs
quit - Quits Rosewell BASIC
List - list the PROGRAM saved in memory
Load - loads an external PROGRAM
Clear - Allows you to clear your PROGRAM code from memory
Dir - Lists the PROGRAM Directory
?Syntax Error? - means something was typed in wrong''')
#save
    if line == "Save" or line == "save":
        print("Would you like to save your program?[y/n]")
        answer = input()
        if answer == "No" or answer == "no" or answer == "N" or answer == "n":
          print("Ready")
          continue
        if answer == "Yes" or answer == "yes" or answer == "Y" or answer == "y":
            print("Enter File name.(the Extension '.py' is not required")
            linename = input()
            file = open(linename + ".py", "w")
            file.write(save)
            file.close()
            print("Ready")
            continue
#run    
    if line == "Run" or line == "run":
        exec(save)
        print("Ready")
        continue
#quit
    if line == "quit" or line == "Quit" or line == "No" or line == "no":
        print("Goodbye")
        break
#list        
    if line == "list" or line == "List":
        print(save)
        continue
#load        
    if line == "load" or line == "Load":
        nerd = input("Enter PROGRAM name: " )
        with open(nerd, "r") as file:
            save = "".join(file.readlines())
        stats = os.stat(nerd)
        print('''-----Directory-----
memory   PROGRAM   ext''')
        print(stats.st_size, 'Bytes' + '    ' + nerd)
        print(str(sys.getsizeof(save)) + " Bytes" + "     System Memory.prg")
        print(str(sys.getsizeof(load)) + " Bytes" + '     ' + str(load))
        print('Back to BASIC')
        continue
            
        print(rose)
        print("Ready")
        continue
#Space
    if line == "":
        continue
#Directory
    if line == "Dir" or line == "dir" or line == "Directory" or line == "directory":
        enter = input("Load a file into Dir?[type file name if yes/ type no or quit to exit dir]")
        if enter == "No" or enter == "no" or enter == "N" or enter == "n" or enter == "Quit" or enter == "quit" or enter == "Q" or enter == "q":
          print('Back to BASIC')
          continue
        else:
          load = enter
        print('''-----Directory-----
memory   PROGRAM   ext''')
        print(str(sys.getsizeof(save)) + " Bytes" + "     System Memory.prg")
        print(str(sys.getsizeof(load)) + " Bytes" + '     ' + str(load))
        print('Back to BASIC')
        continue
#Clear   
    if line == "clear" or line == "Clear":
        print("Are You Sure you want to clear the PROGRAM from memory?[y/n]")
        abc = input()
        if abc == "Yes" or abc == "yes" or abc == "Y" or abc == "y":
            save = ""
            print("Your PROGRAM has been erased from memory!")
            continue
        elif abc == "No" or abc == "no" or abc == "N" or abc == "n":
            save = save
            print("Your PROGRAM has not been erased from memory!")
            continue
    
#Syntax error            
    else:
        print("?Syntax Error?")
        continue
    content += line + "\n"
