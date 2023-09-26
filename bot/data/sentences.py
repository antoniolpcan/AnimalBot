import nltk
from goose3 import Goose

content = []
fileToSpeak = './AI_process/config.json'
option = 'Digite [N] para encerrar o programa'

def sentences(newUrl=False):
    try:
        if(newUrl):
            url = newUrl
        else:
            url = 'https://pt.wikipedia.org/wiki/Mam%C3%ADferos'


        article = Goose().extract(url)
        original_sentences = [sentence for sentence in nltk.sent_tokenize(article.cleaned_text)]
        content.append(article)
        content.append(original_sentences)
        return content
    except Exception as e:
        print('Ocorreu um erro ao acessar o link, tente mais tarde')