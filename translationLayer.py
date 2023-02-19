from rasa_nlu.training_data import load_data
from rasa_nlu.config import RasaNLUModelConfig
from rasa_nlu.model import Trainer
from rasa_nlu.model import Interpreter
from rasa_nlu import config
import spacy
import pathlib

train_data = load_data('rasa-dataset.json')
nlu_config = config.load('config_spacy.yml')
nlp = spacy.load('de')
trainer = Trainer(nlu_config)
trainer.train(train_data)
model_directory = trainer.persist('/projects/')
model_path = pathlib.Path(model_directory)
interpreter = Interpreter.load(model_path)

def translationLayer(inputText):
    result = interpreter.parse(inputText)
    intent = result['intent']['name']
    entities = result['entities']    
    return intent