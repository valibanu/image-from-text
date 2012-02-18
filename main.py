'''
Created on Feb 18, 2012

@author: Diana
'''
from bing.bingimagesearch import BingImageSearch

if __name__ == '__main__':
    bing = BingImageSearch() 
    for pic in bing.search('green apples'):
        print(pic)