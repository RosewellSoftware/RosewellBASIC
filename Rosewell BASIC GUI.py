import tkinter as tk
import sys, io, os
import subprocess as subp
from contextlib import redirect_stdout
from tkinter import *
from tkinter import ttk
from datetime import date
today = date.today()
from tkinter.font import Font
import time, calendar, datetime
import pygame
from pygame import mixer
loadx = ''
loadz = ''
global note
note = ''


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
def findNum(word):
    for i in word:
        if i.isdigit():
            return True
    return False


try:
    from clrprint import *

  
except:
    print('The Clrprint Module could not be imported')
    print(' ')

saves = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890' + u"\u2680" + u"\u2681" + u"\u2682" + u"\u2683" + u"\u2684" + u"\u2685" + u"\u2588" + "@&# !" + '"' + "$%'()*+,-./:;>=<?\[]{}^_" + u"\u0060" + "|~" + u"\u00A1" + u"\u00A2" + u"\u00A3" + u"\u00A4" + u"\u00A5" + u"\u00A6" + u"\u00A7" + u"\u00A8" + u"\u00A9" + u"\u00AA" + u"\u00AB" + u"\u00AC" + u"\u00AE" + u"\u00AF" + u"\u00B0" + u"\u00B6" + u"\u00BB" + u"\u00BC" + u"\u00BD" + u"\u00BE" + u"\u00BF" + u"\u00D7" + u"\u00F7" + u"\u2580" + u"\u2581" + u"\u2582" + u"\u2583" + u"\u2584" + u"\u2585" + u"\u2586" + u"\u2587" + u"\u2588" + u"\u2589" + u"\u258A" + u"\u258B" + u"\u258C" + u"\u258D" + u"\u258E" + u"\u258F" + u"\u2590" + u"\u2591" + u"\u2592" + u"\u2593" + u"\u2594" + u"\u2595" + u"\u2596" + u"\u2597" + u"\u2598" + u"\u2599" + u"\u259A" + u"\u259B" + u"\u259C" + u"\u259D" + u"\u259E" + u"\u259F"

rose = "© Blake Gouthro and JinHo Mo | Rosewell BASIC | V2.1 | Rosewell Software | 2021 - " + str(today.year) + " ©"
load = ''




def copyright():
    
    
    try:
        clrprint('© Blake Gouthro and JinHo Mo |' , 'Rosewell', 'B', 'A', 'S', 'I', 'C', '| V2.1 | Rosewell Software | 2021 - ' + str(today.year) + ' ©', clr=['blue', 'white', 'red', 'yellow', 'green', 'blue', 'purple', 'blue', 'blue'])
    except:
        print(rose)

class Shell(tk.Text):
  global loadx
  
   
  
  def __init__(self, parent, **kwargs):

    
    self.save = ''
    self.saveTF = False
    self.mode = ''
    
    tk.Text.__init__(self, parent, **kwargs)
    self.bind('<Key>', self.on_key) # setup handler to process pressed keys
    self.cmd = None
    self.insert_text(rose, end='''
''')
    self.insert_text("Today's Date: " + str(today), end='''
''')
    self.insert_text('Enough BASIC Bytes Free', end='''
''')
    self.insert_text('Ready', end='''
''')
    # hold the last command issued
    self.show_prompt()
    

  # to append given text at the end of Text box
  def insert_text(self, txt='', end='\n'):
    self.insert(tk.END, txt+end)
    self.see(tk.END) # make sure it is visible
#Ready Prompt
  def show_prompt(self):
    self.insert_text('', end='')
    self.mark_set(tk.INSERT, tk.END) # make sure the input cursor is at the end
    self.cursor = self.index(tk.INSERT) # save the input position

  # handler to process keyboard input
  def on_key(self, event):
    #print(event)
    if event.keysym == 'Up':
      if self.cmd:
        # show the last command
        self.delete(self.cursor, tk.END)
        self.insert(self.cursor, self.cmd)
      return "break" # disable the default handling of up key
    if event.keysym == 'Down':
      return "break" # disable the default handling of down key
    if event.keysym in ('Left', 'BackSpace'):
      current = self.index(tk.INSERT) # get the current position of the input cursor
      if self.compare(current, '==', self.cursor):
        # if input cursor is at the beginning of input (after the prompt), do nothing
        return "break"
    if event.keysym == 'Return':
      # extract the command input
      cmd = self.get(self.cursor, tk.END).strip()
      self.insert_text() # advance to next line
      if cmd.startswith('`'):
        # it is an external command
        self.system(cmd)
      else:
        # it is python statement
        self.execute(cmd)
      self.show_prompt()
      return "break" # disable the default handling of Enter key
    if event.keysym == 'Escape':
      self.master.destroy() # quit the shell
  # function to handle python statement input
  
  def execute(self, cmd):
    
    self.cmd = cmd  # save the command
    global loadx
    global loadz
    loadx = ''
    loadz = loadz
    name = ''
    
    
    def atsciiprint():
      for i in range(157):
        self.insert_text(saves[i], end=''); time.sleep(0.000000000000000001)

    def repeatchr(num):
      for i in range(num):
        atsciiprint()
    def Go(num):
      f = io.StringIO()
      for x in range(num):
        with redirect_stdout(f):
          try:
            exec(self.save, globals())
          except:
            return False
      self.insert_text(f.getvalue(), end='')
    def repeatchr(num):
        for i in range(num):
            atsciiprint()
    
    
    def poke(word):
    
        try:
            
            self.insert_text(atscii.get(word[0], "No Character to Poke"), end='''
''')
            
        except Exception as e:
            print(e)
    
    # use redirect_stdout() to capture the output of exec() to a string
    #20211109 Secret

    
    
    
        
    
    
    
    if cmd == '20211109':
        self.insert_text('Hello User! You have found the November 9th 2021 Secret! The Creation Date of Rosewell OS Happened on this date! We are talking about Rosewell OS not Rosewell BASIC. Never Forget it JinHo Mo or Blake Gouthro', end='''
''')
        self.insert_text('Ready', end='''
''')


    #Color Help
    elif cmd in ['Color Help','color help','COLOR HELP','Color help','color Help','ch','CH','Ch','cH','color h','COLOR h','Color h','COLOR H','Color H','color H']:
        self.insert_text('''-----Background Color Help-----
Here's what to type in for changing the Background Colors

[1] DEFAULT or BASIC BLUE
[2] Special Edition; Commodore 64
[3] RED or DARK RED
[4] BLUE or DARK BLUE
[5] TEAL
[6] ORANGE
[7] GREEN
[8] GRAY - Only Available in Gray plus white text. DOES NOT REQUIRE TYPING 'WHITE' 
[9] PURPLE
[10] YELLOW - 'white' will make the text black for this color
[11] PINK - 'white' will make the text black for this color
[12] WHITE - no 'white' needed, uses Black text
[13] BLACK - no 'white' needed, uses White text
[14] AMBER - No White text available
[15] Special Edition; Commodore Vic-20
[16] Special Edition; Commodore Plus-4
[17] Special Edition; Commodore 128
[18] Special Edition; Commodore PET

Type 'white' in the fullsize text or 'w' in the abrivations to get the color backgound you want plus white text
Ex.
Red is:
Red white or rw
NOTE: All unsaved work will be lost, this is because the process is destroyed when another window is created.
Ready''', end='''
''')
        return


    #Color Changing Feature
    elif "color" in cmd.lower():
        colors = str(cmd.split()[-1:][0])

        if colors in ['BASIC','Basic','basic','Default','default','DEFAULT','B','b','d','D']:
            shell = Shell(root, insertbackground="#78DAFC", highlightbackground ="#0F5FB4",highlightcolor="#0F5FB4", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#78DAFC", bg="#0F5FB4")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        
        if colors in ['c64','C64','Commodore 64','commodore 64','COMMODORE 64','C','c','64']:        
            shell = Shell(root,insertbackground="#6f6ed1", highlightbackground ="#6f6ed1",highlightcolor="#6f6ed1", highlightthickness=30, borderwidth=14, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#6f6ed1", bg="#3F359B")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['c64 white','C64 white','Commodore 64 white','commodore 64 white','COMMODORE 64 white','Cw','cw','64w']:
            shell = Shell(root,insertbackground="#F6F6F6", highlightbackground ="#6f6ed1",highlightcolor="#6f6ed1", highlightthickness=30, borderwidth=14, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#F6F6F6", bg="#3F359B")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['Red','RED','red','Dark Red','DARK RED','dark red','Dark red','dark Red','R','r','DR','dr','Dr','dR']:
            shell = Shell(root,insertbackground="#E39693", highlightbackground ="#8B0D0D",highlightcolor="#8B0D0D", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#E39693", bg="#8B0D0D")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['Red white','RED white','red white','Dark Red white','DARK RED white','dark red white','Dark red white','dark Red white','Rw','rw','DRw','drw','Drw','dRw']:
            shell = Shell(root,insertbackground="#F6F6F6", highlightbackground ="#8B0D0D",highlightcolor="#8B0D0D", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#F6F6F6", bg="#8B0D0D")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['Blue white','blue white','BLUE white','Dark Blue white','Dark blue white','dark Blue white','DARK BLUE white','dark blue white','DBw','dbw','Dbw','dBw']:
            shell = Shell(root,insertbackground="#F6F6F6", highlightbackground ="#10145A",highlightcolor="#10145A", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#F6F6F6", bg="#10145A")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['Blue','blue','BLUE','Dark Blue','Dark blue','dark Blue','DARK BLUE','dark blue','DB','db','Db','dB']:
            shell = Shell(root,insertbackground="#8A8FEA", highlightbackground ="#10145A",highlightcolor="#10145A", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#8A8FEA", bg="#10145A")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()   
        if colors in ['Teal','teal','TEAL','T','t']:
            shell = Shell(root,insertbackground="#52FFC5", highlightbackground ="#008080",highlightcolor="#008080", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#52FFC5", bg="#008080")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['Teal white','teal white','TEAL white','Tw','tw']:
            shell = Shell(root,insertbackground="#F6F6F6", highlightbackground ="#008080",highlightcolor="#008080", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#F6F6F6", bg="#008080")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['Orange','orange','ORANGE','O','o']:
            shell = Shell(root,insertbackground="#955E00", highlightbackground ="#ff8c00",highlightcolor="#ff8c00", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#955E00", bg="#ff8c00")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['Orange white','orange white','ORANGE white','Ow','ow']:
            shell = Shell(root,insertbackground="#F6F6F6", highlightbackground ="#ff8c00",highlightcolor="#ff8c00", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#F6F6F6", bg="#ff8c00")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['green','GREEN','Green','G','g',]:
            shell = Shell(root,insertbackground="#A4EB99", highlightbackground ="#247618",highlightcolor="#247618", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#A4EB99", bg="#247618")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['green white','GREEN white','Green white','Gw','gw',]:
            shell = Shell(root,insertbackground="#F6F6F6", highlightbackground ="#247618",highlightcolor="#247618", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#F6F6F6", bg="#247618")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['gray','GRAY','Gray','GR','gr','Gr','gR']:
            shell = Shell(root,insertbackground="#F6F6F6", highlightbackground ="#525252",highlightcolor="#525252", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#F6F6F6", bg="#525252")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['purple','PURPLE','Purple','P','p']:
            shell = Shell(root,insertbackground="#B770E9", highlightbackground ="#6A19A4",highlightcolor="#6A19A4", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#B770E9", bg="#6A19A4")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['purple white','PURPLE white','Purple white','Pw','pw']:
            shell = Shell(root,insertbackground="#F6F6F6", highlightbackground ="#6A19A4",highlightcolor="#6A19A4", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#F6F6F6", bg="#6A19A4")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['yellow','YELLOW','Yellow','y','Y']:
            shell = Shell(root,insertbackground="#687312", highlightbackground ="#BCFE54",highlightcolor="#BCFE54", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#687312", bg="#BCFE54")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['yellow white','YELLOW white','Yellow white','yw','Yw']:
            shell = Shell(root,insertbackground="#000000", highlightbackground ="#BCFE54",highlightcolor="#BCFE54", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#000000", bg="#BCFE54")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['PINK','pink','Pink','pi','PI','Pi','pI']:
            shell = Shell(root,insertbackground="#900D74", highlightbackground ="#ED33C4",highlightcolor="#ED33C4", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#900D74", bg="#ED33C4")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['PINK white','pink white','Pink white','pi white','PI white','Pi white','pI white']:
            shell = Shell(root,insertbackground="#000000", highlightbackground ="#ED33C4",highlightcolor="#ED33C4", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#000000", bg="#ED33C4")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['white','WHITE','White','w','W']:
            shell = Shell(root,insertbackground="#000000", highlightbackground ="#F6F6F6",highlightcolor="#F6F6F6", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#000000", bg="#F6F6F6")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['BLACK','black','Black']:
            shell = Shell(root,insertbackground="#F6F6F6", highlightbackground ="#000000",highlightcolor="#000000", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#F6F6F6", bg="#000000")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['vic20','Vic20','VIC20','vic-20','VIC-20','Vic-20','vic','VIC','Vic']:        
            shell = Shell(root,insertbackground="#061FEE", highlightbackground ="#00F9F7",highlightcolor="#00F9F7", highlightthickness=30, borderwidth=14, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#061FEE", bg="#F6F6F6")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['plus','PLUS','Plus','Plus4','PLUS4','plus4','plus-4','PLUS-4','Plus-4']:        
            shell = Shell(root,insertbackground="#000000", highlightbackground ="#B69DF8",highlightcolor="#B69DF8", highlightthickness=30, borderwidth=14, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#000000", bg="#F6F6F6")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['128','c128','C128','COMMODORE128','commodore128','Commodore128','Commodore 128',' commodore 128','COMMODORE 128']:        
            shell = Shell(root,insertbackground="#A1E08E", highlightbackground ="#A1E08E",highlightcolor="#A1E08E", highlightthickness=30, borderwidth=14, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#A1E08E", bg="#555555")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['PET','pet','Pet','pEt','peT','PEt','pET','PeT','commodore pet','Commodore pet','COMMODORE pet','COMMODORE PET','Commodore PET','commodore PET']:        
            shell = Shell(root,insertbackground="#00FE52", highlightbackground ="#000000",highlightcolor="#000000", highlightthickness=30, borderwidth=14, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#00FE52", bg="#000000")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        if colors in ['Amber','AMBER','amber','A','a','Ab','aB','AB','ab']:
            shell = Shell(root,insertbackground="#ff8c00", highlightbackground ="#000000",highlightcolor="#000000", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#ff8c00", bg="#000000")
            self.destroy()
            shell.pack(fill=tk.BOTH, expand=1)
            root.update()
        
        
        
        
        
        
         
      # 20050421 Secret
    if cmd == '20050421':
        self.insert_text('Hi My name is CONRAD! You Look Familiar. Have we met somewhere? Whta is your name?', end='''
''')
        self.saveTF = True
        self.mode = '20050421'
        return
    #Save Function
    if self.saveTF:
      user = cmd
      
      self.saveTF = False
      if user in ['Quit', 'quit', 'QUIT', 'Q', 'q', 'Exit', 'exit', 'EXIT', 'E', 'e']:
          self.insert_text('Back to BASIC', end='\n')
      elif self.mode == 'save':
          with open(cmd, 'w') as file:
              file.write(self.save)
          self.insert_text('Saving . . . . .', end='''
''')
          time.sleep(1)
          self.insert_text('Your PROGRAM Has Been Saved!', end='''
''')
          self.insert_text('Ready', end='''
''')
      

          
      #Load Function   
      elif self.mode == 'load':
          try:
              with open(cmd, "r") as file:
                  self.save = "".join(file.readlines())
              self.insert_text('Loading . . . . .', end='''
''')
              time.sleep(1)
              self.insert_text('-----Directory-----', end='''
''')
              self.insert_text('Memory   PROGRAM   Ext', end='''
''')
              self.insert_text(str(sys.getsizeof(self.save)) + " Bytes" + "     System Memory.prg", end='''
''')
              if load != '':
                  
                  self.insert_text(str(sys.getsizeof(load)) + " Bytes" + '     ' + str(load), end='''
''')
              else:
                  self.insert_text(str(sys.getsizeof(load)) + " Bytes" + '     ' + 'BASIC Memory.prg', end='''
''')
              self.insert_text('Ready', end='''
''')
          except:
              self.insert_text("?Dir Error? - The PROGRAM Either Doesn't Exist, or was Typed in Wrong or, is not in the same Folder.", end='''
''')
      
      #Repeat Function
      elif self.mode == 'repeat':
          try:
              repeatchr(int(user))
              self.insert_text('''
Ready''', end='''
''')
          except:
              self.insert_text("?Syntax Error? - means something was typed in wrong", end='''
''')
      #Music Function
      elif 'music' in self.mode:
          mixer.init()
          
          if user in ['1', 'one', 'One', 'ONE', 'O', 'o','Play','play','PLAY','P','p'] and self.mode == 'music':
              self.insert_text("Enter Music name or music path name:", end='\n')
              self.saveTF = True
              self.mode = 'music1'
              return
          elif self.mode == 'music1':
              mixer.music.load(cmd)
              #Loops Music
              mixer.music.play(-1)
              self.insert_text("Background Music is Playing")
          if user in ['2', 'Two','two','TWO','T','t','Stop','stop','STOP','S','s','PAUSE','pause','Pause']:
              mixer.music.stop()
              self.insert_text('Background Music has Stopped Playing', end='''
''')
          if user in ['3','Three','three','THREE','Pause','pause','PAUSE','P','p']:
              mixer.music.pause()
              self.insert_text('Background Music Has Been Paused', end='''
''')
          if user in ['4','Four','FOUR','F','f','four','Unpause','unpause','UNPAUSE','UnPause','up','UP','Up','uP']:
              mixer.music.unpause()
              self.insert_text('Background Music Has Been UnPaused', end='''
''')

          if user in ['5','Five','five','FIVE','Add','ADD','add','FI','fi','Fi','fI','A','a','Queue','queue','QUEUE','q','Q','Add To Queue','ADD TO QUEUE','add to queue','Add to queue','add To queue','add to Queue','Add To queue','add To Queue']:
              self.insert_text('Enter the Path or Name of the Music you Would Like to Add to the Queue:', end='''
''')
              self.saveTF = True
              self.mode = 'music2'
              return
          if user in ['6','six','SIX','Six','UnLoop','unloop','UNLOOP','Unloop','unLoop']:
              self.insert_text('Enter Music Name or Path Name:', end='''
''')
              self.saveTF = True
              self.mode = 'music3'
              return
          elif self.mode == 'music3':
              mixer.music.load(cmd)
              mixer.music.play()
              self.insert_text('Background Music is Playing Without Loop', end='''
''')
          elif self.mode == 'music2':
              mixer.music.queue(user)
              self.insert_text('Music Has Been Added to the Queue', end='''
''')
              
          self.insert_text('Ready', end='''
''')

      #Load, 8 Feature
      elif 'load, 8' in self.mode:
        
        loadx = '/Volumes/'
        
        
        if user != '' or user != ' ': 
            loadx = loadx + user + '/'
            
        elif user == '' or user == ' ':
            user = 'UNTITLED'
            loadx = loadx + user + '/'
        
        self.insert_text("Enter PROGRAM Name and extension or path from External Disk to PROGRAM. [Type 'Quit' or 'Exit' to quit]:", end='''
''')
        loadz = loadx
        self.saveTF = True
        self.mode = 'load,82'
        return
            
      elif 'load,82' in self.mode:
          loadx = loadz
          loadx = loadx + user
          
          try:
            with open(loadx, "r") as file:
              self.save = "".join(file.readlines())
            time.sleep(1)
          except:
            self.insert_text('?Syntax Error? - This Means Something was Typed in Wrong', end='''
''')
          
          self.insert_text('-----Directory-----', end='''
''')
          self.insert_text('Memory   PROGRAM   Ext', end='''
''')
          self.insert_text(str(sys.getsizeof(self.save)) + " Bytes" + "     SYSTEM Memory.prg", end='''
''')
          self.insert_text(str(sys.getsizeof(loadx)) + " Bytes" + '     ' + loadx, end='''
''')
        
              



          self.insert_text('Ready', end='''
''')
      # Clear System Memory
      elif self.mode == 'clear':
          if user in ['Yes','YES','yes','Y','y']:
              self.save = ''
              time.sleep(1)
              self.insert_text('SYSTEM MEMORY Has Been Cleared!', end='''
''')
          if user in ['NO','No','no','n','N']:
              self.save = self.save
              self.insert_text('SYSTEM MEMORY Has Not Been Cleared.', end='''
''')

          self.insert_text('Ready', end='''
''')


      #Directory
      elif self.mode == 'dir':
          if user in ['', 'No','no','NO','N','n']:
              user = 'BASIC Memory.prg'
              programs = ''
          else:
              programs = user
          self.insert_text('-----Directory-----', end='''
''')
          self.insert_text('Memory   PROGRAM   Ext', end='''
''')
          self.insert_text(str(sys.getsizeof(self.save)) + " Bytes" + "     SYSTEM Memory.prg", end='''
''')
          self.insert_text(str(sys.getsizeof(programs)) + " Bytes" + '     ' + user, end='''
''')
          self.insert_text('Ready', end='''
''')

      #Peek Function
      elif self.mode =='peek':
        sub = cmd.split()[-1]
        try:
          if user in ['1', 'One','ONE','one','O','o']:
            for i in sub:
               self.insert_text(ord(i), end = "\n")
          if user in ['2','Two','TWO','two','T','t']:
            for i in sub:
               self.insert_text(chr(int(i)), end = "\n") 
              
        except:
          self.insert_text('?Syntax Error? - means something was typed in wrong', end='''
''')
        self.insert_text('Ready', end='''
''')
      

      #20050421 Secret Function
      elif '20050421' in self.mode:
          
          name = cmd
          
          self.insert_text('''
Welcome ''' + name + "! This Secret is Famillar because it is from Rosewell OS! Not Rosewell BASIC. Anyways Both Operating Systems are Cool Operating Systems.", end='''

''')
          self.insert_text(rose, end='''

''')
          self.insert_text("That is the Rosewell BASIC Copyright line. it is important that all of Blake's OSes have them. Rosewell OS was created on November 9th 2021.", end='''

''')
          self.insert_text('You can Contact the creator at: rosewellsoftware@Gmail.com', end='''

''')
          self.insert_text('''Brewing Coffee for Next Update . . . . .
Have a Good Day ''' + name + '!', end='''

''')
          self.insert_text('Ready', end='''

''')
          cmd = ''
          
      
          
          
          
      #Notes Menu
      elif 'Note' in self.mode:
          global note
          if user in ['1', 'One','one','ONE','New','NEW','new','N','n','o','O']:
              self.insert_text('Are You Sure? This Action will Delete the Previous Note.[y/n]: ', end='''
''')
              self.saveTF = True
              self.mode = 'note2'
              return
          if user in  ['2', 'Two', 'two', 'Review', 'review', 'r', 'R', 'Review Note', 'review Note', 'Review note', 'review note']:
              self.insert_text('''-----Review Note-----
Your Note Contains:
''', end='''
''')
              self.insert_text(note, end='''
''')
              self.insert_text('Ready', end='''
''')
          if user in ['3', 'Add', 'add', 'A', 'a', 'Edit', 'edit', 'E', 'e', 'Add Note', 'Add note', 'add Note', 'add note', 'Edit Note', 'Edit note', 'edit Note', 'edit note']:
              self.insert_text('''-----Add To Note-----
Enter The Contents You Would Like to Add/[1 Line]''', end='''
''')
              self.saveTF = True
              self.mode = 'note4'
              return
      elif 'note2' in self.mode:
          if user in ['NO','no','No','n','N','quit','QUIT','Quit','q','Q','Exit','exit','EXIT','E','e']:
              self.insert_text('Ready', end='''
''')
          else:
              self.insert_text('''-----New Note-----
Enter Your New Note Contents.[1 line]''', end='''
''')
              self.saveTF = True
              self.mode = 'note3'
              return
      elif 'note3' in self.mode:
          
          note = user + "\n"
          self.insert_text('Saving Note . . . . .', end='''
''')
          time.sleep(1)
          self.insert_text('Your Note Has Been Saved! . . . . .', end='''
''')
          self.insert_text('Ready', end='''
''')
      elif 'note4' in self.mode:
          
          note += user + "\n"
          self.insert_text('Saving Note . . . . .', end='''
''')
          time.sleep(1)
          self.insert_text('Your Note Has Been Saved!', end='''
''')
          self.insert_text('Ready', end='''
''')
      elif 'voice' in self.mode:
          os.system( " say " + cmd  + " " )
          self.insert_text('Ready', end='''
''')
      elif 'restart' in self.mode:
          if cmd in ['No','no','NO','n','N']:
              self.insert_text('''The app will not be Restarted.
Ready''', end='''
''')
          if cmd in ['Yes','yes','YES','Y','y']:
              self.insert_text('Restarting App...', end='''
''')
              self.insert_text('Loading . . . . .', end='''
''')
              time.sleep(1)
              shell = Shell(root, insertbackground="#78DAFC", highlightbackground ="#0F5FB4",highlightcolor="#0F5FB4", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#78DAFC", bg="#0F5FB4")
              self.destroy()
              shell.pack(fill=tk.BOTH, expand=1)
              root.update()
              
 
        
      self.mode = ''
      return

    if len(cmd) == 0:
      self.insert_text('', end='')


    # Load, 8
    elif cmd in ['Load,8', 'LOAD, 8', 'LOAD,8', 'load,8', 'load, 8', 'Load, 8', 'l8', 'L8', 'Load*8', 'load*8', 'Load* 8' , 'load* 8', 'LOAD* 8', 'load$8', 'LOAD$8', 'Load$8', 'Load$ 8', 'load$ 8', 'LOAD$ 8', 'load$, 8', 'Load$, 8', 'LOAD$, 8', 'Load*, 8', 'load*, 8', 'LOAD*, 8']:
        self.insert_text("Enter External Disk Name [Type 'Quit' or 'Exit' to quit/ if left blank, the prompt defaults to UNTITLED.]:", end='''
''')
        try:
            
            self.saveTF = True
            self.mode = 'load, 8'
        except:
            self.insert_text("?Dir Error? - The PROGRAM Either Doesn't Exist, or was Typed in Wrong or, is not in the same Folder.", end='''
''')


    # All Chr  
    elif cmd in ['All Chr', 'all chr', 'All chr', 'all Chr', 'ALL CHR', 'AC', 'ac', 'All Character', 'all character', 'All character', 'all Character', 'ALL CHARACTER', 'All Characters', 'all characters', 'all Characters', 'All characters', 'ALL CHARACTERS', 'ALL CHRS', 'all chrs', 'All chrs', 'all Chrs']:
      atsciiprint()
      self.insert_text('''
Ready''', end='''
''')
    #Poke
    elif 'poke' in cmd.lower():
      pokes = cmd.split()[1:]

      poke(pokes)

      self.insert_text('Ready', end='''
''')

    #Peek
    elif 'peek' in cmd.lower():
        self.insert_text('Ord or Chr?[1/2]', end='''
''')
        self.insert_text("Return ATSCII Value or Printed ATSCII?", end='''
''')
        self.saveTF = True
        self.mode = 'peek'
    

        
    #Goto
    elif "goto" in cmd.lower():
      Go(int(cmd.split()[-1:][0]))
      self.insert_text('Ready', end='\n')


    #Saves to Variable
    elif findNum(cmd):
      
      spaces = ''
      space = ''
      varc = ''
      space = cmd.split()[0]
      varc = str(space) + ' '
      spaces = cmd.replace(varc, '')
      self.save += spaces + "\n"


    #list
    elif cmd in ['list', 'List', 'LIST']:
      time.sleep(0.1)
      self.insert_text(self.save, end='''
''')
      self.insert_text('Ready', end='''
''')

    #Contact Us
    elif cmd in ['Contact','contact','CONTACT','Contact Us','CONTACT US','contact us','Contact us','contact Us']:
        self.insert_text('''Contact Us at:
rosewellsoftware@Gmail.com''', end='''
''')
        self.insert_text('Ready', end='''
''')
    
    #Run
    elif cmd in ["Run", "run", 'RUN', 'R', 'r']:
      f = io.StringIO()
      with redirect_stdout(f):
        try:
          exec(self.save, globals())
          self.insert_text(f.getvalue(), end='')
          self.insert_text('Ready', end='''
''')

        except Exception as e:
          print('?Syntax Error? - means something was typed in wrong')



    #Help
    elif cmd in ['HELP', 'Help', 'help', 'H', 'h']:
      self.insert_text('''-----Help Commands-----
GoTo (num) - runs and repeats code (num) amount of times
Help - list all the features of BASIC
Save - Allows you to save BASIC programs to a file
Run - allows you to run BASIC programs
Quit - Quits Rosewell BASIC
List - list the PROGRAM saved in memory
Load - loads an external PROGRAM from the Same folder
Load 8 - Loads a program from an External Disk
Clear - Allows you to clear your PROGRAM code from memory
Dir - Lists the PROGRAM Directory
ATSCII - Prints the Built-in ATSCII characters for poke/peek commands
all chr - Prints all of the characters at once
Repeat Chr - can print All Chr PROGRAM if given a number
Poke - Print an ATSCII Character to the Screen
Peek - Return the value of an ATSCII Character
Music - Opens the Music Menu to play Background Music of your Choice
Note - Opens the Note Built in menu
Time/Date/Calendar/Clock - Tells the current time and date
Text To Speech - Opens the Text To Speach App
Color - You can now change the background color for the app in use
Color Help - Get help with selecting background colors
Restart - Restarts the App back to the DEFAULT color and all unsaved files will be deleted
Contact Us - Larn how to contact Rosewell Software
49 Bytes - Means that the SYSTYEM MEMORY or any other BASIC MEMORY is empty.(Don't know why it says 49 for 0)
?Syntax Error? - means something was typed in wrong
?Dir Error? - The PROGRAM Either Doesn't Exist, or was Typed in Wrong or, is not in the same Folder.''', end='''
''')
      self.insert_text('Ready', end='''
''')

    #Save
    elif cmd in ['Save', 'save', 'SAVE', 's', 'S', 'Saves', 'saves', 'SAVES']:
      self.insert_text("Enter new PROGRAM Name to Save [Type 'Quit' or 'Exit' to quit]:", end='\n')
      self.insert_text("Don't Forget to type '.py' to save as a python file. If your saving in the app, your file will be saved in the app ready to go!", end='\n')
      
      try:
          
          self.saveTF = True
          self.mode = 'save'

          

      except:
          self.insert_text("?Dir Error? - The PROGRAM Either Doesn't Exist, or was Typed in Wrong or, is not in the same Folder.", end='''
''')

    #Text To Speech
    elif cmd in ['speak','Speak','SPEAK','Speech','speech','SPEECH','Text To Speech','text to speech','TEXT TO SPEECH','Text to speech','text To speech','text to Speech',' Text To speech','text To Speech','Text to Speech','TTS','tts','Tts','tTs','ttS','TTs','tTS','TtS']:
        self.insert_text('© Blake Gouthro | Text To Speech App | V1.1 | Rosewell Software | 2022 - ' + str(today.year) +' ©', end='''
''')
        
        self.insert_text('Enter Text To Speak:', end='''
''')
        self.saveTF = True
        self.mode = 'voice'



        
            
    #music
    elif cmd in ['Music', 'music', 'MUSIC', 'M', 'm', 'MM', 'mm', 'Mm', 'mM', 'Music Menu', 'MUSIC MENU', 'music menu', 'Music menu', 'music Menu']:
        
            
        self.insert_text('''-----Music Menu-----
[1] Play Background Music
[2] Stop Background Music
[3] Pause Background Music
[4] UnPause Background Music
[5] Add To Queue
[6] Play Without Loop''', end='''
''')
        try:
          
          self.saveTF = True
          self.mode = 'music'

          
          
          
        except:
          self.insert_text("?Dir Error? - The PROGRAM Either Doesn't Exist, or was Typed in Wrong or, is not in the same Folder.", end='''
''')

    #Load
    elif cmd in ['Load', 'load', 'L', 'l', 'LOAD']:
        self.insert_text("Enter PROGRAM Name to Load [Type 'Quit' or 'Exit' to quit]:", end='''
''')
        try:
            self.saveTF = True
            self.mode = 'load'
            
            

        except:
          self.insert_text("?Dir Error? - The PROGRAM Either Doesn't Exist, or was Typed in Wrong or, is not in the same Folder.", end='''
''')


    #Directory
    elif cmd in ['DIR','Dir','dir','d','D','Directory','directory','DIRECTORY']:
        self.insert_text("Load a File into the Directory? [Type 'Quit' or 'Exit' to exit]:", end='''
''')
        self.saveTF = True
        self.mode = 'dir'
    #Secrets Menu

    elif cmd in ['Secrets', 'secret', 'S', 's', 'SECRET', 'Secret', 'SECRETS', 'secrets']:
        self.insert_text('''-----Secrets Menu-----
Rosewell BASIC - Lists Copyright and System Info
20050421 - Rosewell OS Secret
20211109 - Rosewell OS Secret
Happy Birthday - Sings Happy Birthday to You!
Dev - Opens the Credits Secret''', end='''
''')
        self.insert_text('Ready', end='''
''')


    #Devolper Menu
    elif cmd in ['Dev', 'dev', 'D', 'd', 'developer', 'Developer', 'Credits', 'credits', 'Credit', 'credit', 'CREDIT', 'DEV', 'DEVELOPER']:
        copyright()
        self.insert_text(rose, end='''
''')
        self.insert_text('''-----Credits-----
Blake Gouthro - Rosewell BASIC and Rosewell OS Developer, C.E.O of Rosewell Software, rosewellsoftware@Gmail.com account holder, Programmer, Writer, Graphical Devolper and Head of mangement for Rosewell Software.

JinHo Mo - Rosewell BASIC and Rosewell OS Developer, Writer, Graphical Developer, Programmer, Writer, Graphical Developer, Rosewell Software Team Member.

Beginner's All-Purpose Symbolic Instruction Code or BASIC.''', end='''
''')
        self.insert_text('Ready', end='''
''')


    #Happy Birthday Secret
    elif cmd in ['Happy Birthday', 'happy Birthday', 'Happy birthday', 'happy birthday', 'HB', 'Hb', 'hB', 'hb']:
        self.insert_text('''Congratulations! You have found the Happy Birthday Secret!
''', end='''
''')
        self.insert_text('Happy Birthday to You!', end='''
''')
        os.system( "say Happy Birthday to You" )

        self.insert_text('Happy Birthday to You!', end='''
''')
        os.system( "say Happy Birthday to You" )

        self.insert_text('Happy Birthday User!', end='''
''')
        os.system( "say Happy Birthday User" )

        self.insert_text('Happy Birthday to You!', end='''
''')
        os.system( "say Happy Birthday to You" )
        self.insert_text('''
Ready''', end='''
''')

    #Rosewell BASIC Secret
    elif cmd in ['Rosewell', 'rosewell', 'BASIC', 'Basic', 'basic', 'Rosewell BASIC', 'rosewell BASIC', 'Rosewell Basic', 'rosewell Basic', 'Rosewell basic', 'rosewell basic', 'rb', 'Rb', 'rB', 'RB']:
        copyright()
        self.insert_text(rose, end='''
''')
        self.insert_text('''
--Rosewell BASIC was created to be a Recreation of the older BASIC Operating Systems. This copy isn't as powerful yet but soon it will be.
All files that BASIC can use must be run in the same folder.

Basic Stands for;
Beginner's All-Purpose Symbolic Instruction Code

Hello From Nova Scotia!!
Hello From Canada!!

Brewing Coffee For Next Update. . . . .''', end='''
''')
        self.insert_text('Ready', end='''
''')


    #Repeat Chr
    elif cmd in ['Repeat Character', 'Repeat Chr', 'repeat Character', 'repeat Chr', 'Repeat chr', 'Repeat character', 'repeat character', 'repeat chr', 'RC', 'rC', 'Rc', 'rc', 'REPEAT CHARACTER', 'REPEAT CHR', 'Repeat Characters', 'repeat characters', 'Repeat characters', 'repeat Characters', 'REPEAT CHARACTERS', 'RCS', 'Rcs', 'rcs', 'rCs', 'rcS', 'RCs', 'rCS', 'REPEAT CHRS', 'Repeat Chrs', 'repeat chrs', 'Repeat chrs', 'repeat Chrs']:
        self.insert_text("Enter Numbrer to Repeat 'All chr' [Type 'Quit' or 'Exit' to quit]:", end='''
''')
        try:
            self.saveTF = True
            self.mode = 'repeat'
            
            

        except:
          self.insert_text("?Syntax Error? - means something was typed in wrong.", end='''
''')
    
    #Clear System Memory
    elif cmd in ['Clear', 'clear', 'CLEAR', 'C', 'c']:
        self.insert_text("Would you like to clear SYSTEM MEMORY?", end='''
''')
        self.saveTF = True
        self.mode = 'clear'
    #Note Menu
    elif cmd in ['Note', 'note', 'Notes', 'notes', 'n', 'N',]:
        self.insert_text('''-----Notes Menu-----
[1] New/Delete Note
[2] Review Note
[3] Add to/Open Note''', end='''
''')
        self.insert_text('''
Enter a Number: ''', end='''
''')
        self.saveTF = True
        self.mode = 'Note'
        return

    #ATSCII
    elif cmd in ["ListPeek", "listPeek", 'Listpeek', 'listpeek', 'PETSCII', 'petscii', 'PetscII', 'Petscii', 'ATSCII', 'atscii', 'AtscII', 'Atscii']:
        self.insert_text('-----List of Built-in ATSCII Characters-----', end='''
''')
        self.insert_text('Built-in ATSCII Characters are based off of Unicode Characters. Useful for Poke and Peek commands.', end='''
''')
        for k, v in atscii.items():
            self.insert_text(f"{k} : {v}", end='''
''')
        self.insert_text('Ready', end='''
''')

    #Date/Time/Clock/Calendar
    elif cmd in ['Date', 'date', 'Calender', 'calendar', 'Time', 'time', 'T', 't', 'Clock', 'clock', 'CLOCK', 'DATE', 'TIME', 'CALENDAR']:
        self.insert_text("Today's Date: " + str(today), end='''
''')
        now = datetime.datetime.now()
        self.insert_text(now.strftime("%a, %d, %B "), end='''

''')
        yy = today.year
        mm = today.month
        self.insert_text(calendar.month(yy,mm), end='''
''')
        current_time = time.strftime("%H:%M:%S", time.localtime())
        self.insert_text('Current Time: ' + current_time, end='''
''')
        self.insert_text('Ready', end='''
''')
        
    
    

    #Quit
    elif cmd in ['Quit', 'quit', 'QUIT', 'Q', 'q', 'Exit', 'exit', 'EXIT', 'E', 'e']:
        self.insert_text('GoodBye', end='''
''')
        time.sleep(1)
        root.destroy()
        sys.exit()


    #Restart
    elif cmd in ['Restart','restart','RESTART','R','r']:
        self.insert_text('Are you sure you want to restart the app? [NOTE; All unsaved files will be deleted.]',end='''
''')
        self.saveTF = True
        self.mode = 'restart'
        return
        
        









    #Syntax Error     
    else:
      self.insert_text("?Syntax Error?", end='''
''')
        
    
   
    

    
    
  # function to handle external command input
  def system(self, cmd):
    self.cmd = cmd  # save the command
    try:
      # extract the actual command
      cmd = cmd[cmd.index('`')+1:cmd.rindex('`')]
      proc = subp.Popen(cmd, stdout=subp.PIPE, stderr=subp.PIPE, text=True)
      stdout, stderr = proc.communicate(5) # get the command output
      # append the command output to Text box
      self.insert_text(stdout)
    except Exception as e:
      self.insert_text(str(e))

copyright()

root = tk.Tk()
root.title('Rosewell BASIC')
root.configure(bg="#0F5FB4")



shell = Shell(root, insertbackground="#78DAFC", highlightbackground ="#0F5FB4",highlightcolor="#0F5FB4", borderwidth=10, width=69, height=30, font=('Atari-Basic.ttf', 14), fg="#78DAFC", bg="#0F5FB4")

shell.pack(fill=tk.BOTH, expand=1)
shell.focus_set()


root.mainloop()
