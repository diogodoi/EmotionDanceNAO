# -*- encoding: UTF-8 -*-
import math
from video import VideoRecord
# Para salvar o modelo no formato json
from evaluatePose import Evaluate
import threading
from Movimentos import Movimentos

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
    print(new_move)
    for i in new_move:
        moves.executa_movimento(i)
    
    moves.backtoInit()


    