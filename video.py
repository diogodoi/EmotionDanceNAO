# -*- encoding: UTF-8 -*-
import cv2
# Para salvar o modelo no formato json
from tensorflow.python.keras.models import model_from_json
import numpy as np
import threading
from time import sleep

class VideoRecord:
    def __init__(self):
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
                    return prediction
                except:
                    print('Erro')
        
        
    def startRecording(self):
        ret,frame = self.cap.read()        
        return ret,frame
    
    def stopRecording(self,time):
        print('iniciou')
        sleep(time)
        print('Encerrou')
        self.running = False
        # self.cap.release()
        # cv2.destroyAllWindows()
    
    def run(self):
        self.score = 0
        while True:
            ret,frame = self.startRecording()
            
            value = self.scoreEmotion(frame)
            self.emotionList.append(value)
            if self.running==False:
                break
            
            # if not ret:
            #     break
            # cv2.imshow('Webcam',frame)
            
        #     if cv2.waitKey(1) & 0xFF ==ord('q'):
        #         break
        # self.stopRecording()

        
        
