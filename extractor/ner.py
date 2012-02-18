'''
Created on Feb 18, 2012

@author: Vali
'''

import nltk

def extract_entity_names(t):
    entity_names = []
    
    if hasattr(t, 'node') and t.node:
        if t.node == 'NE':
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child))
                
    return entity_names

def ne_preprocess(paragraph):
#    sentences = nltk.sent_tokenize(paragraph)
#    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
#    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
#    chunked_sentences = nltk.batch_ne_chunk(tagged_sentences)

    sentences = nltk.sent_tokenize(paragraph)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.batch_ne_chunk(tagged_sentences, binary=True)

    entity_names = []
    for tree in chunked_sentences:
        # Print results per sentence
        # print extract_entity_names(tree)
        entity_names.extend(extract_entity_names(tree))
    
    # Print all entity names
    #print entity_names
    # Print unique entity names
    print set(entity_names)
    # Print entity tree
    chunked_sentences = nltk.batch_ne_chunk(tagged_sentences)
    print(chunked_sentences)
    
    