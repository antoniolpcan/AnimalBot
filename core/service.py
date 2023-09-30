from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import matplotlib.pyplot as plt
from PIL import Image
from wordcloud import WordCloud
from goose3 import Goose
import en_core_web_sm
import time
import random
import spacy
import nltk

class Chat():

  def __init__(self, name: str, type: str):
    nltk.download('punkt')
    url = self.select_type(type)
    g = Goose()
    self.article = g.extract(url)
    #self.nlp = spacy.load('en_core_web_sm')
    self.nlp = spacy.load("pt_core_news_sm")
    self.original_sentences = [sentence for sentence in nltk.sent_tokenize(self.article.cleaned_text)]
    print(self.original_sentences)
    self.welcome_words_input = ['olá', 'oi', 'eae'] 
    self.welcome_words_output = [f'Eae {name}!\n', f'Oi, {name}!\n',f'Olá, {name}!\n', f'Bem vindo(a)!\n', f'Olá!! Seja bem vindo(a)\n'] 

  def get_cleaned_text(self):
    return self.preprocessing(self.article.cleaned_text)

  def select_type(self, type):
    if type == "Animais Carnívoros":
      return "https://www.biologianet.com/zoologia/animais-carnivoros.htm"
    elif type == 'Animais Herbívoros':
      return "https://www.biologianet.com/zoologia/animais-herbivoros.htm"
    else:
      return "https://www.biologianet.com/zoologia/animais-onivoros.htm"

  def welcome_message(self, text):
    for word in text.split():
      if word.lower() in self.welcome_words_input: 
        return random.choice(self.welcome_words_output) 

  def preprocessing(self, sentence):
      sentence = sentence.lower()

      tokens = []
      tokens = [token.text for token in self.nlp(sentence) if not (token.is_stop or token.like_num
                                                              or token.is_punct or token.is_space
                                                              or len(token)==1)]
      tokens=' '.join([element for element in tokens])
      return tokens

  def answer(self, user_text, threshold = 0.25):
      cleaned_sentences = []
      for sentence in self.original_sentences:
        cleaned_sentences.append(self.preprocessing(sentence))
      print(cleaned_sentences)
      user_text = self.preprocessing(user_text)
      cleaned_sentences.append(user_text)

      tfidf = TfidfVectorizer()
      x_sentences = tfidf.fit_transform(cleaned_sentences)

      similarity = cosine_similarity(x_sentences[-1], x_sentences)

      sentence_index = similarity.argsort()[0][-2] 
      chatbot_answer = ''

      if similarity[0][sentence_index] < threshold:
        chatbot_answer += 'Desculpe... não consigo responder isso...'
      else:
        chatbot_answer += self.original_sentences[sentence_index]

      return chatbot_answer


