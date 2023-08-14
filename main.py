# -*- encoding: UTF-8 -*-
import math
from video import VideoRecord
# Para salvar o modelo no formato json
from evaluatePose import Evaluate
import threading
from Movimentos import Movimentos
from time import sleep

IP = "192.168.0.251"
PORT = 9559
moves = Movimentos(IP,PORT)

if __name__ == '__main__':
    print("Iniciando...")
    movesScores = []
    moves.backtoInit()
    for i in range(5):
        video = VideoRecord(moves)
        print("Movimento " + str(i))
        video.run(i)
        print('Calculando a pontuação da pose.')
        values = video.emotionList
        final = Evaluate(values).final_score()
        movesScores.append({'pose': i, 'score': final})
        moves.backtoInit()
    
    lista_ordenada = sorted(movesScores, key=lambda x: x['score'], reverse=True)
    new_move = poses_ordenadas = [item['pose'] for item in lista_ordenada]
    
    print("Reordenando a dança...")    
    sleep(180)
    print('De acordo com o sistema o ranking das poses foram:',new_move)
    print('Iniciando a nova dança.')
    new_move = [0,1,2,3,4]
    for i in new_move:
        moves.executa_movimento(i)
        sleep(18)
    
    moves.backtoInit()


    