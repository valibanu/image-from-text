'''
Created on Feb 18, 2012

@author: Vali
'''

import unicodedata
import re
import nltk
import pprint

def clean_content(c):
    c = unicodedata.normalize('NFKD', c).encode('ascii', 'ignore')
#    c = re.sub(r'\<.*/>', '', c)
#    c = re.sub(r'<\w+>', '', c)
#    c = re.sub(r'</\w+>', '', c)
    return c

def clean_sentence(s):
    s = re.sub(r'[^A-Za-z0-9\s-]+', '', s)
    return s

def clean_input(input):
    input = clean_content(input)
#    input = clean_sentence(input)
#    print(input)
#    return input.split('\n')
    return input.strip()

def get_paragraphs(input):
    return input.split('\n')


