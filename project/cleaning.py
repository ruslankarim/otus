import re
import nltk
from nltk.corpus import stopwords
import pymorphy2


def clean_text(text):
    text = text.lower()
    text = re.sub(r'\d+', '', text)                      # Удалить числа
    text = re.sub(r'[^\w\s]', '', text)                  # Удалить знаки препинания
    text = re.sub(r'\s+', ' ', text).strip()             # Удалить лишние пробелы
    return text

nltk.download('stopwords')
russian_stopwords = set(stopwords.words("russian"))

def remove_stopwords(text):
    words = text.split()
    return ' '.join(word for word in words if word not in russian_stopwords)


morph = pymorphy2.MorphAnalyzer()

def lemmatize_text(text):
    words = text.split()
    lemmas = [morph.parse(word)[0].normal_form for word in words]
    return ' '.join(lemmas)


def preprocess(text):
    text = clean_text(text)
    text = remove_stopwords(text)
    text = lemmatize_text(text)
    return text
