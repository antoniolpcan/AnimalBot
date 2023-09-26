import spacy
import random
from spacy.util import minibatch, compounding
from spacy.training import Example

# Carregue um modelo em branco
nlp = spacy.blank('pt')
path = "../../data/training/"

# Adicione o componente NER ao pipeline
if "ner" not in nlp.pipe_names:
    ner = nlp.add_pipe("ner")
else:
    ner = nlp.get_pipe("ner")

# Definir rótulos
ner.add_label("leão")
ner.add_label("águia")
ner.add_label("golfinhos")
ner.add_label("urso polar")
ner.add_label("cavalos")
ner.add_label("tartarugas")
ner.add_label("elefantes")
ner.add_label("pinguins")
ner.add_label("tigres")
ner.add_label("lobo")
ner.add_label("pandas")
ner.add_label("coelhos")
ner.add_label("crocodilos")
ner.add_label("macacos")
ner.add_label("baleias")
ner.add_label("gatos")
ner.add_label("cobras")
ner.add_label("camaleões")
ner.add_label("cangurus")
ner.add_label("morcegos")

# Treinamento
TRAIN_DATA = [
    ("O leão é o rei da selva.", {"entities": [(2, 6, "leão")]}),
    ("Vi uma águia voando alto no céu.", {"entities": [(7, 12, "águia")]}),
    ("Os golfinhos são conhecidos por sua inteligência.", {"entities": [(3, 11, "golfinhos")]}),
    ("O urso polar vive no Ártico.", {"entities": [(2, 11, "urso polar")]}),
    ("Os cavalos são animais muito fortes.", {"entities": [(3, 10, "cavalos")]}),
    ("As tartarugas podem viver por muitos anos.", {"entities": [(3, 12, "tartarugas")]}),
    ("Os elefantes têm trombas longas.", {"entities": [(3, 12, "elefantes")]}),
    ("Os pinguins são aves que não voam.", {"entities": [(3, 10, "pinguins")]}),
    ("Os tigres são felinos muito ágeis.", {"entities": [(3, 9, "tigres")]}),
    ("Vi um lobo na floresta.", {"entities": [(7, 11, "lobo")]}),
    ("Os pandas são adoráveis e comem bambu.", {"entities": [(3, 9, "pandas")]}),
    ("Os coelhos são conhecidos por suas orelhas grandes.", {"entities": [(3, 10, "coelhos")]}),
    ("Os crocodilos vivem em áreas aquáticas.", {"entities": [(3, 12, "crocodilos")]}),
    ("Os macacos são animais muito brincalhões.", {"entities": [(3, 9, "macacos")]}),
    ("As baleias são os maiores mamíferos marinhos.", {"entities": [(3, 9, "baleias")]}),
    ("Os gatos são animais de estimação populares.", {"entities": [(3, 7, "gatos")]}),
    ("As cobras são répteis rastejantes.", {"entities": [(3, 8, "cobras")]}),
    ("Os camaleões têm a capacidade de mudar de cor.", {"entities": [(3, 12, "camaleões")]}),
    ("Os cangurus são conhecidos por saltar longas distâncias.", {"entities": [(3, 10, "cangurus")]}),
    ("Os morcegos são mamíferos voadores.", {"entities": [(3, 10, "morcegos")]}),
]


# Preparar os dados de treinamento
examples = []
for text, annotations in TRAIN_DATA:
    doc = nlp.make_doc(text)
    example = Example.from_dict(doc, annotations)
    examples.append(example)

# Iniciar o treinamento
nlp.begin_training()

# Número de iterações de treinamento
for itn in range(80):
    # Embaralhar os dados
    random.shuffle(examples)
    losses = {}

    # Lotes com os dados de treino
    batches = minibatch(examples, size=compounding(4.0, 32.0, 1.001))
    for batch in batches:
        nlp.update(batch, drop=0.5, losses=losses)

    print("Losses", losses)

# Salvar o modelo treinado
nlp.to_disk(path)
