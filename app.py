import pickle
from flask import Flask, request
import json
from sklearn.naive_bayes import ComplementNB
from sklearn.pipeline import make_pipeline, Pipeline

with open('model.sav', 'rb') as f:
    model: Pipeline = pickle.load(f)
    
def appropriate(text):
    labels = ['inappropriate', 'appropriate']
    return labels[model.predict([text])[0]]

app = Flask(__name__)

@app.route('/', methods=['POST'])
def predict():
    text = request.get_json()
    if text:
        text = text['text']
    return json.dumps({'appropriate':appropriate(text)})

if __name__ == '__main__':
    app.run(debug=True)