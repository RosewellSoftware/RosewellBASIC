from datetime import date
import os, sys, time

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
    And = u'\u0026',
    hashtag = u'\u0023',

    space = u'\u0020',
    exclmark = u'\u0021',
    quotes = u'\u0022',
    dollar = u'\u0024',
    percent = u'\u0025',
    quote = u'\u2019',
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
    colon = u'\u003a',
    semicolon = u'\u003B',
    lessthan = u'\u003C',
    equal = u'\u003D',
    greaterthan = u'\u003E',
    questionmark = u'\u003F',

    uppera = u'\u0041',
    upperb = u'\u0042',
    upperc = u'\u0043',
    upperd = u'\u0044',
    uppere = u'\u0045',
    upperf = u'\u0046',
    upperg = u'\u0047',
    upperh = u'\u0048',
    upperi = u'\u0049',
    upperj = u'\u004A',
    upperk = u'\u004B',
    upperl = u'\u004C',
    upperm = u'\u004D',
    uppern = u'\u004E',
    uppero = u'\u004F',
    upperp = u'\u0050',
    upperq = u'\u0051',
    upperr = u'\u0052',
    uppers = u'\u0053',
    uppert = u'\u0054',
    upperu = u'\u0055',
    upperv = u'\u0056',
    upperw = u'\u0057',
    upperx = u'\u0058',
    uppery = u'\u0059',
    upperz = u'\u005A',
    sqopen = u'\u005B',
    backslash = u'\u005C',
    sqclose = u'\u005D',
    upaccent = u'\u005E',
    lowline = u'\u005F',
    graveaccent = u'\u0060',
    lowera = u'\u0061',
    lowerb = u'\u0062',
    lowerc = u'\u0063',
    lowerd = u'\u0064',
    lowere = u'\u0065',
    lowerf = u'\u0066',
    lowerg = u'\u0067',
    lowerh = u'\u0068',
    loweri = u'\u0069',
    lowerj = u'\u006A',
    lowerk = u'\u006B',
    lowerl = u'\u006C',
    lowerm = u'\u006D',
    lowern = u'\u006E',
    lowero = u'\u006F',
    lowerp = u'\u0070',
    lowerq = u'\u0071',
    lowerr = u'\u0072',
    lowers = u'\u0073',
    lowert = u'\u0074',
    loweru = u'\u0075',
    lowerv = u'\u0076',
    lowerw = u'\u0077',
    lowerx = u'\u0078',
    lowery = u'\u0079',
    lowerz = u'\u007A',
    cropen = u'\u007B',
    verticalbar = u'\u007C',
    crclose = u'\u007D',
    tilde = u'\u007E',
    inexcelmark = u'\u00A1',
    cent = u'\u00A2',
    pound = u'\u00A3',
    currency = u'\u00A4',
    yen = u'\u00A5',
    brokenbar = u'\u00A6',
    sectionsign = u'\u00A7',
    diaeresis = u'\u00A8',
    copyrights = u'\u00A9',
    femord = u'\u00AA',
    leftquotes = u'\u00AB',
    notsign = u'\u00AC',
    registered = u'\u00AE',
    macron = u'\u00AF',
    degree = u'\u00B0',
    pilcrow = u'\u00B6',
    rightquotes = u'\u00BB',
    onedfour = u'\u00BC',
    onedtwo = u'\u00BD',
    threedfour = u'\u00BE',
    inquestionmark = u'\u00BF',
    multiply = u'\u00D7',
    divide = u'\u00F7',
    upperhalf = u'\u2580',
    loweronedeight = u'\u2581',
    loweronedfour = u'\u2582',
    lowerthreedeight = u'\u2583',
    lowerhalf = u'\u2584',
    lowerfivedeight = u'\u2585',
    lowerthreedfour = u'\u2586',
    lowersevendeight = u'\u2587',
    leftsevendeight = u'\u2589',
    leftthreedfour = u'\u258A',
    leftfivedeight = u'\u258B',
    lefthalf = u'\u258C',
    leftthreedeight = u'\u258D',
    leftonedfour = u'\u258E',
    leftonedeight = u'\u258F',
    righthalf = u'\u2590',
    lightshade = u'\u2591',
    mediumshade = u'\u2592',
    darkshade = u'\u2593',
    upperonedeight = u'\u2594',
    rightonedeight = u'\u2595',
    quadlowerleft = u'\u2596',
    quadlowerright = u'\u2597',
    quadupperleft = u'\u2598',
    quadulpllplr = u'\u2599',
    quadulplr = u'\u259A',
    quadulpurpll = u'\u259B',
    quadulpurplr = u'\u259C',
    quadupperright = u'\u259D',
    quadurpll = u'\u259E',
    quadurpllplr = u'\u259F'
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
rose = "© Blake Gouthro and JinHo Mo | Rosewell BASIC | V1.4.5 | Rosewell Software | 2021 - " + str(today.year) + " ©"
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
        print(" ")
        print("Ready")
        continue
# Poke Characters to screen
    if "poke" in line.lower():
        
        pokes = line.split()[1:]
        
        poke(pokes)
        time.sleep(1)
        print(" ")
        print("Ready")
        
        
        
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
Music - Opens the Music Menu to play Background Music of your Choice
?Syntax Error? - means something was typed in wrong
?Dir Error? - The PROGRAM Either Doesn't Exist, or was Typed in Wrong or, is not in the same Folder.
Rosewell BASIC - Lists Copyright and System Info''')
        
#List Peek
    if line == "ListPeek" or line == "listPeek" or line == 'Listpeek' or line == 'listpeek' or line == 'PETSCII' or line == 'petscii' or line == 'PetscII' or line == 'Petscii' or line == 'ATSCII' or line == 'atscii' or line == 'AtscII' or line == 'Atscii':
        print('''-----List of Builtin ATSCII Characters-----
Built-in ATSCII Characters are based off of Unicode Characters. Useful for Poke and Peek commands.
''')
        for k, v in atscii.items():
            print(f"{k} : {v}")
        print(" ")
    
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
    if line == "Exit" or line == "exit" or line == "E" or line == "e" or line == "quit" or line == "Quit" or line == "No" or line == "no" or line == "Goodbye" or line == "goodbye" or line == 'GoodBye' or line == 'goodBye':
        print("Goodbye")
        break
#list        
    if line == "list" or line == "List":
        time.sleep(1)
        print(save)
        print(" ")
        print("Ready")
        continue
#Rosewell BASIC
    if line in ['Rosewell', 'rosewell', 'BASIC', 'Basic', 'basic', 'Rosewell BASIC', 'rosewell BASIC', 'Rosewell Basic', 'rosewell Basic', 'Rosewell basic', 'rosewell basic', 'rb', 'Rb', 'rB', 'RB']:
        print(rose)
        print('''
--Rosewell BASIC was created to be a Recreation of the older BASIC Operating Systems. This copy isn't as powerful yet but soon it will be.
All files that BASIC can use must be run in the same folder.

Hello From Nova Scotia!!
Hello From Canada!!

--Brewing Coffee For Next Update.....--''')
        print(" ")
        print("Ready")
        continue
#Background Music
    if line in ['Music', 'music', 'MUSIC', 'M', 'm', 'BGM', 'bgm', 'BM', 'Bm', 'bM', 'bm', 'Background Music', 'background Music', 'Background music', 'background music']:
        
        try:
            import pygame
            from pygame import mixer
        except ModuleNotFoundError as e:
            print(e)
            print("Please Install the Pygame Module before using Background Music")
            continue
            
        #music menu
        while True:
            print(" ")
            print("Music Menu")
            print(" ")
            print('''[1] Play Background Music
[2] Stop Background Music
[3] Main Menu''')
            print(" ")

            #Play Background Music
            l1 = input("Enter a number above: " )
            if l1 in ['1', 'one', 'One', 'Music', 'music', 'm', 'M', 'Play', 'play', 'P', 'p']:
                
                print("Enter Music Name  and extension to use for Background Song[Type 'Menu' to go back to Main Menu]:")
                #Music Input
                music = input()

                if music == "menu" or music == 'Menu' or music == 'M' or music == 'm':
                    
                    continue

                #Plays Music
                mixer.init()
                mixer.music.load(music)

                #Loops Music
                mixer.music.play(-1)
                print(" ")
                print("Background Music is Playing")
                print(" ")
                
                
                #Back to Music Menu
                continue

            #Stop Background Music
            if l1 in ['2', 'two', 'Two', 'To', 'to', 'Too', 'too', 'Stop', 'stop', 'S', 's']:

                #Stops Playing the Music
                mixer.music.stop() 

                print(" ")
                print("Music has stoped Playing")
                print(" ")
                continue

            #Go back to Main Menu
            if l1 in ['3', 'Three', 'three', 'Quit', 'quit', 'Q', 'q', 'Menu', 'menu', 'M', 'm', 'Main Menu', 'main Menu', 'Main menu', 'main menu']:
                print(" ")
                break
        
        print("Ready")
        continue

        
#load        
    if line == "load" or line == "Load" or line == "l" or line == "L" or line == "LOAD":
        nerd = input("Enter PROGRAM name: " )
        try:
            with open(nerd, "r") as file:
                save = "".join(file.readlines())
            stats = os.stat(nerd)
            time.sleep(1)
            print('''-----Directory-----
memory   PROGRAM   ext''')
            print(stats.st_size, 'Bytes' + '    ' + nerd)
            print(str(sys.getsizeof(save)) + " Bytes" + "     System Memory.prg")
            print(str(sys.getsizeof(load)) + " Bytes" + '     ' + str(load))
            print('Back to BASIC')
            continue
        except:
            time.sleep(1)
            print('?Dir Error? The PROGRAM ' + nerd + " Either Doesn't Exist, or was Typed in Wrong, or is not in the same Folder.")
            
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
            time.sleep(1)
            print("Your PROGRAM has been erased from memory!")
            print("Ready")
            continue
        elif abc == "No" or abc == "no" or abc == "N" or abc == "n":
            save = save
            print("Your PROGRAM has not been erased from memory!")
            print("Ready")
            continue
    
#Syntax error            
    else:
        print("?Syntax Error?")
        continue
    content += line + "\n"
