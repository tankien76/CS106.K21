from nltk.corpus import stopwords
from nltk.tokenize import regexp_tokenize
from nltk.tokenize import word_tokenize
import re
import string

#đưa văn bản về chữ thường 
def text_lowercase(text):
    return text.lower()

#loại bỏ số
def remove_number(text):
    text = str(text)
    result = re.sub(r'\d+', '', text) 
    return result

#loại bỏ các dấu chấm câu
def remove_punctuation(text): 
    translator = str.maketrans('', '', string.punctuation) 
    return text.translate(translator) 

#loại bỏ các stopwords trong tiếng Anh
def remove_stopwords(text): 
    stop_words = set(stopwords.words("english")) 
    word_tokens = word_tokenize(text) 
    filtered_text = [word for word in word_tokens if word not in stop_words] 
    filtered_text = " ".join(filtered_text)
    return filtered_text

def preprocessing_dataset(data):
    data_pred = []
    for i in data:
        i = str(i)
        text = text_lowercase(i)
        text = remove_number(text)
        text = remove_punctuation(text)
        text = remove_stopwords(text)
        data_pred.append(text)

    return data_pred
