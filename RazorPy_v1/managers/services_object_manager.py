'''
Created on Oct 10, 2020

@author: Sangeeta-Laptop
'''
import services
import pkgutil
import inspect
import importlib

class ObjectManager:
  
    def __init__(self):
        self.__results = {}
     
      
    def __init_services__(self):
        
        for importer, modname, ispkg in pkgutil.iter_modules(services.__path__):
            full_name = services.__name__ + '.' + modname
            imported_module = importlib.import_module(full_name)
            for name, obj in inspect.getmembers(imported_module):
                
                if inspect.isclass(obj) and str(obj).find('services') != -1:
                    self.__results[name.lower()] = obj()
                    
    
    def get(self):
        self.__init_services__()
        return self.__results
        
