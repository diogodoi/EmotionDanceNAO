# -*- encoding: UTF-8 -*-
import math
from video import VideoRecord
# Para salvar o modelo no formato json
from evaluatePose import Evaluate
import threading

IP = "192.168.0.251"
PORT = 9559

if __name__ == '__main__':
    print("Iniciando...")
    movesScores = []
    for i in range(5):
        video = VideoRecord(IP,PORT)
        print("Movimento " + str(i))
        video.run(i)
        print('Calculando a pontuação da pose.')
        values = video.emotionList
        final = Evaluate(values).final_score()
        movesScores.append({'pose': i, 'score': final})
    
    print(movesScores)


    