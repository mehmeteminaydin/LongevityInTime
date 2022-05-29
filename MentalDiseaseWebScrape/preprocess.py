import pandas as pd
df = pd.read_csv('mental_health.csv')


#imports for preprocessing
import nltk
import string
import re
from nltk.stem import WordNetLemmatizer
from nltk.corpus import stopwords
import nltk

#Download wordnet, stopwords and punkt list
nltk.download('wordnet')
nltk.download('stopwords')
nltk.download('punkt')
nltk.download('omw-1.4')

puncts_list = string.punctuation
stopword_list = stopwords.words('english')

def remove_num_and_stopwords(text):
    text = text.lower()
    temp = ''
    for word in text.split():
        if word not in stopword_list and not word.isnumeric():
            temp += str(word) + ' '
    return temp

def remove_puncts(text):
    text = remove_num_and_stopwords(text)
    temp = ''
    for char in text:
        if char not in puncts_list:
            temp += char
    temp = temp.lower()
    return temp

# lemmatizer of NLTK for english
lemmatizer = WordNetLemmatizer()

def lemmatize(text):
    text = remove_puncts(text)
    temp = ''
    for word in text.split():
        temp += lemmatizer.lemmatize(word) + ' '
    return temp




#join hashtags and tweets
df['linked'] = df['hashtags'] + df['tweet']

#apply preprocessing functions
df['preprocessed'] = df['linked'].apply(remove_puncts)

#save the preprocessed data
df.to_csv('preprocessed.csv')

