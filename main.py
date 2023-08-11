# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
from movimentos import danca_1,danca_init_2,danca_final_2,danca_3,danca_4,danca_5
import math
from video import VideoRecord
# Para salvar o modelo no formato json
from evaluatePose import Evaluate
from twisted.internet import reactor, defer
import threading
from time import sleep

IP = "192.168.0.251"
PORT = 9559

class Movimentos:
    def __init__(self, IP,PORT):
        self.motion = ALProxy("ALMotion",IP,PORT)
        self.tts = ALProxy("ALTextToSpeech",IP,PORT)
        self.posture = ALProxy("ALRobotPosture",IP,PORT)
        self.aup = ALProxy("ALAudioPlayer", IP, PORT)
        self.moves = [danca_1.MoveFirst,danca_3.MoveThird,danca_4.MoveFour,danca_5.MoveFive,[danca_init_2.MoveSecond_init,danca_final_2.MoveSecond_final]]
        self.audio = ['dance_1.mp3','dance_3.mp3','dance_4.mp3','dance_5.mp3','dance_2.mp3']
        self.delay = [16,10,13,9,11]
    def executa_movimento(self,index):
        self.motion.wakeUp()
        # self.motion.setStiffnesses(1.0)
        self.posture.goToPosture("Stand",0.5)
        move = self.moves[index]
        audio = self.audio[index]
        if type(move)!= list:
            names, keys, times = move()
            # self.aup.post.playFile("/home/nao/audios/"+audio)
            self.motion.post.angleInterpolation(names,keys,times,True)
        else:
            names,keys,times = move[0]()
            names1,keys1,times1 = move[1]()
            theta = -1 * math.pi/2
            self.motion.post.angleInterpolation(names,keys,times,True)
            self.posture.goToPosture("StandInit",0.5)
            self.motion.moveTo(0,0,theta)
            self.motion.post.angleInterpolation(names1,keys1,times1,True)
        
        self.posture.goToPosture("Stand",0.5)
        

# if __name__ == '__main__':
#     moves = Movimentos(IP=IP,PORT=PORT)
#     movesScores = []
#     print("Iniciando...")
#     for i in range(5):
#         video = VideoRecord()
#         video.run()
#         print("Movimento " + str(i))
#         moves.executa_movimento(i)
#         video.stopRecording()
#         print('Calculando a pontuação da pose.')
#         values = video.emotionList
#         print(values.__len__)
#         final = Evaluate(values).final_score()
#         movesScores.append({'pose':i,'score':final})

#     print(movesScores)



if __name__ == '__main__':
    moves = Movimentos(IP=IP, PORT=PORT)
    movesScores = []
    print("Iniciando...")

    threads = []
    for i in range(5):
        video = VideoRecord()
        print("Movimento " + str(i))
        thread_move = threading.Thread(target=moves.executa_movimento,args=(i,))
        thread_video = threading.Thread(target=video.run)
        thread_delay = threading.Thread(target=video.stopRecording,args=(moves.delay[i],))
        thread_move.start()
        thread_delay.start()
        thread_video.start()
        thread_move.join()
        thread_video.join()
        thread_delay.join()
        print('Calculando a pontuação da pose.')
        values = video.emotionList
        print('Tamanho da lista:', len(values))
        final = Evaluate(values).final_score()
        movesScores.append({'pose': i, 'score': final})
    
    print(movesScores)


    