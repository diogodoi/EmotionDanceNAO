# -*- encoding: UTF-8 -*-
import os
import cv2
import shutil as sh
import random as rd
import pandas as pd
import numpy as np
import itertools
from sklearn.model_selection import train_test_split
import matplotlib.pyplot as plt
from tensorflow.python.keras.models import model_from_json
from sklearn.metrics import confusion_matrix
import seaborn as sns
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score


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

faces, emotions = getSample(500)

X_train, X_test, y_train, y_test = train_test_split(faces, emotions, test_size = 0.1, random_state = 42) # divisão da base de dados de treinamento e de teste 
X_train, X_val, y_train, y_val = train_test_split(X_train, y_train, test_size = 0.1, random_state = 41)

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