from preprocess import preprocess
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data.sentences import sentences, fileToSpeak
from data.automatic import superSearch
import random


# Comparar a pergunta com a base
def answer(user_text, search=False):
    threshold = 0.25 
    newUrl = False
    cleaned_sentences = [] 

    if(search):
        newUrl = superSearch(user_text)

    sent = sentences(newUrl)

    
    if(sent is not None and len(sent) == 2): 
        # Atribuir recursos
        article = sent[0]
        original_sentences = sent[1]

        try:
            # Retirar stopwords
            for sentence in original_sentences: 
                cleaned_sentences.append(preprocess(sentence))

            # Base de conhecimento
            user_text = preprocess(user_text) 
            cleaned_sentences.append(user_text) 

            # Extrair índices TF-IDF das sentences
            tfidf = TfidfVectorizer() 
            x_sentences = tfidf.fit_transform(cleaned_sentences) 

            # Calcular similaridade com a pergunta do usuário
            similarity = cosine_similarity(x_sentences[-1], x_sentences) 
            sentence_index = similarity.argsort()[0][-2] 

            chatbot_answer = ''
            sent.clear()
            # Verificar a similaridade (porcentagem)
            if similarity[0][sentence_index] < threshold: 
                chatbot_answer += 'Not found'
            else: 
                chatbot_answer += original_sentences[sentence_index]
                return chatbot_answer
        except Exception as e:
            print('Erro inesperado')


def randomNumb(optionList): 
    size = len(optionList)
    if(size > 1): 
        size = size - 1
        number = random.randint(0, size)
        return number