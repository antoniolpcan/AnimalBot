import spacy

nlp = spacy.load('en_core_web_sm')

def preprocess(sentence):
    sentence = sentence.lower()

    tokens = []
    tokens = [token.text for token in nlp(sentence) if not (token.is_stop or 
    token.like_num or token.is_punct or token.is_space or len(token) ==1 )]

    tokens = ' '.join([element for element in tokens])
    return tokens