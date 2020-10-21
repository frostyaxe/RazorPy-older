'''
Created on Oct 10, 2020

@author: Sangeeta-Laptop
'''
import yaml
from managers import job_managers

class Application(object):
    
    def __init__(self):
        a_yaml_file = open("../resources/cowsay.yml")
        self.parsed_yaml_file = yaml.load(a_yaml_file, Loader=yaml.FullLoader)
        job_managers.JobManager(self.parsed_yaml_file).read()
    
    
    
Application()
    