#coding:utf-8
import os
import cv2
import random as rd
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from tensorflow.python.keras.models import Sequential,Model
from tensorflow.python.keras.layers import Dense, Dropout, Activation, Flatten
from tensorflow.python.keras.layers import Conv2D, MaxPooling2D, BatchNormalization
from tensorflow.python.keras.losses import categorical_crossentropy
from tensorflow.python.keras.optimizers import Adam
from tensorflow.python.keras.callbacks import ReduceLROnPlateau, EarlyStopping, ModelCheckpoint
from tensorflow.python.keras.models import load_model
from tensorflow.python.keras.models import model_from_json
from sklearn.metrics import confusion_matrix
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import matplotlib.pyplot as plt

path = 'DataEmotion/archive/test/'
def emocao(pasta):
    if 'angry' in pasta:
        return 0
    elif 'fear' in pasta:
        return 1
    elif 'sad' in pasta:
        return 2
    elif 'neutral' in pasta:
        return 3
    elif 'happy' in pasta:
        return 4
    elif 'surprise' in pasta:
        return 5


def normalizar(x):
    x = x.astype('float32') 
    x = x / 255.0
    return x 

def getSample(sampleSize):
    faces = []
    emotions = []
    for i,j,k in os.walk(path):
        if k.__len__() == 0:
            continue
        sample = rd.sample(k,sampleSize)
        emotion = emocao(i)
        for imgPath in sample:
            img = cv2.imread(i+"/"+imgPath)
            toGray = cv2.cvtColor(img,cv2.COLOR_RGB2GRAY)
            faces.append(toGray)
            emotions.append(emotion)
            
    faces = np.asarray(faces)
    faces = normalizar(faces)
    faces = np.expand_dims(faces, -1)
    emocoes = pd.get_dummies(emotions).values
    return faces,emocoes

faces, emotions = getSample(2000)

X_train, X_test, y_train, y_test = train_test_split(faces, emotions, test_size = 0.1, random_state = 42) # divisão da base de dados de treinamento e de teste 
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size = 0.1, random_state = 41)

# Criação de variáveis 
num_labels = 6
# temos sete classe/emoções
width, height = 48, 48 # parâmetros altura e largura das imagens em pixels

cnn_model = Sequential()
cnn_model.add(Conv2D(6,kernel_size=(3,3),activation='relu',input_shape=(width, height,1), data_format = 'channels_last'))
cnn_model.add(MaxPooling2D(pool_size=(2,2)))
cnn_model.add(Conv2D(16,kernel_size=(3,3),activation='relu'))
cnn_model.add(MaxPooling2D(pool_size=(2,2)))
cnn_model.add(Conv2D(120,kernel_size=(3,3),activation='relu'))
cnn_model.add(Dropout(0.1))
cnn_model.add(Flatten())
cnn_model.add(Dense(84, activation='relu'))
cnn_model.add(Dropout(0.3))
cnn_model.add(Dense(num_labels, activation='softmax'))

cnn_model.compile(loss = 'categorical_crossentropy', # define o erro
              optimizer = Adam(lr= 0.0001, beta_1=0.9, beta_2=0.999, epsilon=1e-7), # atualiza os pesos onde beta indica a taxa de decaimento exponencial relacionado com a taxa de aprendizagem
              metrics = ['accuracy']) 

arquivo_modelo = 'cnn_expressoes.h5' # referente aos pesos
arquivo_modelo_json = 'cnn_modelo_expressoes.json' # referente a arquitetura da Rede Neural


lr_reducer = ReduceLROnPlateau(monitor='val_loss', factor = 0.9, patience=3, verbose = 1) # caso a callbacks seja executada demosntrará as mensagens
early_stopper = EarlyStopping(monitor='val_loss', min_delta=0, patience = 8, verbose = 1, mode = 'auto') # para o treinamento antes do atingimento do plateau
checkpointer = ModelCheckpoint(arquivo_modelo, monitor='val_loss', verbose = 1, save_best_only=True) # o save_best_only=True permite que o checkpointer, quando o valor do erro diminuir, ele vai salvando o modelo, sobrescrevendo o melhor modelo.

cnn_model_json = cnn_model.to_json()
with open(arquivo_modelo_json, 'w') as json_file:
  json_file.write(cnn_model_json)

batch_size = 16 # indica de qtos em qtos registros será feita a atualização dos pesos da RN, recalculo do erro a cada 64 registro
epochs = 100 # será executado por 100 épocas o algorítmo 

cnn_history = cnn_model.fit(np.array(X_train), np.array(y_train),
                    batch_size = batch_size,
                    epochs = epochs,
                    verbose = 1,
                    validation_data = (np.array(X_val), np.array(y_val)),
                    shuffle=True, 
                    callbacks=[lr_reducer,checkpointer]) 


arquivo_modelo = 'cnn_expressoes.h5' 
arquivo_modelo_json = 'cnn_modelo_expressoes.json'

json_file = open(arquivo_modelo_json, 'r')
loaded_model_json = json_file.read()
json_file.close() 

loaded_model = model_from_json(loaded_model_json)
loaded_model.load_weights(arquivo_modelo)

y_pred = loaded_model.predict(X_test)
pred_y_discrete = [[1 if val == max(pred) else 0 for val in pred] for pred in y_pred]
cm = confusion_matrix(np.argmax(y_test, axis=1), np.argmax(pred_y_discrete,axis=1))


# Calculate accuracy
acc = accuracy_score(np.argmax(y_test, axis=1), np.argmax(pred_y_discrete, axis=1))

# Calculate precision
precision = precision_score(np.argmax(y_test, axis=1), np.argmax(pred_y_discrete, axis=1), average='weighted')

# Calculate recall
recall = recall_score(np.argmax(y_test, axis=1), np.argmax(pred_y_discrete, axis=1), average='weighted')

# Calculate F1-score
f1 = f1_score(np.argmax(y_test, axis=1), np.argmax(pred_y_discrete, axis=1), average='weighted')

print("Accuracy:", acc)
print("Precision:", precision)
print("Recall:", recall)
print("F1-score:", f1)
# # Defina os rótulos das classes
class_labels = ['angry', 'fear', 'sad', 'neutral', 'happy', 'surprise']

# # Crie um heatmap da matriz de confusão usando seaborn
plt.figure(figsize=(8, 6))
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues', xticklabels=class_labels, yticklabels=class_labels)
plt.xlabel('Predicted')
plt.ylabel('True')
plt.title('Confusion Matrix')
plt.show()