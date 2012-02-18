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
    return input

def ie_preprocess(document):
    sentences = nltk.sent_tokenize(document) 
    sentences = [nltk.word_tokenize(sent) for sent in sentences] 
    sentences = [nltk.pos_tag(sent) for sent in sentences]
    pprint.PrettyPrinter().pprint(sentences)

if __name__ == '__main__':
    s = clean_input(u"In 1856, the two principalities of Moldavia and Wallachia secured their autonomy and ended the suzerainty of the Ottoman Empire. In 1859 they united, and a national identity was born, adopting the name Romania in the following years. Formal recognition of its independence occurred in 1878. Following World War II, Romania was occupied by the Soviets, and a \"people's republic\" was formed in 1947. From 1965, under the regime of Nicolae Ceausescu, the Romanian people suffered impoverishment and oppression, until his overthrow and execution during the Revolution of 1989. \nRecent political events have seen Romania become a full member state of the European Union in June 2007.")
#    print(s)
    ie_preprocess(s)
#    for sen in s:
#        print(sen)
    

