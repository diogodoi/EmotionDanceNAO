# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
from movimentos import danca_1,danca_init_2,danca_final_2,danca_3,danca_4,danca_5
import math
# Para salvar o modelo no formato json


class Movimentos:
    def __init__(self, IP,PORT):
        self.motion = ALProxy("ALMotion",IP,PORT)
        self.tts = ALProxy("ALTextToSpeech",IP,PORT)
        self.posture = ALProxy("ALRobotPosture",IP,PORT)
        self.aup = ALProxy("ALAudioPlayer", IP, PORT)
        self.moves = [danca_1.MoveFirst,danca_3.MoveThird,danca_4.MoveFour,danca_5.MoveFive,danca_init_2.MoveSecond_init]
        self.audio = ['dance_1.mp3','dance_3.mp3','dance_4.mp3','dance_5.mp3','dance_2.mp3']
        
    def executa_movimento(self,index):
        self.motion.wakeUp()
        move = self.moves[index]
        audio = self.audio[index]
        names, keys, times = move()
        self.aup.post.playFile("/home/nao/audios/"+audio)
        self.motion.post.angleInterpolation(names,keys,times,True)
        
    def backtoInit(self):
        self.posture.goToPosture("Stand",0.5)