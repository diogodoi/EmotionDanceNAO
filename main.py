# -*- encoding: UTF-8 -*-
from video import VideoRecord
from evaluatePose import Evaluate
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
    print("Por enquanto pense nas danças.")   
    sleep(60)
    print('Pense por mais um minuto')
    sleep(60)
    print('Iniciando nova dança em:')
    print('1')
    sleep(1)
    print('2')
    sleep(1)
    print('3')
    sleep(1)
    
    
    print('Iniciando a nova dança.')
    for i in new_move:
        moves.executa_movimento(i)
        sleep(18)
    
    moves.backtoInit()
    print('De acordo com o sistema o ranking das poses foram:',lista_ordenada)


    