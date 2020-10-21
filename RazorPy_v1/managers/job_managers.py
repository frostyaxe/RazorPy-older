'''
Created on Oct 10, 2020

@author: Sangeeta-Laptop
'''
from managers.services_object_manager import ObjectManager
import sys

class JobManager(object):
    
    def __init__(self, jobs_json_obj):
        self.__jobs_json_obj = jobs_json_obj
        self.__services_object_manager = None
        
    def read(self):
        jobs = self.__jobs_json_obj['jobs']
        for job in jobs:
            self.__services_object_manager = ObjectManager()
            get_services_dict = self.__services_object_manager.get()
            job_modules = job.keys() 
            for job_module in job_modules:
                if(job_module in get_services_dict):
                    service_obj = get_services_dict[job_module]
                    tasks = job[job_module]
                    for task,value in tasks.items():
                        if( hasattr(service_obj, task)):
                            setattr(service_obj,task,  value)
                           
                    service_obj.execute()    
                    
                else:
                    sys.exit("Unable to find service : : {0}".format(job_module))
        
        
        