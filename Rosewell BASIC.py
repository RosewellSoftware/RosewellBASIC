from datetime import date
import os, sys

today = date.today()
save = ""
name = ""
nerd = ""
load = 'BASIC Memory'
line = ""
pokes = ""
apple = ""
atscii = dict(
    dice1 = u"\u2680",
    dice2 = u"\u2681",
    dice3 = u"\u2682",
    dice4 = u"\u2683",
    dice5 = u"\u2684",
    dice6 = u"\u2685",
    block = u"\u2588",
    at = u"\u0040",
    And = u'\0038',
    hashtag = u'\u0023',

    space = u'\u0020',
    exclmark = u'\u0021',
    quotes = u'\u0021',
    dollar = u'\u0024',
    percent = u'\u0025',
    quote = u'\u0027',
    openbracket = u'\u0028',
    closebracket = u'\u0029',
    star = u'\u002A',
    plus = u'\u002B',
    comma = u'\u002C',
    minus = u'\u002D',
    period = u'\u002E',
    forwardslash = u'\u002F',
    zero = u'\u0030',
    one = u'\0031',
    two = u'\0032',
    three = u'\0033',
    four = u'\0034',
    five = u'\0035', 
    six = u'\0036',
    seven = u'\0037',
    eight = u'\0038',
    nine = u'\0039',
    colon = u'\003A',
    semicolon = u'\003B',
    lessthan = u'\003C',
    equal = u'\003D',
    greaterthan = u'\003E',
    questionmark = u'\003F',

    uppera = u'\0041',
    upperb = u'\0042',
    upperc = u'\0043',
    upperd = u'\0044',
    uppere = u'\0045',
    upperf = u'\0046',
    upperg = u'\0047',
    upperh = u'\0048',
    upperi = u'\0049',
    upperj = u'\004A',
    upperk = u'\004B',
    upperl = u'\004C',
    upperm = u'\004D',
    uppern = u'\004E',
    uppero = u'\004F',
    upperp = u'\0050',
    upperq = u'\0051',
    upperr = u'\0052',
    uppers = u'\0053',
    uppert = u'\0054',
    upperu = u'\0055',
    upperv = u'\0056',
    upperw = u'\0057',
    upperx = u'\0058',
    uppery = u'\0059',
    upperz = u'\005A',
    sqopen = u'\005B',
    backslash = u'\005C',
    sqclose = u'\005D',
    upaccent = u'\005E',
    lowline = u'\005F',
    graveaccent = u'\0060',
    lowera = u'\0061',
    lowerb = u'\0062',
    lowerc = u'\0063',
    lowerd = u'\0064',
    lowere = u'\0065',
    lowerf = u'\0066',
    lowerg = u'\0067',
    lowerh = u'\0068',
    loweri = u'\0069',
    lowerj = u'\006A',
    lowerk = u'\006B',
    lowerl = u'\006C',
    lowerm = u'\006D',
    lowern = u'\006E',
    lowero = u'\006F',
    lowerp = u'\0070',
    lowerq = u'\0071',
    lowerr = u'\0072',
    lowers = u'\0073',
    lowert = u'\0074',
    loweru = u'\0075',
    lowerv = u'\0076',
    lowerw = u'\0077',
    lowerx = u'\0078',
    lowery = u'\0079',
    lowerz = u'\007A',
    cropen = u'\007B',
    verticalbar = u'\007C',
    crclose = u'\007D',
    tilde = u'\007E',
    inexcelmark = u'\00A1',
    cent = u'\00A2',
    pound = u'\00A3',
    currency = u'\00A4',
    yen = u'\00A5',
    brokenbar = u'\00A6',
    sectionsign = u'\00A7',
    diaeresis = u'\00A8',
    copyrights = u'\00A9',
    femord = u'\00AA',
    leftquotes = u'\00AB',
    notsign = u'\00AC',
    registered = u'\00AE',
    macron = u'\00AF',
    degree = u'\00B0',
    pilcrow = u'\00B6',
    rightquotes = u'\00BB',
    onedfour = u'\00BC',
    onedtwo = u'\00BD',
    threedfour = u'\00BE',
    inquestionmark = u'\00BF',
    multiply = u'\00D7',
    divide = u'\00F7',
    upperhalf = u'\2580',
    loweronedeight = u'\2581',
    loweronedfour = u'\2582',
    lowerthreedeight = u'\2583',
    lowerhalf = u'\2584',
    lowerfivedeight = u'\2585',
    lowerthreedfour = u'\2586',
    lowersevendeight = u'\2587',
    leftsevendeight = u'\2589',
    leftthreedfour = u'\258A',
    leftfivedeight = u'\258B',
    lefthalf = u'\258C',
    leftthreedeight = u'\258D',
    leftonedfour = u'\258E',
    leftonedeight = u'\258F',
    righthalf = u'\2590',
    lightshade = u'\2591',
    mediumshade = u'\2592',
    darkshade = u'\2593',
    upperonedeight = u'\2594',
    rightonedeight = u'\2595',
    quadlowerleft = u'\2596',
    quadlowerright = u'\2597',
    quadupperleft = u'\2598',
    quadulpllplr = u'\2599',
    quadulplr = u'\259A',
    quadulpurpll = u'\259B',
    quadulpurplr = u'\259C',
    quadupperright = u'\259D',
    quadurpll = u'\259E',
    quadurpllplr = u'\259F'
    )
def Go(num):
    
    for i in range(num):
        exec(save)

def findNum(word):
    for i in word:
        if i.isdigit():
            return True
    return False

def eliminate(word):
    return " ".join(word.split()[1:])

def poke(word):
    
    try:
        
        print(atscii.get(word[0], "No Character to Poke"))
        
    except Exception as e:
        print(e) 
rose = "© Blake Gouthro and JinHo Mo | Rosewell BASIC | V1.4 | Rosewell Software | 2021 - " + str(today.year) + " ©"
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
    # Poke Characters to screen
    if "poke" in line.lower():
        
        pokes = line.split()[1:]
        
        poke(pokes)
        
        continue
#peek
    if "peek" in line.lower():
      print("ord or chr?[1/2]")
      print("Return ATSCII Value or Printed ATSCII?")
      peekz = int(input())
      sub = line.split()[-1]
      if peekz == 1:
        
        for i in sub:
            print(ord(i), end = "\n\n")
        print("Ready")
        
        continue
      if peekz == 2:
        sub = line.split()[-1]
        for i in sub:
            print(chr(int(i)), end = "\n\n")
        print("Ready")
        
    if findNum(line):
        save += eliminate(line) + "\n"
        continue

#Help
    if line == "Help" or line == "help":
      print('''-----Help Commands-----
GoTo (num) - runs and repeats code (num) amount of times
Help - list all the features of BASIC
Save - Allows you to save BASIC programs to a file
Run - allows you to run BASIC programs
quit - Quits Rosewell BASIC
List - list the PROGRAM saved in memory
Load - loads an external PROGRAM
Clear - Allows you to clear your PROGRAM code from memory
Dir - Lists the PROGRAM Directory
ATSCII - Prints the Built-in ATSCII characters for poke/peek commands
Poke - Print an ATSCII Character to the Screen
Peek - Return the value of an ATSCII Character
?Syntax Error? - means something was typed in wrong''')
        
#List Peek
    if line == "ListPeek" or line == "listPeek" or line == 'Listpeek' or line == 'listpeek' or line == 'PETSCII' or line == 'petscii' or line == 'PetscII' or line == 'Petscii' or line == 'ATSCII' or line == 'atscii' or line == 'AtscII' or line == 'Atscii':
        print('''-----List of Builtin ATSCII Characters-----
Built-in ATSCII Characters are based off of Unicode Characters. Useful for Poke and Peek commands.
''')
        for k, v in atscii.items():
            print(f"{k} : {v}")
        continue
    
        print("Ready")
        continue

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
    if line == "quit" or line == "Quit" or line == "No" or line == "no" or line == "Goodbye" or line == "goodbye" or line == 'GoodBye' or line == 'goodBye':
        print("Goodbye")
        break
#list        
    if line == "list" or line == "List":
        print(save)
        continue
#load        
    if line == "load" or line == "Load":
        nerd = input("Enter PROGRAM name: " )
        try:
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
        except Exception as e:
            print(e)
            print(" ")
            print("Ready")
            continue
        print(" ")
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
