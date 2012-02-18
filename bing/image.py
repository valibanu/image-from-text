'''
Created on Feb 18, 2012

@author: Diana
'''

class Image(object):
    '''
    classdocs
    '''


    def __init__(self, url, height, width):
        '''
        Constructor
        '''
        self.url = url
        self.height = height
        self.width = width
        
    def __str__(self):
        return self.url