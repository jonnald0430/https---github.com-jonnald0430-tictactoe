#when you import something, it's gonna look locally, your standard library location and lastly your third party library location
'''
# normal import
import modfolderexample.examplemod as examplemod
# import a certain function
from modfolderexample.examplemod import do_a_thing, do_another_thing
# import all the functions, unclear which is used tho so don't do it
from modfolderexample.examplemod import *
# import something as a certain variable or word
from modfolderexample.examplemod import do_a_thing as dat 

do_a_thing()
'''
# pip3 communicates with python package index
# imports are just a bunch of python code
# firewalls don't really catch from pip3
# could have viruses
# go to official package on python package index to check out code

# colorama example
from colorama import Fore, Back, Style
print(Fore.RED + 'some red text')
print(Back.GREEN + 'and with a green background')
print(Style.DIM + 'and in dim text')
print(Style.RESET_ALL)
print('back to normal now')
