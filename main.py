'''
Created on Feb 18, 2012

@author: Vali
'''
import sys

from bing.bingimagesearch import BingImageSearch
from extractor.clean import clean_input, get_paragraphs
from extractor.ner import get_named_entities


if __name__ == '__main__':
    input = sys.argv[1]
#    input = u"Every story;;http://www.3applesbookaward.org/yr/promote/images/GreenApple.jpg;;http://doh.sd.gov/diabetes/img/GreenApples.jpg;;http://www.wallpapers.manbiz.eu/wallpapers/green_apples-1280x800.jpg"
#    input = clean_input(input)
#    print(input)
    
    bing = BingImageSearch()    
    for paragraph in get_paragraphs(input):
#        print(paragraph)
        keywords = get_named_entities(paragraph, 'ORGANIZATION')
        if not keywords:
            keywords = get_named_entities(paragraph, 'GPE')
        if not keywords:
            keywords = get_named_entities(paragraph, 'PERSON')
        if not keywords:
            keywords = paragraph
#        print('\n' + keywords)
        picture_urls = [pic.url for pic in bing.search(keywords)]
        print('{0};;{1}'.format(paragraph,
                                ';;'.join(picture_urls)))
