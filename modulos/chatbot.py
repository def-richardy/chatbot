from modulos.simplify import *
from time import sleep
from fuzzywuzzy import fuzz
from random import randint, choice
from os import system
from gtts import gTTS
from playsound import playsound


palpites_maior = ['Que porra de chute é esse? calma ai neymar, menos que isso...', 'Passou longe, é menos que isso...', 'calma vida tá nervoso? menos...', 'kkkkk você é foda hein, eu disse menor...', 'tô me cansando disso kkkkkk']
palpites_menor = ['Um pouco maior...', 'Quase lá, é um pouco maior, tenta de novo...', 'Tô me cansando disso kkkkk...', 'Hmmm, é menor que isso...']

class ChatBot():
    def __init__(self):
        self.training_data = list()
    
    def training(self):
        self.training_data = ler_Json(self.training_data, 'data/data.json')
    
    def get_response(self):
        self.ask = input('Você: ').lower()
        for speech in self.training_data:
            self.match = fuzz.token_set_ratio(self.ask, speech)
            index = self.training_data.index(speech) + 1
            if self.match > 60:
                audio = gTTS(self.training_data[index], lang='pt')
                audio.save('kyon_speech.mp3')
                playsound('kyon_speech.mp3')
                print(f'kyon: {self.training_data[index]}')
                break
            else:
                continue

        if self.ask not in self.training_data:
            if self.match > 60:
                pass
            else:
                print('Kyon: Eu não tenho uma resposta pra isso.')
    
    def game_adivinhar(self):
        number = randint(1, 50)
        print('Kyon: Eu pensei em um número de 1 a 50, tente adivinhar...')
        while True:
            ask = int(input('Você: '))
            if ask < number:
                print(f'Kyon: {choice(palpites_menor)}')
            elif ask > number:
                print(f'Kyon: {choice(palpites_maior)}')
            elif ask == number:
                print(f'Kyon: finalmente acertou')
                break

    def get_date(self):
        self.data = obter_data()