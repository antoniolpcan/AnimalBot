from wordcloud import WordCloud
from PIL import Image
import time
import random


""""""
def countWords(words):
    word = words.split()

    # Contar as word
    quantity = len(word)

    # Imprimir a contagem
    print("O texto contém", quantity, "word")
    return quantity


def newNumb(text, quantity):
    quantity = 7
    # Dividir  palavras
    words = text.split()

    # Selecionar aleatoriamente
    select = random.sample(words, quantity)
    newWord = " ".join(select)

    return newWord


def wcloud(text, tempFile):
    if(text is not None):
        count = countWords(text)
        text = newNumb(text, count)
        if(text):
            # Configurar a geração da nuvem de palavras com limite de palavras
            wordcloud = WordCloud(width=800, height=400).generate(text)

            # Salvar a nuvem de palavras em um arquivo de imagem
            wordcloud.to_file(tempFile)

            # Abrir a imagem com a PIL
            image = Image.open(tempFile)

            # Exibir a image em uma janela separada
            image.show()

            # Esperar por 5 segundos antes de fechar a image
            #time.sleep(5)

            # Fechar a janela da image (pode não funcionar em todos os sistemas)
            image.close()

# Exemplo de uso com limite de 10 palavras na nuvem
example_text = "Python é uma linguagem de programação muito popular. É fácil de aprender e poderosa."

wcloud(example_text, "w_cloud.png")
# Exemplo de texto


