# -*- encoding: UTF-8 -*-
import cv2
import time

from tensorflow.python.keras.models import load_model
# Para salvar o modelo no formato json
from tensorflow.python.keras.models import model_from_json
import numpy as np

class VideoRecord:
    def __init__(self):
        self.cap = cv2.VideoCapture(0)
        
        self.expressoes = [1,-1]
        arquivo_modelo = 'cnn_expressoes.h5' # referente aos pesos
        arquivo_modelo_json = 'cnn_expressoes.json' # referente a arquitetura da Rede Neural
        
        # Código para recepção do open (carregando o modelo salvo no item 6)
        json_file = open(arquivo_modelo_json, 'r')
        loaded_model_json = json_file.read()
        json_file.close() # liberação de memória 

        # Fazendo a leitura do arquivo json para transformar esse para o modelo Tensorflow
        self.loaded_model = model_from_json(loaded_model_json)
        self.loaded_model.load_weights(arquivo_modelo)
        print(self.loaded_model)

        self.face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml') 
        self.running = True
        self.emotionList = []
    
    def scoreEmotion(self,face):
        faces = self.face_cascade.detectMultiScale(face, 1.04, 5)
        lista_frames = []
        if len(faces) == 0:
            print(faces)
            return 0
        else:
            for x,y,w,h in faces:
                face_cut = face[y:y+h,x:x+w]
                toGray = cv2.cvtColor(face_cut,cv2.COLOR_RGB2GRAY)
                resized = cv2.resize(toGray, (48,48))
                normalized = resized.astype('float')/255
                # print(normalized)
                to_predict = np.expand_dims(normalized, -1)
        #         lista_frames.append(normalized)
                cv2.imshow('webcam',normalized)

                try:                        
                    prediction = self.loaded_model.predict(to_predict)
                    print(prediction)
        #             score = self.expressoes[int(np.argmax(prediction[-1]))]
        #             # return score
                except:
                    print('Erro')
        
        
    def startRecording(self):
        ret,frame = self.cap.read()        
        return ret,frame
    
    def stopRecording(self):
        self.running = False
        self.cap.release()
        cv2.destroyAllWindows()
        return self.score
    
    def run(self):
        self.score = 0
        while self.running:
            ret,frame = self.startRecording()
            
            self.scoreEmotion(frame)
            
            if not ret:
                break
            # cv2.imshow('Webcam',frame)
            
            if cv2.waitKey(1) & 0xFF ==ord('q'):
                break
        self.stopRecording()
            

video = VideoRecord()
video.run()


