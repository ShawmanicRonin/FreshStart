import sys
import webbrowser
import random
import string
import colorama
from colorama import Fore, Back, Style #I ran a pip install command to run this code. This link will hopefully give you the same google A.I. results I had... 
#https://www.google.com/search?q=how+to+print+different+color+text+to+terminal+python&rlz=1C1RXQR_enUS927US927&oq=how+to+print+different+color+text+to+term&gs_lcrp=EgZjaHJvbWUqBwgBECEYoAEyBggAEEUYOTIHCAEQIRigATIHCAIQIRigATIHCAMQIRigATIHCAQQIRiPAtIBCTE1ODk4ajBqN6gCALACAA&sourceid=chrome&ie=UTF-8
colorama.init(autoreset=True)
#from _class_ import SCP
#from _class_ import n #importing temp value
#from docs import *
from collections import defaultdict
n = 'null'

def ChoiceSeparator(x):
    x = x
    print('-' * x)

MyDict = {'one':'two'}

def Menu():
    print(f'\nwhat would you like to do?\n\n',
          'Search the archive', ChoiceSeparator(10), '1\n',
          'Retrieve a random entry', ChoiceSeparator(5), '2\n',
          'Append the archive', ChoiceSeparator(10), '3\n',
          'Exit the archive', ChoiceSeparator(12), '4')
    menu_choice = int(input('>'))
    if menu_choice == 1:
        Search()
    elif menu_choice == 2:
        Random()
    elif menu_choice == 3:
        Append()
    elif menu_choice == 4:
        Exit()

def Exit():
    webbrowser.open('https://www.youtube.com/watch?v=dQw4w9WgXcQ')
    sys.exit

def Search():
    SearchInput = str(input('What word would you like to define?\n\n\n> ').lower())
    if SearchInput in MyDict.keys:
        print('I work')
    elif SearchInput == "house":
        print(f'\n\n\n\n\n{Fore.BLUE}House', '\n\n\n\n\nThis is not for you.\n\n\n\n\n')

def Random():
    return random

def Append():
    n

Menu()