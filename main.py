# -*- encoding: UTF-8 -*-
from naoqi import ALProxy
from movimentos import danca_1,danca_init_2,danca_final_2,danca_3,danca_4,danca_5
from time import sleep
import math
from video import VideoRecord

IP = "192.168.0.200"
PORT = 9559

class Movimentos:
    def __init__(self, IP,PORT):
        self.motion = ALProxy("ALMotion",IP,PORT)
        self.tts = ALProxy("ALTextToSpeech",IP,PORT)
        self.posture = ALProxy("ALRobotPosture",IP,PORT)
        self.moves = [danca_1.MoveFirst,[danca_init_2.MoveSecond_init,danca_final_2.MoveSecond_final],danca_3.MoveThird,danca_4.MoveFour,danca_5.MoveFive]
        
    def executa_movimento(self,index):
        self.motion.wakeUp()
        # self.motion.setStiffnesses(1.0)
        self.posture.goToPosture("Stand",0.5)
        move = self.moves[index]
        if type(move)!= list:
            names, keys, times = move()
            self.motion.angleInterpolation(names,keys,times,True)
        else:
            names,keys,times = move[0]()
            names1,keys1,times1 = move[1]()
            theta = -1 * math.pi/2
            self.motion.angleInterpolation(names,keys,times,True)
            self.posture.goToPosture("StandInit",0.5)
            self.motion.moveTo(0,0,theta)
            self.motion.angleInterpolation(names1,keys1,times1,True)
        
        self.posture.goToPosture("Stand",0.5)
        

if __name__ == '__main__':
    moves = Movimentos(IP=IP,PORT=PORT)
    print("Iniciando...")
    for i in range(5):
        print("Movimento " + str(i))
        moves.executa_movimento(i)
        sleep(5)




    