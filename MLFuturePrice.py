# Notused...
import numpy as np
import tensorflow as tf
from tensorflow import keras
from bs4 import BeautifulSoup
from urllib.request import urlopen, Request
import pandas as pd

data_train_file = "PriceData2.csv"
data_path = '/Users/conradpereira/Desktop/Spring2020/Gesher/Stock-Price-Close-Predictor/PriceData2.csv'



df_train = pd.read_csv(data_train_file)
df_train.head()


# if label is float
df_train.fillna(3, inplace=True)
df_train.Increase = df_train.Increase.astype(int)

def get_feature_labels(df):
  features = df.values[:, 1:]
  labels = df['Increase'].values
  return(features, labels)

train_features, train_labels = get_feature_labels(df_train)
train_labels = tf.keras.utils.to_categorical(train_labels)
train_features.shape


model = tf.keras.Sequential()
model.add(tf.keras.layers.Dense(64, activation=tf.nn.relu, input_shape=(2,)))
model.add(tf.keras.layers.Dense(64, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(64, activation=tf.nn.relu))
model.add(tf.keras.layers.Dense(2, activation=tf.nn.softmax))



model.compile(loss='binary_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

model.fit(train_features, train_labels, epochs=10, batch_size=1, shuffle=True, validation_split=.1)
