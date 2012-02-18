'''
Created on Feb 18, 2012

@author: Vali
'''

from simple_bing import SimpleBing
from pprint import PrettyPrinter
from image import Image
import json

class BingImageSearch(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.bing = SimpleBing('6DDD22E2FDE6E12E755A1D96044041B13C64814F')
        
    def search(self, text, search_results=3):
        json_response = self.bing.search(query=text, sources='image', 
                                         image_count=search_results)
#        print(json_response)
#        obj = json.load(json_response)
#        for key in json_response['SearchResponse']:
#            print('{0} -> {1}'.format(key, json_response['SearchResponse'][key]))
        images = json_response['SearchResponse']['Image']['Results']
#        PrettyPrinter().pprint(images)
#        for key in images:
#            print('{0} -> {1}'.format(key, images[key]))
        for image in images:
            yield Image(image['MediaUrl'], image['Height'], image['Width'])
