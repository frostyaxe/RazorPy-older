'''
Created on Oct 10, 2020

@author: Sangeeta-Laptop
'''

from cowsay import tux,dragon,cheese
from sys import stderr,exit


class Cowsay:
    
    def __init__(self):
        self.__set_character = None
        self.__message = None
        
    @property
    def set_character(self):
        return self.__set_character
    
    @set_character.setter
    def set_character(self, cowsay_character):
        self.__set_character = cowsay_character
        
    @property
    def text(self):
        return self.__message
    
    @text.setter
    def text(self, message):
        self.__message = message
        
    
    def execute(self):
        '''
            This function must be present in each and every python module
        '''
        if(self.set_character is None):
            stderr.write('Please specify \'set_character\' value in yaml!')
            exit(1)
        if(self.text is None):
            stderr.write('Please specify \'text\' value in yaml!')
            exit(1)
        
        if(self.set_character.lower() == 'tux' ):
            tux(self.text) 
     
        elif(self.set_character.lower() == 'dragon' ):
            dragon(self.text)
        elif(self.set_character.lower() == 'cheese' ):
            cheese(self.text)
        else:
            print("Specified cowsay character :: {0} is not present!".format(self.set_character))