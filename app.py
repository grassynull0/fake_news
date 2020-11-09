# To build this front end app, I followed youtube tutorials and github repos
import numpy as np
from flask import Flask, request,render_template
import pickle
import flask
import newspaper
from newspaper import Article
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import TfidfTransformer
import urllib
import os

app = Flask(__name__)
app=flask.Flask(__name__,template_folder='html_template')

with open('model_final.pickle', 'rb') as model:
    model2 = pickle.load(model)

@app.route('/')
def main():
    return render_template('main.html')

#Receiving the input url from the user and using Web Scrapping to extract the news content
@app.route('/predict',methods=['GET', 'POST'])
def predict():
    url = request.get_data(as_text=True)[5:]
    url = urllib.parse.unquote(url)
    article = Article(str(url))
    article.download()
    article.parse()
    article.nlp()
    news = article.summary
    #Passing the news article to the model and returing whether it is Fake or Real
    pred = model2.predict([news])
    return render_template('main.html', prediction_text='The news is "{}"'.format(pred[0]))
    
if __name__=="__main__":
    port=int(os.environ.get('PORT',5000))
    app.run(port=port,debug=True,use_reloader=False)
