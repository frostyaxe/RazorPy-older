

class RazorPyException(Exception):
    '''
    Created on Oct 3, 2020
    
    @author: Sangeeta-Laptop
    '''
    
    
    def __init__(self, message_id):
        super().__init__(self.__get_message(message_id))


    def __get_message(self,message_id):
        
        if message_id == "Invalid_Args":  # App Name not found        
            return "Invalid number of arguments passed. Required 2 arguments!"
        
        