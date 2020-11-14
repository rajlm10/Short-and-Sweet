from flask import Flask, render_template, url_for, request, redirect
import gensim
from nltk.corpus import stopwords
from nltk.cluster.util import cosine_distance
import numpy as np
import pickle

app = Flask(__name__)

# Looading the model
#model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin',limit=500000,binary=True)
model=pickle.load(open("dictionary","rb"))
print("model loaded")

# cosine similarity
def similarity(a,b):
    return np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))

def sentence_similarity(a,b):
    s1 = [word for word in a.split() if word not in set(stopwords.words('english'))-{'not'}]
    s2 = [word for word in b.split() if word not in set(stopwords.words('english'))-{'not'}]
    vec1 = np.zeros(300)
    vec2 = np.zeros(300)
    for i in range(len(s1)):
        #vec1 += model[s1[i]]
        vec1+=model.get(s1[i],0)
    for i in range(len(s2)):
        #vec2 += model[s2[i]]
        vec2+=model.get(s2[i],0)
    return similarity(vec1,vec2)

def summarize(text):
    sentences = text.split('.')
    check = []
    for i in range(len(sentences)):
        check.append(True)

    final_text = []
    for i in range(len(sentences)):
        for j in range(i + 1, len(sentences)):
            if check[i] == False or check[j] == False:
                continue
            if(i == j == len(sentences) - 1):
                continue
            elif (sentence_similarity(sentences[i], sentences[j]) <= 0.6):
                final_text.append(sentences[i])
                final_text.append(sentences[j])
            else:
                final_text.append(sentences[i])
                check[j] = False
    final_text = list(dict.fromkeys(final_text))
    result = ".".join(final_text)
    return result

@app.route('/')
def welcome():
    return render_template('homePage.html')


@app.route('/details', methods = ['POST', 'GET'])
def details():
    inputText = request.form['para']
    outputText = summarize(inputText)
    return render_template('details.html', name = outputText)

if __name__ == "__main__":
    app.run(debug=True)
