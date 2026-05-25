from wordcloud import WordCloud
import nltk as nltk
import numpy as np
import pandas as pd
import matplotlib.pyplot as pl
import warnings
from sklearn.linear_model import LogisticRegression
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score
import pickle
import statsmodels.api as sm

from sklearn.svm import SVC
#ABIR EL CSV PARA LA CARGA DE MENSAJES CYBERBULLYING
###################################################################################################
data = pd.read_csv("cyberbullying.csv", encoding='UTF-8')
print(data)


#df=sm.data.('weather', 'nycflights123').data
#print(df)

X = data['v1'].values
y = data['v2'].values
print(X)
print(y)


step=[('scaler',StandardScaler()),('classifiler',LogisticRegression())]
#pipe=make_pipeline(step)
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.2 , random_state= 0)
#pipe.fit(X_train,y_train)

########################
data = data.rename(columns={"v1": "mensajes", "v3": "etiqueta"})
print(data)
###########################################################################

data['etiqueta'].value_counts()
nltk.download("punkt")
warnings.filterwarnings('ignore')

not_cyberbullyinWords = ''
cyberbullyingWords = ''

#PALABRAS BULLYING Y NO BULLYING
###################################################################################################
for val in data[data['etiqueta'] == "cyberbullying"].mensajes:
    text = val.lower()                                                                          #convertir a minusculas
    tokens = nltk.word_tokenize(text)
    for words in tokens:
        cyberbullyingWords = cyberbullyingWords + words + ' '
for val in data[data['etiqueta'] == "not_cyberbullying"].mensajes:
    text = val.lower()                                                                          #convertir a minusculas
    tokens = nltk.word_tokenize(text)
    for words in tokens:
        not_cyberbullyinWords = not_cyberbullyinWords + words + ' '
###################################################################################################

#PARA IMPRIMIR LAS PALBRAS BULLYING Y NO_BULLYING EN LA FIGURA
##################################################################################################
Bullying_wordcloud = WordCloud(width = 1000, height = 500).generate(cyberbullyingWords)
Not_bullying_wordcloud = WordCloud(width = 1000, height = 500).generate(not_cyberbullyinWords)

pl.figure(figsize=(10,0), facecolor='w')
pl.imshow(Bullying_wordcloud)
#pl.show()                       #Enviamos figura cyberbullying
pl.imshow(Not_bullying_wordcloud)
#pl.show()                       #Enviamos figura not_cybebullying

###################################################################################################

#PARA IMPRIMIR PALABRAS EN POSICIONES 0=NO_CYBERBULLYING Y 1=CYBERBULLYING
###################################################################################################
data=data.replace(['not_cyberbullying', 'cyberbullying'], [0, 1])
print("Filas y columnas")
print(data)
###################################################################################################

#train - Test split

var = X_train.shape
var1=y_train.shape
var2=y_test.shape


#Preprocessing
cv = CountVectorizer()
cv.get_feature_names
    #Training by ML Algorithm

nb = MultinomialNB()
pipe = make_pipeline(cv, nb)
pipe.fit(X_train,y_train)
y_pred = pipe.predict(X_test)
accuracy_score(y_pred, y_test)

email = ['Hey i am Elon Musk. I hate you fucking kid']
pipe.predict(email)

pickle.dump(pipe, open("Naive_model.pkl",'wb'))