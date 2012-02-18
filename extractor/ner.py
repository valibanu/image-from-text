'''
Created on Feb 18, 2012

@author: Vali
'''

import nltk

def _get_tree_text(tree):
   pass 

def extract_entity_names(t, ent_type="GPE"):
    entity_names = []
    
    if isinstance(t, nltk.tree.Tree):
        if t.node == ent_type:
            entity_names.append(' '.join([child[0] for child in t]))
        else:
            for child in t:
                entity_names.extend(extract_entity_names(child, ent_type=ent_type))
                
    return entity_names

def get_named_entities(paragraph, ent_type):
    sentences = nltk.sent_tokenize(paragraph)
    tokenized_sentences = [nltk.word_tokenize(sentence) for sentence in sentences]
    tagged_sentences = [nltk.pos_tag(sentence) for sentence in tokenized_sentences]
    chunked_sentences = nltk.batch_ne_chunk(tagged_sentences)

    entity_names = []
    for tree in chunked_sentences:
        entity_names.extend(extract_entity_names(tree, ent_type))
    
    keywords = ''
    for ent in entity_names:
        keywords = keywords + ' ' + ent

    return keywords
