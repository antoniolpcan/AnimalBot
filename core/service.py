import spacy
import en_core_web_sm
nlp = spacy.load('en_core_web_sm')
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import nltk
from goose3 import Goose

nltk.download('punkt')
url="https://gorillaz.fandom.com/wiki/Backstory"
g = Goose()
article = g.extract(url)


original_sentences = [sentence for sentence in nltk.sent_tokenize(article.cleaned_text)]
welcome_words_input = ['hey', 'hello', 'hi'] 
welcome_words_output = ['hey', 'hello', 'how are you?', 'welcome', 'how are you doing?'] 


import random

def welcome_message(text):
  for word in text.split():
    if word.lower() in welcome_words_input: 
      return random.choice(welcome_words_output) 

welcome_message('hey')

def preprocessing(sentence):
    sentence = sentence.lower()

    tokens = []
    tokens = [token.text for token in nlp(sentence) if not (token.is_stop or token.like_num
                                                            or token.is_punct or token.is_space
                                                            or len(token)==1)]
    tokens=' '.join([element for element in tokens])
    return tokens

def answer(user_text, threshold = 0.25):
    cleaned_sentences = []
    for sentence in original_sentences:
      cleaned_sentences.append(preprocessing(sentence))

    user_text = preprocessing(user_text)
    cleaned_sentences.append(user_text)

    tfidf = TfidfVectorizer()
    x_sentences = tfidf.fit_transform(cleaned_sentences)

    similarity = cosine_similarity(x_sentences[-1], x_sentences)

    sentence_index = similarity.argsort()[0][-2] 
    chatbot_answer = ''

    if similarity[0][sentence_index] < threshold:
      chatbot_answer += 'Sorry, I cant answer that yet!'
    else:
      chatbot_answer += original_sentences[sentence_index]

    return chatbot_answer


