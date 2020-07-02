import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import MultinomialNB
from Data_Preprocessing import *
from sklearn import preprocessing
import numpy as np
from sklearn.metrics import accuracy_score
from sklearn.pipeline import Pipeline
from sklearn.metrics import f1_score
from sklearn.ensemble import RandomForestClassifier
import pickle

#load dataset từ file text_data.csv ở trong cùng một thư mục với file model.py
def load_dataset():
    dataset = pd.read_csv("text_data.csv", encoding='ISO 8859-1')
    article = dataset.iloc[:,0]
    category = dataset.iloc[:,1]
    return article, category

#tiền xử lý dữ liệu (loại bỏ dấu câu, stop words,...)
def pre_processing(article):
    articles = preprocessing_dataset(article)
    return articles

#chuyển các nhãn đã quy ước về dạng số để phục vụ cho việc train, test model
def convert(y):
    number = preprocessing.LabelEncoder()
    y= number.fit_transform(y)
    return y, number

#train dữ liệu
def Train_data(X, y):
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2)
    pl = Pipeline([
    ('tfidf', TfidfVectorizer()),  
    ('classifier', MultinomialNB()),  
    ])
    model = pl.fit(X_train,y_train)
    print("Model Multinomial Naive Bayes: ")
    print("Train score: ", model.score(X_train, y_train))
    print("Test score: ", model.score(X_test, y_test))
    y_pred = model.predict(X_test)
    print("F1 score: ", f1_score(y_test, y_pred, average = "macro"))
    pl1 = Pipeline([
    ('tfidf', TfidfVectorizer()),  
    ('classifier', RandomForestClassifier()),  
    ])

    model1 = pl1.fit(X_train,y_train)
    print("Model Random Forest Classifier: ")
    print("Train score: ", model1.score(X_train, y_train))
    print("Test score: ", model1.score(X_test, y_test))
    y_pred1 = model1.predict(X_test)
    print("F1 score: ", f1_score(y_test, y_pred1, average = "macro"))
    return model

if __name__ == "__main__":
    article, category = load_dataset()
    articles = pre_processing(article)
    y, number = convert(category)
    model = Train_data(articles, y)
    #lưu model đã train vào file model.p
    pickle.dump(model, open("model.p", 'wb'))
    #lưu dữ liệu số của label đã được chuyển đổi
    pickle.dump(number, open("number.p", 'wb'))