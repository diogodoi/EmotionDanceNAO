# -*- encoding: UTF-8 -*-
import cv2
# Para salvar o modelo no formato json
from tensorflow.python.keras.models import model_from_json
import numpy as np
from time import sleep,time
from Movimentos import Movimentos

class VideoRecord:
    def __init__(self,IP,PORT):
        self.cap = cv2.VideoCapture(0)
        
        arquivo_modelo = 'cnn_expressoes.h5' # referente aos pesos
        arquivo_modelo_json = 'cnn_modelo_expressoes.json' # referente a arquitetura da Rede Neural
        
        # Código para recepção do open (carregando o modelo salvo no item 6)
        json_file = open(arquivo_modelo_json, 'r')
        loaded_model_json = json_file.read()
        json_file.close() # liberação de memória 

        # Fazendo a leitura do arquivo json para transformar esse para o modelo Tensorflow
        self.loaded_model = model_from_json(loaded_model_json)
        self.loaded_model.load_weights(arquivo_modelo)

        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
        self.running = True
        self.emotionList = []
        self.delay = [19,13,16,12,14]
        self.moves = Movimentos(IP=IP, PORT=PORT) # type: ignore
    
    def scoreEmotion(self,face):
        faces = self.face_cascade.detectMultiScale(face, 1.04, 5)
        lista_frames = []
        if len(faces) == 0:
            return 0
        else:
            for x,y,w,h in faces:
                face_cut = face[y:y+h,x:x+w]
                resized = cv2.resize(face_cut, (48,48))
                toGray = cv2.cvtColor(resized,cv2.COLOR_RGB2GRAY)                
                normalized = toGray.astype('float')/255
                new_dim = np.expand_dims(normalized, -1)
                lista_frames.append(new_dim)
                
                try:                        
                    prediction = self.loaded_model.predict(np.array(lista_frames))
                    print(prediction)
                    return prediction[0]
                except:
                    return None
        
        
    def startRecording(self):
        ret,frame = self.cap.read()        
        return ret,frame

    
    def run(self,index):
        self.moves.executa_movimento(index)
        start = time()
        while True:
            ret,frame = self.startRecording()
            final = time()
            delay_seconds = final - start 
            if delay_seconds>self.delay[index]:break
            value = self.scoreEmotion(frame)
            if (value is not 0):self.emotionList.append(value)
                

        

